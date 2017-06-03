class SimilarSearcher(object):
    """ Класс для поиска похожих продуктов в списке"""
    def __init__(self, products):
        self.products = products

    def search_similar(self, word):
        similar_products = []
        for target in self.products:
            if SimilarSearcher.is_similar(target[1], word):
                similar_products.append(target)
        return similar_products

    @staticmethod
    def is_similar(target, word):
        parts = word.split(" ")
        for part in parts:
            if part.strip().lower() in target.lower().split(' ') and part.strip().lower() not in ["в", "на", "из", "с"]:
                return True
        return False
