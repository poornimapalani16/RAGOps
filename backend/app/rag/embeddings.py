from fastembed import TextEmbedding


class FastEmbedEmbeddings:

    def __init__(self):

        self.model = TextEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )


    def embed_documents(
        self,
        texts: list[str]
    ) -> list[list[float]]:

        embeddings = self.model.embed(
            texts
        )

        return [
            vector.tolist()
            for vector in embeddings
        ]


    def embed_query(
        self,
        text: str
    ) -> list[float]:

        embedding = next(
            self.model.embed([text])
        )

        return embedding.tolist()


embeddings = FastEmbedEmbeddings()