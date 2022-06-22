import logging
from flask import Blueprint, jsonify, abort
from curs_work3.bp_posts.dao.comment_dao import CommentDao
from curs_work3.bp_posts.dao.post import Post
from curs_work3.bp_posts.dao.post_dao import PostDAO
from curs_work3.config import DATA_PATH_POST, DATA_PATH_COMMENTS


#Создаем блупринт
bp_api = Blueprint("bp_api", __name__)

#Создаем объекты доступа к данным
posts_dao = PostDAO(DATA_PATH_POST)
comments_dao = CommentDao(DATA_PATH_COMMENTS)

api_logger = logging.getLogger("api_logger")


@bp_api.route("/posts/")
def api_posts_all():
    """Эндпоинт для всех постов"""
    all_posts: list[Post] = posts_dao.get_posts_all()
    api_logger.debug("Запрошены все посты")

    return jsonify([post.as_dict() for post in all_posts]), 200


@bp_api.route("/posts/<int:pk>")
def api_posts_single(pk: int):
    """Эндпоинт для одного поста"""
    post: Post | None = posts_dao.get_post_by_pk(pk)
    if post is None:
        api_logger.debug(f"Обращение к несуществующему посту {pk}")
        abort(404)
    api_logger.debug(f"Запрошен пост {pk}")
    return jsonify(post.as_dict()), 200


@bp_api.errorhandler(404)
def api_error_404(error):
    api_logger.error(f"Ошибка {error}")
    return jsonify({"error": str(error)}), 404


@bp_api.route("/posts/")
def api_posts_hello():
    return "Это api. Доступные эндпоинты /api/posts и /api/posts/ Смотри документацию у меня на гитхабе"
