import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class PluginsorggraylogpluginspipelineprocessorsystempipelinessimulateApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def simulate(self, simulation, **kwargs):
        """
        Simulate the execution of the pipeline message processor


        >>> thread = api.simulate(simulation, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param SimulationRequest simulation:  (required)
        :return: SimulationResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.simulate_with_http_info(simulation, **kwargs)
        else:
            (data) = self.simulate_with_http_info(simulation, **kwargs)
            return data

    def simulate_with_http_info(self, simulation, **kwargs):
        """
        Simulate the execution of the pipeline message processor


        >>> thread = api.simulate_with_http_info(simulation, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param SimulationRequest simulation:  (required)
        :return: SimulationResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['simulation']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'simulation' is set
        if ('simulation' not in params) or (params['simulation'] is None):
            raise ValueError("Missing the required parameter `simulation` when calling `simulate`")

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/simulate'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'simulation' in params:
            body_params = params['simulation']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SimulationResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
