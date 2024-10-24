import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger



class SystemmetricsApi(object):
	def __init__(self, api_client=None):
		config = Configuration()
		if api_client:
			self.api_client = api_client
		else:
			if not config.api_client:
				config.api_client = ApiClient()
			self.api_client = config.api_client

	def by_namespace(self, namespace, **kwargs):
		"""
		Get all metrics of a namespace
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please define a `callback` function
		to be invoked when receiving the response.
		>>> thread = api.by_namespace(namespace, callback=callback_function)

		:param callback function: The callback function
			for asynchronous request. (optional)
		:param Object namespace:  (required)
		:return: MetricsSummaryResponse If the method is called asynchronously, returns the request thread.
		"""
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.by_namespace_with_http_info(namespace, **kwargs)
		else:
			(data) = self.by_namespace_with_http_info(namespace, **kwargs)
			return data

	def by_namespace_with_http_info(self, namespace, **kwargs):
		"""
		Get all metrics of a namespace
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please define a `callback` function
		to be invoked when receiving the response.
		>>> thread = api.by_namespace_with_http_info(namespace, callback=callback_function)

		:param callback function: The callback function
			for asynchronous request. (optional)
		:param Object namespace:  (required)
		:return: MetricsSummaryResponse If the method is called asynchronously, returns the request thread.
		"""

		all_params = ['namespace']
		all_params.append('callback')
		all_params.append('_return_http_data_only')

		params = locals()
		for key in params['kwargs']:
			val = params['kwargs'][key]
			if key not in all_params:
				raise TypeError(f"Got an unexpected keyword argument {key}")
			params[key] = val
		del params['kwargs']
		# verify the required parameter 'namespace' is set
		if ('namespace' not in params) or (params['namespace'] is None):
			raise ValueError("Missing the required parameter `namespace` when calling `by_namespace`")

		resource_path = '/system/metrics/namespace/{namespace}'.replace('{format}', 'json')
		path_params = {}
		if 'namespace' in params:
			path_params['namespace'] = params['namespace']

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

		return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='MetricsSummaryResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

	def metric_names(self, **kwargs):
		"""
		Get all metrics keys/names
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please define a `callback` function
		to be invoked when receiving the response.
		>>> thread = api.metric_names(callback=callback_function)

		:param callback function: The callback function
			for asynchronous request. (optional)
		:return: MetricNamesResponse If the method is called asynchronously, returns the request thread.
		"""
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.metric_names_with_http_info(**kwargs)
		else:
			(data) = self.metric_names_with_http_info(**kwargs)
			return data

	def metric_names_with_http_info(self, **kwargs):
		"""
		Get all metrics keys/names


		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please define a `callback` function
		to be invoked when receiving the response.
		>>> thread = api.metric_names_with_http_info(callback=callback_function)

		:param callback function: The callback function
			for asynchronous request. (optional)
		:return: MetricNamesResponse If the method is called asynchronously, returns the request thread.
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

		resource_path = '/system/metrics/names'.replace('{format}', 'json')
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

		return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='MetricNamesResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

	def metrics(self, **kwargs):
		"""
		Get all metrics
		Note that this might return a huge result set.

		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please define a `callback` function
		to be invoked when receiving the response.
		>>> thread = api.metrics(callback=callback_function)

		:param callback function: The callback function
			for asynchronous request. (optional)
		:return: MetricRegistry If the method is called asynchronously, returns the request thread.
		"""
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.metrics_with_http_info(**kwargs)
		else:
			(data) = self.metrics_with_http_info(**kwargs)
			return data

	def metrics_with_http_info(self, **kwargs):
		"""
		Get all metrics
		Note that this might return a huge result set.

		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please define a `callback` function
		to be invoked when receiving the response.
		>>> thread = api.metrics_with_http_info(callback=callback_function)

		:param callback function: The callback function
			for asynchronous request. (optional)
		:return: MetricRegistry If the method is called asynchronously, returns the request thread.
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

		resource_path = '/system/metrics'.replace('{format}', 'json')
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

		return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='MetricRegistry', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

	def multiple_metrics(self, requested_metrics, **kwargs):
		"""
		Get the values of multiple metrics at once
		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please define a `callback` function
		to be invoked when receiving the response.
		>>> thread = api.multiple_metrics(requested_metrics, callback=callback_function)

		:param callback function: The callback function
			for asynchronous request. (optional)
		:param MetricsReadRequest requested_metrics:  (required)
		:return: MetricsSummaryResponse If the method is called asynchronously, returns the request thread.
		"""
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.multiple_metrics_with_http_info(requested_metrics, **kwargs)
		else:
			(data) = self.multiple_metrics_with_http_info(requested_metrics, **kwargs)
			return data

	def multiple_metrics_with_http_info(self, requested_metrics, **kwargs):
		"""
		Get the values of multiple metrics at once


		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please define a `callback` function
		to be invoked when receiving the response.
		>>> thread = api.multiple_metrics_with_http_info(requested_metrics, callback=callback_function)

		:param callback function: The callback function
			for asynchronous request. (optional)
		:param MetricsReadRequest requested_metrics:  (required)
		:return: MetricsSummaryResponse If the method is called asynchronously, returns the request thread.
		"""

		all_params = ['requested_metrics']
		all_params.append('callback')
		all_params.append('_return_http_data_only')

		params = locals()
		for key in params['kwargs']:
			val = params['kwargs'][key]
			if key not in all_params:
				raise TypeError(f"Got an unexpected keyword argument {key}")
			params[key] = val
		del params['kwargs']
		# verify the required parameter 'requested_metrics' is set
		if ('requested_metrics' not in params) or (params['requested_metrics'] is None):
			raise ValueError("Missing the required parameter `requested_metrics` when calling `multiple_metrics`")

		resource_path = '/system/metrics/multiple'.replace('{format}', 'json')
		path_params = {}

		query_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'requested_metrics' in params:
			body_params = params['requested_metrics']

		# HTTP header `Accept`
		header_params['Accept'] = self.api_client.select_header_accept([])
		if not header_params['Accept']:
			del header_params['Accept']

		# HTTP header `Content-Type`
		header_params['Content-Type'] = self.api_client.select_header_content_type([])

		# Authentication setting
		auth_settings = []

		return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='MetricsSummaryResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

	def single_metric(self, metric_name, **kwargs):
		"""
		Get a single metric


		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please define a `callback` function
		to be invoked when receiving the response.
		>>> thread = api.single_metric(metric_name, callback=callback_function)

		:param callback function: The callback function
			for asynchronous request. (optional)
		:param Object metric_name:  (required)
		:return: Metric If the method is called asynchronously, returns the request thread.
		"""
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.single_metric_with_http_info(metric_name, **kwargs)
		else:
			(data) = self.single_metric_with_http_info(metric_name, **kwargs)
			return data

	def single_metric_with_http_info(self, metric_name, **kwargs):
		"""
		Get a single metric


		This method makes a synchronous HTTP request by default. To make an
		asynchronous HTTP request, please define a `callback` function
		to be invoked when receiving the response.
		>>> thread = api.single_metric_with_http_info(metric_name, callback=callback_function)

		:param callback function: The callback function
			for asynchronous request. (optional)
		:param Object metric_name:  (required)
		:return: Metric If the method is called asynchronously, returns the request thread.
		"""

		all_params = ['metric_name']
		all_params.append('callback')
		all_params.append('_return_http_data_only')

		params = locals()
		for key in params['kwargs']:
			val = params['kwargs'][key]
			if key not in all_params:
				raise TypeError(f"Got an unexpected keyword argument {key}")
			params[key] = val
		del params['kwargs']
		# verify the required parameter 'metric_name' is set
		if ('metric_name' not in params) or (params['metric_name'] is None):
			raise ValueError("Missing the required parameter `metric_name` when calling `single_metric`")

		resource_path = '/system/metrics/{metricName}'.replace('{format}', 'json')
		path_params = {}
		if 'metric_name' in params:
			path_params['metricName'] = params['metric_name']

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

		return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Metric', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
