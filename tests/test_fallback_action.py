#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-26 16:51
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    test_fallback_action.py
# @Project: rasa-3.x-action-examples
# @Package: 
# @Ref:
from actions.actions import ActionHelloWorld

# 模拟一条抽取的数据
from tests.client import Client

message = {
    'entities': [],
    'intent': {'confidence': 0.4, 'name': 'inform'},
    'intent_ranking': [
        {'confidence': 0.3, 'name': 'greet'},
        {'confidence': 0.3, 'name': 'bot_challenge'},
        {'confidence': 0.4, 'name': 'give_time'}],
    'text': 'can you tell me what time it is'
}


def test_base_usecase():
    action = ActionHelloWorld()

    client = Client(action=action)
    # 获取客户端的提示语（含按钮，当前项目设置最大是3个），以及词槽
    msg_back, slots = client.invoke_message(message=message)
    print(msg_back)
    # {'text': '2022-08-26 16:57:17.995311', 'buttons': [], 'elements': [], 'custom': {}, 'template': None, 'response': None, 'image': None, 'attachment': None}

