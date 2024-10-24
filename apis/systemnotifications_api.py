import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class SystemnotificationsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_notification(self, notification_type, **kwargs):
        """
        Delete a notification


        >>> thread = api.delete_notification(notification_type, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object notification_type:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_notification_with_http_info(notification_type, **kwargs)
        else:
            (data) = self.delete_notification_with_http_info(notification_type, **kwargs)
            return data

    def delete_notification_with_http_info(self, notification_type, **kwargs):
        """
        Delete a notification


        >>> thread = api.delete_notification_with_http_info(notification_type, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object notification_type:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['notification_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notification_type' is set
        if ('notification_type' not in params) or (params['notification_type'] is None):
            raise ValueError("Missing the required parameter `notification_type` when calling `delete_notification`")

        resource_path = '/system/notifications/{notificationType}'.replace('{format}', 'json')
        path_params = {}
        if 'notification_type' in params:
            path_params['notificationType'] = params['notification_type']

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

        return self.api_client.call_api(resource_path, 'DELETE', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list_notifications(self, **kwargs):
        """
        Get all active notifications


        >>> thread = api.list_notifications(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_notifications_with_http_info(**kwargs)
        else:
            (data) = self.list_notifications_with_http_info(**kwargs)
            return data

    def list_notifications_with_http_info(self, **kwargs):
        """
        Get all active notifications


        >>> thread = api.list_notifications_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: Map If the method is called asynchronously, returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']

        resource_path = '/system/notifications'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Map', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
