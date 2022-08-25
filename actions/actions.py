#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-25 22:24
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    actions.py
# @Project: rasa-3.x-action-examples
# @Package:
# @Ref:

import json
from lunr.index import Index

from clumper import Clumper
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Read in the recipes with all the data.
recipes = Clumper.read_jsonl("static/recipes.jsonl").collect()

class ActionSuggestRecipe(Action):

    def name(self) -> Text:
        return "action_suggest_recipe"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        db = {d['uid']: d for d in recipes}
        # Read in the index for fast querying.
        with open("static/index.json", "r") as f:
            idx = Index.load(json.loads(f.read()))
        
        # Attempt to find matching documents.
        matches = idx.search(tracker.latest_message['text'])

        # We may have no matches, respond appropriately.
        if len(matches) == 0:
            dispatcher.utter_message(text="Sorry, I couldn't find any recipes.")
            return []
        # We've found matches here, so we list the top 5.
        dispatcher.utter_message(text="These recipes might be interesting.")
        for match in matches[:5]:
            item = db[match['ref']]
            dispatcher.utter_message(f" - {item['name']}")
        return []
