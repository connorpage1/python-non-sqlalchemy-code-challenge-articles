class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if type(new_author) != Author:
            raise TypeError("Author must be an Author object")
        else: 
            self._author = new_author
            
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if type(new_magazine) != Magazine:
            raise TypeError("Magazine must be an Magazine object")
        else: 
            self._magazine = new_magazine
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if type(new_title) != str:
            raise TypeError("Title must be of type string")
        elif not 4 < len(new_title) <= 50:
            raise ValueError("Title must be at between 5 and 50 characters in length")
        elif hasattr(self, "title"):
            raise PermissionError("Cannot change title")
        else:
            self._title = new_title
        
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    
    
    @property
    def name (self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Name must be of type string")
        elif not new_name:
            raise ValueError("Name must be at least one character")
        elif hasattr(self, "name"):
            raise PermissionError("Cannot change name")
        else:
            self._name = new_name
            
            
    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({magazine for magazine in Magazine.all if self in magazine.contributors()})

    def add_article(self, magazine, title):
        if type(magazine) is not Magazine:
            raise TypeError("Magazine must be a Magazine object")
        elif type(title) != str:
            raise TypeError("Title must be a string")
        elif not 4 < len(title) <= 50:
            raise ValueError("Title must be at between 5 and 50 characters in length")
        else:
            return Article(self, magazine, title)
        
    def topic_areas(self):
        if self.articles():
            return list({magazine.category for magazine in self.magazines()})
        else:
            return None

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Name must be of type string")
        elif not 1 < len(new_name) <= 16:
            raise ValueError("Names must be between 2 and 16 characters long")
        else:
            self._name = new_name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if type(new_category) != str:
            raise TypeError("Category must be of type string")
        elif not new_category:
            raise ValueError("Categories must be at least one character")
        else:
            self._category = new_category
    
    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        if self.articles():
            return [article.title for article in self.articles()]
        return None

    def contributing_authors(self):
        all_authors = [article.author for article in self.articles()]
        if contributing_author_list := [
            author for author in all_authors if all_authors.count(author) > 2
            ]:
            return contributing_author_list
        
        return None
    
    @classmethod
    def top_publisher(cls):
        mag_dict = {}
        top_mag = None
        if Article.all: 
            for article in Article.all:
                if article.magazine not in mag_dict:
                    mag_dict[article.magazine] = 1  
                else:
                    mag_dict[article.magazine] += 1
        
        top_count = 0
        for magazine, count in mag_dict.items():
            if count > top_count:
                top_count = count
                top_mag = magazine
                
                    
        return top_mag
        