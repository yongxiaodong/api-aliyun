# -*- coding: utf-8 -*-
# @Author: BigHead

from lib import common_log
from conf import settings
from interface import xxx_interface

logger = common_log.get_logger(__name__)


def run(query_parameter):
    from flask import Flask, request, render_template
    app = Flask(__name__,  template_folder='%s/templates' % settings.BASE_DIR)

    @app.route('/metrics', methods=['GET', 'POST'])
    def home():
        receive_data = xxx_interface.get_all_dbinfo(query_parameter)
        return render_template('index.html', data=receive_data), {'Content-Type': 'text/plain'}
    app.run(host='0.0.0.0', port='9101')
