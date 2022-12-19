from loguru import logger
from apis.apidocs_api import ApiClient
from apis.systeminputs_api import SysteminputsApi
s=SysteminputsApi()
print(s.list())
a=ApiClient()
print(a)
