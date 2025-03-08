# BCD Embedding Server

## Introduction
Bilingual and Crosslingual Embedding (BCEmbedding), developed by NetEase Youdao, encompasses EmbeddingModel and RerankerModel. The EmbeddingModel specializes in generating semantic vectors, playing a crucial role in semantic search and question-answering, and the RerankerModel excels at refining search results and ranking tasks.


## Requirements
- Python 3.12
- docker & docker-compose 
- huggingface models [bce-embedding-base_v1](https://huggingface.co/maidalun1020/bce-embedding-base_v1) [bce-reranker-base_v1](https://huggingface.co/maidalun1020/bce-reranker-base_v1)

## Installation
```shell
pip install -r requirements.txt
```
Finally, project files are organized as follows:
```
.
├── README.md
├── pretrained_model
│   ├── bce-embedding-base_v1
│   │   ├── 1_Pooling
│   │   │   └── config.json
│   │   ├── README.md
│   │   ├── assets
│   │   │   ├── Wechat.jpg
│   │   │   └── rag_eval_multiple_domains_summary.jpg
│   │   ├── config.json
│   │   ├── config_sentence_transformers.json
│   │   ├── modules.json
│   │   ├── pytorch_model.bin
│   │   ├── sentence_bert_config.json
│   │   ├── sentencepiece.bpe.model
│   │   ├── special_tokens_map.json
│   │   ├── tokenizer.json
│   │   └── tokenizer_config.json
│   └── bce-reranker-base_v1
│       ├── README.md
│       ├── assets
│       │   ├── Wechat.jpg
│       │   └── rag_eval_multiple_domains_summary.jpg
│       ├── config.json
│       ├── pytorch_model.bin
│       ├── sentencepiece.bpe.model
│       ├── special_tokens_map.json
│       ├── tokenizer.json
│       └── tokenizer_config.json
├── requirements.txt
└── src
    ├── __pycache__
    │   └── app.cpython-312.pyc
    ├── app.py
    └── embeding
        ├── __pycache__
        │   ├── encode.cpython-312.pyc
        │   └── rerank.cpython-312.pyc
        ├── encode.py
        └── rerank.py

```

## Configuration
```shell
# .env
# model path, that is the path of the pretrained models bce-embedding-base-v1 and bce-reranker-base-v1 
MODEL_PATH=./pretrained_model

# Server port
SERVER_PORT=8000

# Debug mode
DEBUG=False
```

## Usage
```shell
python -m src.app
```
docker-compose run 
```shell
sh install.sh
```

docker-compose run (on nvidia docker)
```shell
sh install-gpu.sh
```

## API

### Embedding
```shell
curl --location 'http://127.0.0.1:8000/encode' \
--header 'Content-Type: application/json' \
--data '{
    "sentences": [
        "hello"
    ]
}'

```
response data format :
```
[
    [
        0.024592425674200058,
        ...
        0.014320493675768375
    ]
]
```


### Rerank
```shell
curl --location 'http://127.0.0.1:8000/rerank' \
--header 'Content-Type: application/json' \
--data '{
    "sentences": [
        "你好我是lorne",
        "你是谁啊？"
    ],
    "query":"你是谁？"
}'
```

response data format :
```
{
    "rerank_ids": [
        1,
        0
    ],
    "rerank_passages": [
        "你是谁啊？",
        "你好我是lorne"
    ],
    "rerank_scores": [
        0.6116276383399963,
        0.498232364654541
    ]
}
```

### Score
```shell
curl --location 'http://127.0.0.1:8000/score' \
--header 'Content-Type: application/json' \
--data '{
    "sentences": [
        "你好我是lorne",
        "你是谁啊？"
    ],
    "query":"你是谁？"
}'
```

response data format :
```
[
    0.498232364654541,
    0.6116276383399963
]
```
## QA
### Docker nvidia runtime error
add /etc/docker/daemon.json runtimes setting and restart docker `sudo systemctl restart docker`
```shell
{
    "runtimes": {
        "nvidia": {
            "path": "/usr/bin/nvidia-container-runtime",
            "runtimeArgs": []
        }
    },
    "default-runtime": "runc"
}
```

## References
- [bce-embedding](https://github.com/netease-youdao/BCEmbedding)
