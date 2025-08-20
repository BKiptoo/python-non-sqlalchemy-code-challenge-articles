class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article._all_articles if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list({mag.category for mag in mags})

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Magazine category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [article for article in Article._all_articles if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [article.title for article in arts]

    def contributing_authors(self):
        from collections import Counter
        authors = [article.author for article in self.articles()]
        count = Counter(authors)
        result = [author for author, num in count.items() if num > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        mags = cls._all_magazines
        if not mags:
            return None
        return max(mags, key=lambda m: len(m.articles()), default=None) if any(m.articles() for m in mags) else None

class Article:

    _all_articles = []
    all = []


    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Article author must be an Author instance.")
        if not isinstance(magazine, Magazine):
            raise Exception("Article magazine must be a Magazine instance.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Article title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article._all_articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Article author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Article magazine must be a Magazine instance.")
        self._magazine = value