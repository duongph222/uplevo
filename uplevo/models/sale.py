# -*- coding: utf-8 -*-

from __future__ import print_function

import flask
from odoo import models, api
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import google.oauth2.credentials
import google_auth_oauthlib.flow


class Sale(models.Model):
    _inherit = 'sale.orders'

    @api.multi
    def share_file(self):
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            '../custom_addons/uplevo/uplevo/static/client_id.json', scopes=['https://www.googleapis.com/auth/drive'])
        flow.redirect_uri = 'http://localhost:8080'
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        return flask.redirect(authorization_url)
        state = flask.session['state']
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            'client_secret.json',
            scopes=['https://www.googleapis.com/auth/youtube.force-ssl'],
            state=state)
        flow.redirect_uri = flask.url_for('http://localhost:8080', _external=True)

        authorization_response = flask.request.url
        flow.fetch_token(authorization_response=authorization_response)

        credentials = flow.credentials
        flask.session['credentials'] = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}
        drive = build('drive', 'v2', credentials=credentials)
        files = drive.files().list().execute()
