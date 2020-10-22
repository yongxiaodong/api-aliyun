# -*- coding: utf-8 -*-
# @Author: BigHead


from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest


def DescribeInstances(settings):
    client = AcsClient(settings.accessKeyId, settings.accessSecret, settings.zone)

    request = DescribeInstancesRequest()
    request.set_accept_format('json')

    response = client.do_action_with_exception(request).decode('utf-8')
    return response
