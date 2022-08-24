#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-25 06:56
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    prepare.py
# @Project: rasa-3.x-action-examples
# @Package:
# @Ref:

import typer
# 该对象将方法添加到字典列表中更好地探索。
"""
from clumper import Clumper

list_dicts = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]

c = Clumper(list_dicts)
assert len(c) == 4
"""
from clumper import Clumper
# Jina 是一个框架，它使任何人都可以在云上构建跨模式和多模式应用程序。它将 PoC 提升为生产就绪服务。 Jina 处理基础设施的复杂性，
# 使每个开发人员都可以使用高级解决方案工程和云原生技术。
# `Document` 是 Jina 中的**原始数据类型**之一。
# `DocumentArray` 是 :class:`Document` 的可变序列。
# Flow 是 Jina 精简和分配 Executor 的方式。
from jina import Document, DocumentArray, Flow

app = typer.Typer(name="JinaDemo", add_completion=False, help="This is demo application for Jina.")
# 读取 jsonl 文件。也可以从 url 读取文件。
recipes = Clumper.read_jsonl("static/recipes.jsonl").collect()

# A DocumentArray is a list of Documents.
# DocumentArray 是一个文档列表。
docs = DocumentArray(
    # 获取每一行json中key=="name"的值
    [Document(text=d['name']) for d in recipes]
)

# Create a new Flow to process our Documents
# 创建一个新流程来处理我们的文档
flow = (
    Flow(protocol="http", port_expose=12345)
    .add(uses="jinahub://TransformerTorchEncoder", name="encoder", install_requirements=True)
    .add(uses="jinahub://SimpleIndexer", install_requirements=True, name="indexer", workspace="workspace")
)

def print_search_results(response, number=5):
    matches = response[0].data.docs[0].matches

    print("\nYour search results")
    print("===================\n")

    for match in matches[0:number]:
        print(f"- {match.text}")


@app.command()
def index():
    """Use Jina to index the recipe data."""
    # 使用 Jina 索引配方数据。
    with flow:
        flow.index(inputs=docs)

@app.command()
def search():
    """Use Jina to search in the recipe data."""
    # 使用 Jina 在配方数据中进行搜索。
    with flow:
        while True:
            query = Document(text=input("Enter a query: "))
            response = flow.search(inputs=query, return_results=True)
            print_search_results(response)

@app.command()
def serve():
    """Use Jina to search in the recipe data."""
    # 使用 Jina 在配方数据中进行搜索。
    with flow:
        flow.block()

if __name__ == "__main__":
    app()
