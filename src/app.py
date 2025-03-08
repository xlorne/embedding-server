import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from src.embeding.encode import Embedding
from src.embeding.rerank import Reranker

load_dotenv()

SERVER_PORT = os.getenv("SERVER_PORT")
MODEL_PATH = os.getenv("MODEL_PATH")

embedding = Embedding(MODEL_PATH)
reranker = Reranker(MODEL_PATH)
app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

# 向量化
@app.route('/encode', methods=['POST'])
def encode():
    request_body = request.get_json()
    sentences = request_body['sentences']
    embeddings = embedding.encode(sentences)
    return jsonify(embeddings), 200

# 获取精排结果
@app.route('/rerank', methods=['POST'])
def rerank():
    request_body = request.get_json()
    query = request_body['query']
    sentences = request_body['sentences']
    rerank_results = reranker.rerank(query, sentences)
    return jsonify(rerank_results), 200

# 获取数据排序
@app.route('/score', methods=['POST'])
def score():
    request_body = request.get_json()
    query = request_body['query']
    sentences = request_body['sentences']
    rerank_results = reranker.score(query, sentences)
    return jsonify(rerank_results), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=SERVER_PORT,debug=True)