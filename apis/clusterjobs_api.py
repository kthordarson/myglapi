import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class ClusterjobsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def cancel_job(self, job_id, **kwargs):
        """
        Cancel job with the given ID


        >>> thread = api.cancel_job(job_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object job_id:  (required)
        :return:\s SystemJobSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cancel_job_with_http_info(job_id, **kwargs)
        else:
            (data) = self.cancel_job_with_http_info(job_id, **kwargs)
            return data

    def cancel_job_with_http_info(self, job_id, **kwargs):
        """
        Cancel job with the given ID


        >>> thread = api.cancel_job_with_http_info(job_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object job_id:  (required)
        :return:\s SystemJobSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `cancel_job`")

        resource_path = '/cluster/jobs/{jobId}'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SystemJobSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_job(self, job_id, **kwargs):
        """
        Get job with the given ID


        >>> thread = api.get_job(job_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object job_id:  (required)
        :return:\s SystemJobSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_job_with_http_info(job_id, **kwargs)
        else:
            (data) = self.get_job_with_http_info(job_id, **kwargs)
            return data

    def get_job_with_http_info(self, job_id, **kwargs):
        """
        Get job with the given ID


        >>> thread = api.get_job_with_http_info(job_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object job_id:  (required)
        :return:\s SystemJobSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_job`")

        resource_path = '/cluster/jobs/{jobId}'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SystemJobSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list(self, **kwargs):
        """
        List currently running jobs


        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        List currently running jobs


        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Map If the method is called asynchronously, returns the request thread.
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

        resource_path = '/cluster/jobs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Map', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
