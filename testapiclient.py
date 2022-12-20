from loguru import logger
from apis.apidocs_api import ApiClient
from apis.systeminputs_api import SysteminputsApi
from apis.searchuniversalrelative_api import SearchuniversalrelativeApi
from apis.streams_api import StreamsApi

def sysinputs():
	s=SysteminputsApi()
	slist = s.list()
	print(slist)

def apiclnt():
	a=ApiClient()
	print(a)

def search(q, range):
	search = SearchuniversalrelativeApi()
	# q='RemoteMGNT'
	# range=(86400)
	res = search.search_relative(q, range)
	logger.info(f'[s] searchres: {res.total_results}')
	return res

if __name__ == '__main__':
	streams = StreamsApi()
	sres = search('RemoteMGNT', 86400)
	print(sres)
