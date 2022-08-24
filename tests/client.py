#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-24 22:10
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    client.py
# @Project: rasa-3.x-action-examples
# @Package:
# @Ref:

from typing import Any, Text, Dict, List
import uuid
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class Client:
    def __init__(self, action):
        self.action = action

    def invoke_message(self, message, slots=None):
        if not slots:
            slots = {}

        dispatcher = CollectingDispatcher()  # 将消息发送回用户
        # 保持对话的状态。
        # active_form={}
        # active_loop={}
        # events=[]
        # followup_action
        # latest_action_name
        # latest_message=Message()
        # sender_id='25f86d17-6c4f-4f5c-bda9-077b424474ea'
        # slots={}
        tracker = Tracker(
            sender_id=str(uuid.uuid4()),
            slots=slots,
            latest_message=message,
            events=[],
            paused=False,
            followup_action=None,
            active_loop={},
            latest_action_name=None
        )

        domain = {}

        slots = self.action.run(dispatcher=dispatcher, tracker=tracker, domain=domain)
        return dispatcher.messages[0], slots