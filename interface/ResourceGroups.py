# -*- coding: utf-8 -*-
# @Author: BigHead

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkresourcemanager.request.v20200331.ListResourceGroupsRequest import ListResourceGroupsRequest


def get_resourcegroups(config):
    client = AcsClient(config.accessKeyId, config.accessSecret, config.zone)

    request = ListResourceGroupsRequest()
    request.set_accept_format('json')

    response = client.do_action_with_exception(request).decode('utf-8')
    # python2:  print(response)
    # print(str(response, encoding='utf-8'))
    return response