import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class DashboardsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create(self, json_body, **kwargs):
        """
        Create a dashboard
        >>> thread = api.create(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param CreateDashboardRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(json_body, **kwargs)
        else:
            (data) = self.create_with_http_info(json_body, **kwargs)
            return data

    def create_with_http_info(self, json_body, **kwargs):
        """
        Create a dashboard
        >>> thread = api.create_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param CreateDashboardRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key} to method create")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `create`")

        resource_path = '/dashboards'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'json_body' in params:
            body_params = params['json_body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def delete(self, dashboard_id, **kwargs):
        """
        Delete a dashboard and all its widgets


        >>> thread = api.delete(dashboard_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object dashboard_id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(dashboard_id, **kwargs)
        else:
            (data) = self.delete_with_http_info(dashboard_id, **kwargs)
            return data

    def delete_with_http_info(self, dashboard_id, **kwargs):
        """
        Delete a dashboard and all its widgets


        >>> thread = api.delete_with_http_info(dashboard_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object dashboard_id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['dashboard_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `delete`")

        resource_path = '/dashboards/{dashboardId}'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboardId'] = params['dashboard_id']

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

    def get(self, dashboard_id, **kwargs):
        """
        Get a single dashboards and all configurations of its widgets
        >>> thread = api.get(dashboard_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object dashboard_id:  (required)
        :return: Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(dashboard_id, **kwargs)
        else:
            (data) = self.get_with_http_info(dashboard_id, **kwargs)
            return data

    def get_with_http_info(self, dashboard_id, **kwargs):
        """
        Get a single dashboards and all configurations of its widgets
        >>> thread = api.get_with_http_info(dashboard_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object dashboard_id:  (required)
        :return: Map If the method is called asynchronously, returns the request thread.
        """

        all_params = ['dashboard_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `get`")

        resource_path = '/dashboards/{dashboardId}'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboardId'] = params['dashboard_id']

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

    def list(self, **kwargs):
        """
        Get a list of all dashboards and all configurations of their widgets
        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: DashboardList If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        Get a list of all dashboards and all configurations of their widgets
        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: DashboardList If the method is called asynchronously, returns the request thread.
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

        resource_path = '/dashboards'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='DashboardList', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def set_positions(self, dashboard_id, json_body, **kwargs):
        """
        Update/set the positions of dashboard widgets
        >>> thread = api.set_positions(dashboard_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object dashboard_id:  (required)
        :param WidgetPositionsRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_positions_with_http_info(dashboard_id, json_body, **kwargs)
        else:
            (data) = self.set_positions_with_http_info(dashboard_id, json_body, **kwargs)
            return data

    def set_positions_with_http_info(self, dashboard_id, json_body, **kwargs):
        """
        Update/set the positions of dashboard widgets
        >>> thread = api.set_positions_with_http_info(dashboard_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object dashboard_id:  (required)
        :param WidgetPositionsRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['dashboard_id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `set_positions`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `set_positions`")

        resource_path = '/dashboards/{dashboardId}/positions'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboardId'] = params['dashboard_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'json_body' in params:
            body_params = params['json_body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        res = None
        try:
            res = self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
        except Exception as e:
            logger.error(f'[err] {type(e)} {e}')
        return res # self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))


    def update(self, dashboard_id, json_body, **kwargs):
        """
        Update the settings of a dashboard
        >>> thread = api.update(dashboard_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object dashboard_id:  (required)
        :param UpdateDashboardRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(dashboard_id, json_body, **kwargs)
        else:
            (data) = self.update_with_http_info(dashboard_id, json_body, **kwargs)
            return data

    def update_with_http_info(self, dashboard_id, json_body, **kwargs):
        """
        Update the settings of a dashboard
        >>> thread = api.update_with_http_info(dashboard_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object dashboard_id:  (required)
        :param UpdateDashboardRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['dashboard_id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `update`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `update`")

        resource_path = '/dashboards/{dashboardId}'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboardId'] = params['dashboard_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'json_body' in params:
            body_params = params['json_body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        res = None
        try:
            res = self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
        except Exception as e:
            logger.error(f'[err] {type(e)} {e}')
        return res # self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

