#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-24 22:10
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    actions.py
# @Project: rasa-3.x-action-examples
# @Package:
# @Ref:

from typing import Any, Text, Dict, List

# Action：为响应对话状态而采取的下一个动作。
# Tracker：保持对话的状态。
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCustomFallback(Action):

    def name(self) -> Text:
        return "action_custom_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # 排除意图为nlu_fallback
        intents = [i for i in tracker.current_state()['latest_message']['intent_ranking'] if i['name'] != 'nlu_fallback']
        # 允许的意图
        allowed_intents = ["new_order", "what_happened", "inform"]
        # 意图对应的问题
        message = {
            "new_order": "Do you want to place a new order?",
            "what_happened": "Do you want to ask about a previous order?",
            "inform": "Would you like more information about stroopwafels?"
        }
        # 跌去前3个意图，且意图在允许意图里面的，获取意图，以及意图对应的固定答语
        # buttons=[{'payload': 'new_order', 'title': 'Do you want to place a new order?'},
        # {'payload': 'what_happened', 'title': 'Do you want to ask about a previous order?'},
        # {'payload': 'inform', 'title': 'Would you like more information about stroopwafels?'}]
        buttons = [{'payload': i['name'], 'title': message[i['name']]} for i in intents[:3] if i['name'] in allowed_intents]
        # 将文本发送到输出通道。
        dispatcher.utter_message(
            text="It wasn't 100% clear what you meant. Could you speficy/rephrase?",
            buttons=buttons
        )
        return []
