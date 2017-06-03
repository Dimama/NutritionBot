class SimilarSearcher(object):
    """ Класс для поиска похожих наименований в списке"""
    def __init__(self, words):
        self.words = words

    def search_similar(self, word):
        similar_words = []
        for target in self.words:
            if SimilarSearcher.is_similar(target, word):
                similar_words.append(target)
        return similar_words

    @staticmethod
    def is_similar(target, word):
        parts = word.split(" ")
        for part in parts:
            if part.strip().lower() in target.lower():
                return True
        return False
