#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-24 22:10
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    test_fallback_action.py
# @Project: rasa-3.x-action-examples
# @Package:
# @Ref:

from .client import Client
from actions.actions import ActionCustomFallback

# 模拟一条抽取的数据
message = {
    'entities': [],
    'intent': {'confidence': 0.4, 'name': 'inform'},
    'intent_ranking': [
        {'confidence': 0.3, 'name': 'new_order'},
        {'confidence': 0.3, 'name': 'what_happened'},
        {'confidence': 0.4, 'name': 'inform'}],
    'text': 'stroop stroop stroopwafels!!!!'
}


def test_base_usecase():
    action = ActionCustomFallback()

    client = Client(action=action)
    # 获取客户端的提示语（含按钮，当前项目设置最大是3个），以及词槽
    msg_back, slots = client.invoke_message(message=message)
    print(msg_back)
    # {'text': "It wasn't 100% clear what you meant. Could you speficy/rephrase?",
    # 'buttons': [{'payload': 'new_order', 'title': 'Do you want to place a new order?'},
    # {'payload': 'what_happened', 'title': 'Do you want to ask about a previous order?'},
    # {'payload': 'inform', 'title': 'Would you like more information about stroopwafels?'}],
    # 'elements': [], 'custom': {}, 'template': None, 'response': None, 'image': None,
    # 'attachment': None}

    assert "Could you speficy/rephrase?" in msg_back["text"]
    assert len(msg_back['buttons']) == 3
