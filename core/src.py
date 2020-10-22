# -*- coding: utf-8 -*-
# @Author: BigHead

from lib import common_log
from conf import settings
from interface import *

logger = common_log.get_logger(__name__)


def run(query_parameter):
    from flask import Flask, request, render_template
    app = Flask(__name__,  template_folder='%s/templates' % settings.BASE_DIR)

    @app.route('/metrics', methods=['GET', 'POST'])
    def home():
        receive_data = xxx_interface.get_all_dbinfo(query_parameter)
        return render_template('index.html', data=receive_data), {'Content-Type': 'text/plain'}
    app.run(host='0.0.0.0', port='9101')


def getresourcegroups(settings):
    resourcegroups = ResourceGroups.get_resourcegroups(settings)
    logger.info(resourcegroups)


def createkeypair(settings):
    groupid = 'rg-acfm375ov5t45hy'
    r = CreateKeyPair.createkeypair(settings, groupid)
    logger.info(r)


def attachkeypair(settings, instanceid):
    keypairmame = 'aliyun'
    # instanceid = 'i-2vc2rnqadinkdnblncru'
    r = AttachKeyPair.AttachKeyPair(settings, keypairmame, instanceid)
    logger.info(r)


def rebootinstance(settings, instanceid):
    r = RebootInstances.RebootInstances(settings, instanceid)
    logger.info(r)

def detachkeypair(settings, instanceid):
    keypairmame = 'aliyun'
    r = DetachKeyPair.DetachKeyPair(settings, keypairmame, instanceid)
    logger.info(r)

def describeinstances(settings):
    r = DescribeInstances.DescribeInstances(settings)
    logger.info(r)