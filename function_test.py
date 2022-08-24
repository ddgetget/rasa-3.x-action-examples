#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-25 07:16
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    function_test.py
# @Project: rasa-3.x-action-examples
# @Package: 
# @Ref:

from jina import DocumentArray, Executor, Flow, requests


class MyExec(Executor):
    @requests
    async def add_text(self, docs: DocumentArray, **kwargs):
        for d in docs:
            d.text += 'hello, world!'




if __name__ == '__main__':
    f = Flow().add(uses=MyExec).add(uses=MyExec)

    with f:
        r = f.post('/', DocumentArray.empty(2))
        # print(r.texts)
        print(r)
