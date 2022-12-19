from loguru import logger
from apis.apidocs_api import ApiClient
from apis.systeminputs_api import SysteminputsApi
s=SysteminputsApi()
slist = s.list()
print(slist)
a=ApiClient()
print(a)
