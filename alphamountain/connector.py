"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector, get_logger, ConnectorError

from .operations import _check_health, operations

logger = get_logger('alphamountain')


class alphaMountainConnector(Connector):
    def execute(self, config, operation, params, **kwargs):
        try:
            action = operations.get(operation)
            result = action(config, params)
            return result
        except Exception as err:
            logger.error(str(err))
            raise ConnectorError(str(err))

    def check_health(self, config):
        return _check_health(config)
