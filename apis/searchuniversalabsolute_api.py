import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class SearchuniversalabsoluteApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def export_search_absolute_chunked(self, query, _from, to, fields, **kwargs):
        """
        Export message search with absolute timerange.
        Search for messages using an absolute timerange, specified as from/to with format yyyy-MM-ddTHH:mm:ss.SSSZ (e.g. 2014-01-23T15:34:49.000Z) or yyyy-MM-dd HH:mm:ss.

        >>> thread = api.export_search_absolute_chunked(query, _from, to, fields, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object query: Query (Lucene syntax) (required)
        :param Object _from: Timerange start. See description for date format (required)
        :param Object to: Timerange end. See description for date format (required)
        :param Object fields: Comma separated list of fields to return (required)
        :param Object limit: Maximum number of messages to return.
        :param Object offset: Offset
        :param Object filter: Filter
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.export_search_absolute_chunked_with_http_info(query, _from, to, fields, **kwargs)
        else:
            (data) = self.export_search_absolute_chunked_with_http_info(query, _from, to, fields, **kwargs)
            return data

    def export_search_absolute_chunked_with_http_info(self, query, _from, to, fields, **kwargs):
        """
        Export message search with absolute timerange.
        Search for messages using an absolute timerange, specified as from/to with format yyyy-MM-ddTHH:mm:ss.SSSZ (e.g. 2014-01-23T15:34:49.000Z) or yyyy-MM-dd HH:mm:ss.

        >>> thread = api.export_search_absolute_chunked_with_http_info(query, _from, to, fields, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object query: Query (Lucene syntax) (required)
        :param Object _from: Timerange start. See description for date format (required)
        :param Object to: Timerange end. See description for date format (required)
        :param Object fields: Comma separated list of fields to return (required)
        :param Object limit: Maximum number of messages to return.
        :param Object offset: Offset
        :param Object filter: Filter
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['query', '_from', 'to', 'fields', 'limit', 'offset', 'filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `export_search_absolute_chunked`")
        # verify the required parameter '_from' is set
        if ('_from' not in params) or (params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `export_search_absolute_chunked`")
        # verify the required parameter 'to' is set
        if ('to' not in params) or (params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `export_search_absolute_chunked`")
        # verify the required parameter 'fields' is set
        if ('fields' not in params) or (params['fields'] is None):
            raise ValueError("Missing the required parameter `fields` when calling `export_search_absolute_chunked`")

        resource_path = '/search/universal/absolute/export'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'query' in params:
            query_params['query'] = params['query']
        if '_from' in params:
            query_params['from'] = params['_from']
        if 'to' in params:
            query_params['to'] = params['to']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'filter' in params:
            query_params['filter'] = params['filter']
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['text/csv'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def field_histogram_absolute(self, query, field, interval, _from, to, **kwargs):
        """
        Field value histogram of a query using an absolute timerange
        >>> thread = api.field_histogram_absolute(query, field, interval, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object query: Query (Lucene syntax) (required)
        :param Object field: Field of whose values to get the histogram of (required)
        :param Object interval: Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) (required)
        :param Object _from: Timerange start. See search method description for date format (required)
        :param Object to: Timerange end. See search method description for date format (required)
        :param Object filter: Filter
        :param Object cardinality: Calculate the cardinality of the field as well
        :return: HistogramResult If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.field_histogram_absolute_with_http_info(query, field, interval, _from, to, **kwargs)
        else:
            (data) = self.field_histogram_absolute_with_http_info(query, field, interval, _from, to, **kwargs)
            return data

    def field_histogram_absolute_with_http_info(self, query, field, interval, _from, to, **kwargs):
        """
        Field value histogram of a query using an absolute timerange
        >>> thread = api.field_histogram_absolute_with_http_info(query, field, interval, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object query: Query (Lucene syntax) (required)
        :param Object field: Field of whose values to get the histogram of (required)
        :param Object interval: Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) (required)
        :param Object _from: Timerange start. See search method description for date format (required)
        :param Object to: Timerange end. See search method description for date format (required)
        :param Object filter: Filter
        :param Object cardinality: Calculate the cardinality of the field as well
        :return: HistogramResult If the method is called asynchronously, returns the request thread.
        """

        all_params = ['query', 'field', 'interval', '_from', 'to', 'filter', 'cardinality']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `field_histogram_absolute`")
        # verify the required parameter 'field' is set
        if ('field' not in params) or (params['field'] is None):
            raise ValueError("Missing the required parameter `field` when calling `field_histogram_absolute`")
        # verify the required parameter 'interval' is set
        if ('interval' not in params) or (params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `field_histogram_absolute`")
        # verify the required parameter '_from' is set
        if ('_from' not in params) or (params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `field_histogram_absolute`")
        # verify the required parameter 'to' is set
        if ('to' not in params) or (params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `field_histogram_absolute`")

        resource_path = '/search/universal/absolute/fieldhistogram'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'query' in params:
            query_params['query'] = params['query']
        if 'field' in params:
            query_params['field'] = params['field']
        if 'interval' in params:
            query_params['interval'] = params['interval']
        if '_from' in params:
            query_params['from'] = params['_from']
        if 'to' in params:
            query_params['to'] = params['to']
        if 'filter' in params:
            query_params['filter'] = params['filter']
        if 'cardinality' in params:
            query_params['cardinality'] = params['cardinality']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='HistogramResult', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def histogram_absolute(self, query, interval, _from, to, **kwargs):
        """
        Datetime histogram of a query using an absolute timerange
        >>> thread = api.histogram_absolute(query, interval, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object query: Query (Lucene syntax) (required)
        :param Object interval: Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) (required)
        :param Object _from: Timerange start. See search method description for date format (required)
        :param Object to: Timerange end. See search method description for date format (required)
        :param Object filter: Filter
        :return: HistogramResult If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.histogram_absolute_with_http_info(query, interval, _from, to, **kwargs)
        else:
            (data) = self.histogram_absolute_with_http_info(query, interval, _from, to, **kwargs)
            return data

    def histogram_absolute_with_http_info(self, query, interval, _from, to, **kwargs):
        """
        Datetime histogram of a query using an absolute timerange
        >>> thread = api.histogram_absolute_with_http_info(query, interval, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object query: Query (Lucene syntax) (required)
        :param Object interval: Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) (required)
        :param Object _from: Timerange start. See search method description for date format (required)
        :param Object to: Timerange end. See search method description for date format (required)
        :param Object filter: Filter
        :return: HistogramResult If the method is called asynchronously, returns the request thread.
        """

        all_params = ['query', 'interval', '_from', 'to', 'filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `histogram_absolute`")
        # verify the required parameter 'interval' is set
        if ('interval' not in params) or (params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `histogram_absolute`")
        # verify the required parameter '_from' is set
        if ('_from' not in params) or (params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `histogram_absolute`")
        # verify the required parameter 'to' is set
        if ('to' not in params) or (params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `histogram_absolute`")

        resource_path = '/search/universal/absolute/histogram'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'query' in params:
            query_params['query'] = params['query']
        if 'interval' in params:
            query_params['interval'] = params['interval']
        if '_from' in params:
            query_params['from'] = params['_from']
        if 'to' in params:
            query_params['to'] = params['to']
        if 'filter' in params:
            query_params['filter'] = params['filter']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='HistogramResult', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def search_absolute(self, query, _from, to, **kwargs):
        """
        Message search with absolute timerange.
        Search for messages using an absolute timerange, specified as from/to with format yyyy-MM-ddTHH:mm:ss.SSSZ (e.g. 2014-01-23T15:34:49.000Z) or yyyy-MM-dd HH:mm:ss.

        >>> thread = api.search_absolute(query, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object query: Query (Lucene syntax) (required)
        :param Object _from: Timerange start. See description for date format (required)
        :param Object to: Timerange end. See description for date format (required)
        :param Object limit: Maximum number of messages to return.
        :param Object offset: Offset
        :param Object filter: Filter
        :param Object fields: Comma separated list of fields to return
        :param Object sort: Sorting (field:asc / field:desc)
        :param Object decorate: Run decorators on search result
        :return: SearchResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_absolute_with_http_info(query, _from, to, **kwargs)
        else:
            (data) = self.search_absolute_with_http_info(query, _from, to, **kwargs)
            return data

    def search_absolute_with_http_info(self, query, _from, to, **kwargs):
        """
        Message search with absolute timerange.
        Search for messages using an absolute timerange, specified as from/to with format yyyy-MM-ddTHH:mm:ss.SSSZ (e.g. 2014-01-23T15:34:49.000Z) or yyyy-MM-dd HH:mm:ss.

        >>> thread = api.search_absolute_with_http_info(query, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object query: Query (Lucene syntax) (required)
        :param Object _from: Timerange start. See description for date format (required)
        :param Object to: Timerange end. See description for date format (required)
        :param Object limit: Maximum number of messages to return.
        :param Object offset: Offset
        :param Object filter: Filter
        :param Object fields: Comma separated list of fields to return
        :param Object sort: Sorting (field:asc / field:desc)
        :param Object decorate: Run decorators on search result
        :return: SearchResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['query', '_from', 'to', 'limit', 'offset', 'filter', 'fields', 'sort', 'decorate']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_absolute`")
        # verify the required parameter '_from' is set
        if ('_from' not in params) or (params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `search_absolute`")
        # verify the required parameter 'to' is set
        if ('to' not in params) or (params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `search_absolute`")

        resource_path = '/search/universal/absolute'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'query' in params:
            query_params['query'] = params['query']
        if '_from' in params:
            query_params['from'] = params['_from']
        if 'to' in params:
            query_params['to'] = params['to']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'filter' in params:
            query_params['filter'] = params['filter']
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'decorate' in params:
            query_params['decorate'] = params['decorate']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SearchResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def stats_absolute(self, field, query, _from, to, **kwargs):
        """
        Field statistics for a query using an absolute timerange.
        Returns statistics like min/max or standard deviation of numeric fields over the whole query result set.

        >>> thread = api.stats_absolute(field, query, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object field: Message field of numeric type to return statistics for (required)
        :param Object query: Query (Lucene syntax) (required)
        :param Object _from: Timerange start. See search method description for date format (required)
        :param Object to: Timerange end. See search method description for date format (required)
        :param Object filter: Filter
        :return: FieldStatsResult If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.stats_absolute_with_http_info(field, query, _from, to, **kwargs)
        else:
            (data) = self.stats_absolute_with_http_info(field, query, _from, to, **kwargs)
            return data

    def stats_absolute_with_http_info(self, field, query, _from, to, **kwargs):
        """
        Field statistics for a query using an absolute timerange.
        Returns statistics like min/max or standard deviation of numeric fields over the whole query result set.

        >>> thread = api.stats_absolute_with_http_info(field, query, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object field: Message field of numeric type to return statistics for (required)
        :param Object query: Query (Lucene syntax) (required)
        :param Object _from: Timerange start. See search method description for date format (required)
        :param Object to: Timerange end. See search method description for date format (required)
        :param Object filter: Filter
        :return: FieldStatsResult If the method is called asynchronously, returns the request thread.
        """

        all_params = ['field', 'query', '_from', 'to', 'filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field' is set
        if ('field' not in params) or (params['field'] is None):
            raise ValueError("Missing the required parameter `field` when calling `stats_absolute`")
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `stats_absolute`")
        # verify the required parameter '_from' is set
        if ('_from' not in params) or (params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `stats_absolute`")
        # verify the required parameter 'to' is set
        if ('to' not in params) or (params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `stats_absolute`")

        resource_path = '/search/universal/absolute/stats'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'field' in params:
            query_params['field'] = params['field']
        if 'query' in params:
            query_params['query'] = params['query']
        if '_from' in params:
            query_params['from'] = params['_from']
        if 'to' in params:
            query_params['to'] = params['to']
        if 'filter' in params:
            query_params['filter'] = params['filter']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='FieldStatsResult', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def terms_absolute(self, field, query, _from, to, **kwargs):
        """
        Most common field terms of a query using an absolute timerange
        >>> thread = api.terms_absolute(field, query, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object field: Message field of to return terms of (required)
        :param Object query: Query (Lucene syntax) (required)
        :param Object _from: Timerange start. See search method description for date format (required)
        :param Object to: Timerange end. See search method description for date format (required)
        :param Object size: Maximum number of terms to return
        :param Object filter: Filter
        :return: TermsResult If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.terms_absolute_with_http_info(field, query, _from, to, **kwargs)
        else:
            (data) = self.terms_absolute_with_http_info(field, query, _from, to, **kwargs)
            return data

    def terms_absolute_with_http_info(self, field, query, _from, to, **kwargs):
        """
        Most common field terms of a query using an absolute timerange
        >>> thread = api.terms_absolute_with_http_info(field, query, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object field: Message field of to return terms of (required)
        :param Object query: Query (Lucene syntax) (required)
        :param Object _from: Timerange start. See search method description for date format (required)
        :param Object to: Timerange end. See search method description for date format (required)
        :param Object size: Maximum number of terms to return
        :param Object filter: Filter
        :return: TermsResult If the method is called asynchronously, returns the request thread.
        """

        all_params = ['field', 'query', '_from', 'to', 'size', 'filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field' is set
        if ('field' not in params) or (params['field'] is None):
            raise ValueError("Missing the required parameter `field` when calling `terms_absolute`")
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `terms_absolute`")
        # verify the required parameter '_from' is set
        if ('_from' not in params) or (params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `terms_absolute`")
        # verify the required parameter 'to' is set
        if ('to' not in params) or (params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `terms_absolute`")

        resource_path = '/search/universal/absolute/terms'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'field' in params:
            query_params['field'] = params['field']
        if 'query' in params:
            query_params['query'] = params['query']
        if 'size' in params:
            query_params['size'] = params['size']
        if '_from' in params:
            query_params['from'] = params['_from']
        if 'to' in params:
            query_params['to'] = params['to']
        if 'filter' in params:
            query_params['filter'] = params['filter']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='TermsResult', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def terms_stats_absolute(self, key_field, value_field, order, query, _from, to, **kwargs):
        """
        Ordered field terms of a query computed on another field using an absolute timerange
        >>> thread = api.terms_stats_absolute(key_field, value_field, order, query, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object key_field: Message field of to return terms of (required)
        :param Object value_field: Value field used for computation (required)
        :param Object order: What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN) (required)
        :param Object query: Query (Lucene syntax) (required)
        :param Object _from: Timerange start. See search method description for date format (required)
        :param Object to: Timerange end. See search method description for date format (required)
        :param Object size: Maximum number of terms to return
        :param Object filter: Filter
        :return: TermsStatsResult If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.terms_stats_absolute_with_http_info(key_field, value_field, order, query, _from, to, **kwargs)
        else:
            (data) = self.terms_stats_absolute_with_http_info(key_field, value_field, order, query, _from, to, **kwargs)
            return data

    def terms_stats_absolute_with_http_info(self, key_field, value_field, order, query, _from, to, **kwargs):
        """
        Ordered field terms of a query computed on another field using an absolute timerange
        >>> thread = api.terms_stats_absolute_with_http_info(key_field, value_field, order, query, _from, to, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object key_field: Message field of to return terms of (required)
        :param Object value_field: Value field used for computation (required)
        :param Object order: What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN) (required)
        :param Object query: Query (Lucene syntax) (required)
        :param Object _from: Timerange start. See search method description for date format (required)
        :param Object to: Timerange end. See search method description for date format (required)
        :param Object size: Maximum number of terms to return
        :param Object filter: Filter
        :return: TermsStatsResult If the method is called asynchronously, returns the request thread.
        """

        all_params = ['key_field', 'value_field', 'order', 'query', '_from', 'to', 'size', 'filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_field' is set
        if ('key_field' not in params) or (params['key_field'] is None):
            raise ValueError("Missing the required parameter `key_field` when calling `terms_stats_absolute`")
        # verify the required parameter 'value_field' is set
        if ('value_field' not in params) or (params['value_field'] is None):
            raise ValueError("Missing the required parameter `value_field` when calling `terms_stats_absolute`")
        # verify the required parameter 'order' is set
        if ('order' not in params) or (params['order'] is None):
            raise ValueError("Missing the required parameter `order` when calling `terms_stats_absolute`")
        # verify the required parameter 'query' is set
        if ('query' not in params) or (params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `terms_stats_absolute`")
        # verify the required parameter '_from' is set
        if ('_from' not in params) or (params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `terms_stats_absolute`")
        # verify the required parameter 'to' is set
        if ('to' not in params) or (params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `terms_stats_absolute`")

        resource_path = '/search/universal/absolute/termsstats'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'key_field' in params:
            query_params['key_field'] = params['key_field']
        if 'value_field' in params:
            query_params['value_field'] = params['value_field']
        if 'order' in params:
            query_params['order'] = params['order']
        if 'query' in params:
            query_params['query'] = params['query']
        if 'size' in params:
            query_params['size'] = params['size']
        if '_from' in params:
            query_params['from'] = params['_from']
        if 'to' in params:
            query_params['to'] = params['to']
        if 'filter' in params:
            query_params['filter'] = params['filter']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='TermsStatsResult', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
