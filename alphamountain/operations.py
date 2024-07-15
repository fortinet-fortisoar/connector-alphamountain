"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import requests, json
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('alphamountain')

API_VERSION = '1'
REQUEST_TYPE = 'partner.info'


class alphaMountain(object):

    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip()
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url
        self.verify_ssl = config.get('verify_ssl', False)
        self.api_key = config.get('api_key')
        self.headers = {'Content-Type': 'application/json'}
        self.version = API_VERSION
        self.request_type = REQUEST_TYPE

    def make_api_call(self, endpoint=None, method='POST', payload=None, params=None):
        service_endpoint = self.server_url + endpoint
        try:
            response = requests.request(method, service_endpoint, data=payload, headers=self.headers, params=params,
                                        verify=self.verify_ssl)
            logger.debug('API Payload: {0}'.format(payload))
            logger.debug('API Response Reason: {0}'.format(response.reason))
            logger.debug('API Service Endpoint: {0}'.format(service_endpoint))
            logger.debug('API Response Status code: {0}'.format(response.status_code))
            logger.debug('API Response: {0}'.format(response.text))
            if response.ok:
                return response.json()
            else:
                logger.error('Failed with response {0}'.format(response.text))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response.text})
        except requests.exceptions.SSLError as err:
            logger.error(err)
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout as err:
            logger.error(err)
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout as err:
            logger.error(err)
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError as err:
            logger.error(err)
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            logger.error(err)
            raise ConnectorError(str(err))


def get_payload(params, am):
    input_type = params.get('input_type', '')
    limit = params.get('limit', '')
    payload = {'version': am.version, 'license': am.api_key, 'type': am.request_type}
    if limit:
        payload.update({'limit': limit})
    if input_type == 'Multiple URLs':
        urls = params.get('urls', '')
        if isinstance(urls, str):
            urls = urls.split(',')
            urls = [url.strip()for url in urls]
        payload.update({'uris': urls})
    else:
        url = params.get('url', '')
        scan_depth = params.get('scan_depth', '').lower()
        payload.update({'uri': url})
        if scan_depth:
            payload.update({'scan_depth': scan_depth})
    return payload


def get_threat_score(config, params):
    am = alphaMountain(config)
    payload = get_payload(params, am)
    input_type = params.get('input_type', '')
    endpoint = '/threat/uri' if input_type == 'Specific URL' else '/threat/uris'
    return am.make_api_call(endpoint, payload=json.dumps(payload))


def get_url_categories(config, params):
    am = alphaMountain(config)
    payload = get_payload(params, am)
    input_type = params.get('input_type', '')
    endpoint = '/category/uri' if input_type == 'Specific URL' else '/category/uris'
    return am.make_api_call(endpoint, payload=json.dumps(payload))


def identify_impersonation_detection(config, params):
    am = alphaMountain(config)
    payload = get_payload(params, am)
    return am.make_api_call('/impersonate/uri', payload=json.dumps(payload))


def get_domain_popularity(config, params):
    am = alphaMountain(config)
    domain = params.get('domain')
    payload = {'version': am.version, 'license': am.api_key, 'type': am.request_type, 'domain': domain}
    return am.make_api_call('/popularity/domain', payload=json.dumps(payload))


def _check_health(config):
    am = alphaMountain(config)
    payload = {'version': am.version, 'license': am.api_key, 'endpoint': 'category'}
    return am.make_api_call('/quota', payload=json.dumps(payload))


operations = {
    'get_threat_score': get_threat_score,
    'get_url_categories': get_url_categories,
    'identify_impersonation_detection': identify_impersonation_detection,
    'get_domain_popularity': get_domain_popularity
}
