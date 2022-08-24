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

## BUG记录
### 环境问题(Jina和tensorflow,tensorboard,tensorflow-hub,tensorflow-text不在同一个区间)
```commandline
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
tensorflow 2.7.3 requires protobuf<3.20,>=3.9.2, but you have protobuf 3.0.0 which is incompatible.
tensorflow-text 2.9.0 requires tensorflow<2.10,>=2.9.0; platform_machine != "arm64" or platform_system != "Darwin", but you have tensorflow 2.7.3 which is incompatible.
tensorflow-hub 0.12.0 requires protobuf>=3.8.0, but you have protobuf 3.0.0 which is incompatible.
tensorboard 2.10.0 requires protobuf<3.20,>=3.9.2, but you have protobuf 3.0.0 which is incompatible.
jina 2.6.4 requires protobuf>=3.13.0, but you have protobuf 3.0.0 which is incompatible.
```

## 参考资料
1. [github-retreival-jina](https://github.com/RasaHQ/rasa-action-examples/tree/main/retreival-jina)
2. [githut-Jina](https://github.com/jina-ai/jina)