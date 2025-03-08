from BCEmbedding import EmbeddingModel

class Embedding:

    def __init__(self, model_path: str):
        self.model = EmbeddingModel(f'{model_path}/bce-embedding-base_v1')

    def encode(self, sentences):
        return self.model.encode(sentences).tolist()

