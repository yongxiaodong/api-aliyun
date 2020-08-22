# __author__ = "BigHead"
# creation time: 2020/8/20 14:25
import datetime
import pytz
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkrds.request.v20140815.DescribeResourceUsageRequest import DescribeResourceUsageRequest
from aliyunsdkrds.request.v20140815.DescribeDBInstancePerformanceRequest import DescribeDBInstancePerformanceRequest

from aliyunsdkr_kvstore.request.v20150101.DescribeHistoryMonitorValuesRequest import DescribeHistoryMonitorValuesRequest
from aliyunsdkr_kvstore.request.v20150101.DescribeMonitorItemsRequest import DescribeMonitorItemsRequest


class QueryDbInfo(object):
    def __init__(self, keyid, secret, zone, dbid, redisid):
        self.dbid = dbid
        self.redisid = redisid
        self.client = AcsClient(keyid, secret, zone)
        self.utc_tz = pytz.timezone('UTC')
        self.request = None
        self.starttime = None
        self.endtime = None

    # 获取前一分钟和现在的UTC 时间
    def get_start_end_time(self):
        self.starttime = (datetime.datetime.now(tz=self.utc_tz) - datetime.timedelta(minutes=1)).strftime(
            "%Y-%m-%dT%H:%MZ")
        self.endtime = (datetime.datetime.now(tz=self.utc_tz) - datetime.timedelta(minutes=0)).strftime(
            "%Y-%m-%dT%H:%MZ")

    # 获取rds的资源使用率
    def resource_usage(self):
        self.request = DescribeResourceUsageRequest()
        self.request.set_accept_format('json')
        self.request.set_DBInstanceId(self.dbid)
        response = self.client.do_action_with_exception(self.request)
        return eval(response.decode('utf-8'))

    # 获取rds实例的性能情况
    def instance_performance(self, key):
        self.request = DescribeDBInstancePerformanceRequest()
        self.request.set_DBInstanceId(self.dbid)
        self.request.set_Key(key)
        self.get_start_end_time()
        self.request.set_StartTime(self.starttime)
        self.request.set_EndTime(self.endtime)
        response = self.client.do_action_with_exception(self.request)
        return eval(response.decode('utf-8'))

    def redis_monitor_data(self):
        self.request = DescribeHistoryMonitorValuesRequest()
        # 此处重写self时间, 因为redis 接口时间格式为"%Y-%m-%dT%H:%M:%SZ",比rds的时间多了一个秒位
        self.starttime = (datetime.datetime.now(tz=self.utc_tz) - datetime.timedelta(minutes=10)).strftime(
            "%Y-%m-%dT%H:%M:%SZ")
        self.endtime = (datetime.datetime.now(tz=self.utc_tz) - datetime.timedelta(minutes=0)).strftime(
            "%Y-%m-%dT%H:%M:%SZ")
        self.request.set_IntervalForHistory("01m")
        self.request.set_InstanceId(self.redisid)
        self.request.set_StartTime(self.starttime)
        self.request.set_EndTime(self.endtime)
        # self.request.set_MonitorKeys("fs_total_write_io")
        response = self.client.do_action_with_exception(self.request)
        return eval(response.decode('utf-8'))

    def query_redis_monitor_items(self):
        self.request = DescribeMonitorItemsRequest()
        response = self.client.do_action_with_exception(self.request)
        return eval(response.decode('utf-8'))

    @classmethod
    def set_config(cls):
        from conf import settings
        keyid = settings.accessKeyId
        secret = settings.accessSecret
        zone = settings.zone
        dbid = settings.rds1
        redisid = settings.REDIS_ID
        return cls(keyid, secret, zone, dbid, redisid)


if __name__ == '__main__':
    test = QueryDbInfo.set_config()
    resource_usage = test.redis_monitor_data()
    # resource_usage = test.query_redis_monitor_items()
    redis_resource_usage = eval(resource_usage.get('MonitorHistory'))
    mem_usage = [redis_resource_usage[single].get('UsedMemory') for single in redis_resource_usage][
        -1]
    print(mem_usage)
    # j = json.dumps(resource_usage)
    # print(j)
    # performance = test.instance_performance('MySQL_QPSTPS')
    # print(performance)
