from json import JSONDecodeError
import json
from exceptions.data_exceptions import DataSourceError
from bp_posts.dao.post import Post


class PostDAO:

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

    def load_posts(self):
        """Возвращает список экземляров Post (одно и тоже)"""
        posts_data = self.load_data()
        list_of_posts = [Post(**post_data) for post_data in posts_data]
        #Post(poster_name=post_data("poster_name"),
                                    #poster_avatar=post_data("poster_avatar"),
                                    #pic=post_data("pic"),
                                    #content=post_data("content"),
                                    #views_count=post_data("views_count"),
                                    #likes_count=post_data("likes_count"),
                                    #pk=post_data("pk"))
        return list_of_posts

    def get_posts_all(self):
        """и снова тоже самое"""
        posts_data = self.load_posts()
        return posts_data

    def get_post_by_pk(self, pk):
        """Получаем пост по PK"""
        # posts_data = self.load_data()
        # post_pk = []
        # for post_data in posts_data:
        # if post_data.get("pk") == pk:
        # post_pk.append(post_data)
        # return post_pk

        # post_pk = [post_data for post_data in posts_data if post_data.pk == pk]
        # return post_pk
        if type(pk) != int:
            raise TypeError("pk must be int")

        posts_data = self.load_posts()
        for post_data in posts_data:
            if post_data.pk == pk:
                return post_data

    def search_in_content(self, substring):
        """Поиск среди постов по запросу substring"""
        # posts_data = self.load_posts()
        # for post_data in posts_data:
        # if substring in post_data.content.lower():
        # return post_data

        if type(substring) != str:
            raise TypeError("substring must be str")

        substring = str(substring).lower()
        posts_data = self.load_posts()
        post_substring = [post_data for post_data in posts_data if substring in post_data.content.lower()]

        return post_substring

    def get_post_by_poster(self, user_name):
        """Ищем посты по имени USERa"""
        if type(user_name) != str:
            raise TypeError("user_name must be str")

        user_name = str(user_name).lower()
        posts_data = self.load_posts()
        posts_by_name = [post_data for post_data in posts_data if post_data.poster_name.lower() == user_name]

        return posts_by_name
