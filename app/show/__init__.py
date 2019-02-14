# -*- coding:utf-8 -*-

from flask import Blueprint


show = Blueprint('show', __name__, static_folder='static')

# 在末尾导入相关模块，是为了避免循环导入依赖，因为在下面的模块中还要导入蓝本main
from . import views, forms
