import metapy
import os


class Meta:
    def __init__(self, config="config.toml"):
        self.config = config
        if not os.path.exists(self.config):
            os.system.exit(1)

        idx = metapy.index.make_inverted_index(self.config)
        ranker = metapy.index.OkapiBM25()

    def add_query(self, q):
        query = metapy.index.Document()
        query.content(q)

    def search_inverted_index(self, q, num_results=20):
        """
        Return a ranked list of (doc_id, score) pairs
        """
        query = self.add_query(q)
        top_docs = self.ranker.score(self.idx, query, num_results)
        return top_docs