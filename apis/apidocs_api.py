from loguru import logger
import sys
import os
import re
sys.path.append('/home/kth/development2/graylogstuff/myglapi')
from configuration import Configuration
from api_client import ApiClient
class ApidocsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def overview(self, **kwargs):
        """
        Get API documentation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.overview(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.overview_with_http_info(**kwargs)
        else:
            (data) = self.overview_with_http_info(**kwargs)
            return data

    def overview_with_http_info(self, **kwargs):
        """
        Get API documentation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.overview_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously, returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method overview" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/api-docs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def route(self, route, **kwargs):
        """
        Get detailed API documentation of a single resource
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.route(route, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Object route: Route to fetch. For example /system (required)
        :return: None
                 If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.route_with_http_info(route, **kwargs)
        else:
            (data) = self.route_with_http_info(route, **kwargs)
            return data

    def route_with_http_info(self, route, **kwargs):
        """
        Get detailed API documentation of a single resource
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.route_with_http_info(route, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Object route: Route to fetch. For example /system (required)
        :return: None
                 If the method is called asynchronously, returns the request thread.
        """

        all_params = ['route']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method route" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'route' is set
        if ('route' not in params) or (params['route'] is None):
            raise ValueError("Missing the required parameter `route` when calling `route`")

        resource_path = '/api-docs/{route: .+}'.replace('{format}', 'json')
        path_params = {}
        if 'route' in params:
            path_params['route'] = params['route']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
