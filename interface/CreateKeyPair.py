# -*- coding: utf-8 -*-
# @Author: BigHead

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.CreateKeyPairRequest import CreateKeyPairRequest



def createkeypair(settings, ResourceGroupId):
    client = AcsClient(settings.accessKeyId, settings.accessSecret, settings.zone)

    request = CreateKeyPairRequest()
    request.set_accept_format('json')

    request.set_KeyPairName("aliyun")
    request.set_Tags([
      {
        "Key": "kuaiban",
        "Value": "kuaiban1234"
      }
    ])
    request.set_ResourceGroupId(ResourceGroupId)

    response = client.do_action_with_exception(request).decode('utf-8')
    # python2:  print(response)
    return response