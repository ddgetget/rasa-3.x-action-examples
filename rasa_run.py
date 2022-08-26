#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-26 17:23
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    rasa_run.py
# @Project: rasa-3.x-action-examples
# @Package:
# @Ref:


import rasa

rasa.run(
    model="models",
    endpoints="config/endpoints.yml",
    credentials="config/credentials.yml"
)
