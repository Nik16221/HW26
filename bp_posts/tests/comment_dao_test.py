import pytest
from curs_work3.bp_posts.dao.comment_dao import CommentDao


class TestCommentDAO:

    @pytest.fixture
    def comment_dao(self):
        comment_dao_instance = CommentDao("curs_work3/data/comments.json")
        return comment_dao_instance

    def test_get_all_correct_ids(self, comment_dao):
        comments = comment_dao.load_comments()

        correct_id = {1, 2, 3, 4, 5, 6, 7}
        ids = set(comment.post_id for comment in comments)
        assert ids == correct_id, "Не совпадают полученные id"
