import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
class SystemprocessingApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def pause_processing(self, **kwargs):
        """
        Pauses message processing
        If the message journal is enabled, incoming messages will be spooled on disk, if it is disabled, you might lose messages from inputs which cannot buffer themselves, like AMQP or Kafka-based inputs.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pause_processing(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.pause_processing_with_http_info(**kwargs)
        else:
            (data) = self.pause_processing_with_http_info(**kwargs)
            return data

    def pause_processing_with_http_info(self, **kwargs):
        """
        Pauses message processing
        If the message journal is enabled, incoming messages will be spooled on disk, if it is disabled, you might lose messages from inputs which cannot buffer themselves, like AMQP or Kafka-based inputs.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pause_processing_with_http_info(callback=callback_function)

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
                    " to method pause_processing" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/system/processing/pause'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def resume_processing(self, **kwargs):
        """
        Resume message processing
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.resume_processing(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.resume_processing_with_http_info(**kwargs)
        else:
            (data) = self.resume_processing_with_http_info(**kwargs)
            return data

    def resume_processing_with_http_info(self, **kwargs):
        """
        Resume message processing
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.resume_processing_with_http_info(callback=callback_function)

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
                    " to method resume_processing" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/system/processing/resume'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
