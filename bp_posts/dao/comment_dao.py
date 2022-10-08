import json
from json import JSONDecodeError
from bp_posts.dao.comment import Comment
from exceptions.data_exceptions import DataSourceError


class CommentDao:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """Загружает данные из json файла (одно и тоже)"""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                posts_data = json.load(file)

        except(FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"не удается получить данные из {self.path}")

        return posts_data

    def load_comments(self):
        """Возвращает список экземляров Comment"""
        comments_data = self.load_data()
        list_of_comments = [Comment(**comment_data) for comment_data in comments_data]

        return list_of_comments

    def get_comments_by_post_pk(self, post_pk):
        """Получает все комментарии к определенному посту по его post_pk"""
        if type(post_pk) != int:
            raise TypeError("post_pk must be int")

        #for comment_data in comments_data:
            #if comment_data.post_pk == post_pk:
                #return comment_data

        comments_data = self.load_comments()
        comment_match = [comment_data for comment_data in comments_data if comment_data.post_pk == post_pk]
        return comment_match
