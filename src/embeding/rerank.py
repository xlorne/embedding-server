from BCEmbedding import RerankerModel


class Reranker:
    def __init__(self, model_path: str):
        self.model = RerankerModel(f'{model_path}/bce-reranker-base_v1')

    def rerank(self, query:str, sentences:list[str]) -> list[float]:
        return self.model.rerank(query,sentences)


    def score(self, query:str, sentences: list[str]) -> list[float]:
        sentence_pairs = [[query, sentence] for sentence in sentences]
        return self.model.compute_score(sentence_pairs)
