# __author__ = "BigHead"
# creation time: 2020/8/20 14:02
from lib.models import QueryDbParents
import json
from lib import common_log
loger = common_log.get_logger(__name__)

def get_performance_data(dbinfo, key):
    performance = dbinfo.instance_performance(key).get('PerformanceKeys').get('PerformanceKey')
    return performance


def get_resource_usage(dbinfo):
    resource_usage = dbinfo.resource_usage()
    return resource_usage


def get_redis_resource_usage(dbinfo):
    resource_usage = dbinfo.redis_monitor_data()
    return resource_usage


def get_all_dbinfo(query_parameter):
    dbinfo = QueryDbParents.QueryDbInfo.set_config()
    resource_usage = get_resource_usage(dbinfo)
    r = get_performance_data(dbinfo, query_parameter)
    result = {}
    for single in r:
        title_list = single.get('ValueFormat').split('&')
        value_list = single.get('Values').get('PerformanceValue')[0].get('Value').split('&')
        for title, value in zip(title_list, value_list):
            result[title] = value
    redis_resource_usage = eval(get_redis_resource_usage(dbinfo).get('MonitorHistory'))
    if redis_resource_usage:
        result['redis_memory_usage'] = [redis_resource_usage[single].get('UsedMemory') for single in redis_resource_usage][-1]
    else:
        loger.error('获取redis内存使用情况数据为空: %s' % redis_resource_usage)
        result['redis_memory_usage'] = None
    return {**result, **resource_usage}


if __name__ == '__main__':
    import time
    s = time.time()
    rec = get_all_dbinfo('MySQL_Sessions,MySQL_InnoDBDataReadWriten,MySQL_InnoDBBufferRatio,MySQL_QPSTPS')
    j = json.dumps(rec)
    print(j)
    e = time.time()
    print(e - s)
