We use the `m3hrdadfi/recipe_nlg_lite` recipe dataset from huggingface for this demo. Note that this demo was made with Rasa 3.0.5 in mind.

Before running anything, be sure to install Rasa as well as the extra dependencies.

```
python -m pip install rasa==3.0.5
python -m pip install -r requirements.txt
```

To get started, we first need to index the dataset. We've made a script that can do this for you. 
首先，我们首先需要索引数据集。我们已经制作了一个可以为您执行此操作的脚本。
```
python scripts/prepare.py index
```

Once the dataset is indexed, you can use the jina pipeline to find search.
一旦数据集被索引，您就可以使用 jina 管道来查找搜索。
```
python scripts/prepare.py search
```

Given an indexed dataset, we can now also use it inside of a custom action too. The custom action is implemented as a proxy, so you'll need to run a jina server to use it.
给定一个索引数据集，我们现在也可以在自定义操作中使用它。自定义操作是作为代理实现的，因此您需要运行 jina 服务器才能使用它。
```
python scripts/prepare.py search
```

Once it's active you can talk to the assitant by running the Rasa shell. Don't forget to run the action server too!
一旦它处于活动状态，您就可以通过运行 Rasa shell 与助手交谈。不要忘记也运行动作服务器！
```
python -m rasa run actions
python -m rasa shell
```

## 参考资料
1. [github-retreival-jina](https://github.com/RasaHQ/rasa-action-examples/tree/main/retreival-jina)