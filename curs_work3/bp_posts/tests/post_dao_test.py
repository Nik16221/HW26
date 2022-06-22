import pytest
from curs_work3.bp_posts.dao.post import Post
from curs_work3.bp_posts.dao.post_dao import PostDAO


def check_fields(post):
    #assert hasattr(post, "poster_name"), "Нет поля"
    #assert hasattr(post, "poster_avatar"), "Нет поля"
    #assert hasattr(post, "pic"), "Нет поля"
    #assert hasattr(post, "content"), "Нет поля"
    #assert hasattr(post, "views_count"), "Нет поля"
    #assert hasattr(post, "likes_count"), "Нет поля"
    #assert hasattr(post, "pk"), "Нет поля"
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    for field in fields:
        assert hasattr(post, field), f"Нет поля {field}"


class TestPostsDAO:

    @pytest.fixture
    def post_dao(self):
        post_dao_instance = PostDAO("./bp_posts/tests/post_mock.json")
        return post_dao_instance

    def test_get_all_types(self, post_dao):
        posts = post_dao.get_posts_all()
        assert type(posts) == list, "incorrect type for result"

        post = post_dao.get_posts_all()[0]
        assert type(post) == Post, "incorrect type for result single item"

    def test_get_all_fields(self, post_dao):
        posts = post_dao.get_posts_all()
        post = post_dao.get_posts_all()[0]

        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        posts = post_dao.get_posts_all()

        correct_pks = {1, 2, 3}
        pks = set(post.pk for post in posts)
        assert pks == correct_pks, "Не совпадают полученные id"

    def test_get_by_pk_types(self, post_dao):
        post = post_dao.get_post_by_pk(1)
        assert type(post) == Post, "incorrect type for result single item"

    def test_get_by_pk_fields(self, post_dao):
        post = post_dao.get_post_by_pk(1)
        check_fields(post)

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_post_by_pk(999)
        assert post is None, "Should be None for non existent pk"

    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_pk_correct_id(self, post_dao, pk):
        post = post_dao.get_post_by_pk(pk)
        assert post.pk == pk, f"Incorrect post.pk for requesten post with pk = {pk}"

    def test_search_in_content_types(self, post_dao):
        posts = post_dao.search_in_content("ага")
        assert type(posts) == list, "incorrect type for result"

        post = post_dao.get_posts_all()[0]
        assert type(post) == Post, "incorrect type for result single item"

    def test_search_in_content_fields(self, post_dao):
        posts = post_dao.search_in_content("Ага")
        post = post_dao.get_posts_all()[0]
        check_fields(post)

    def test_search_in_content_not_found(self, post_dao):
        posts = post_dao.search_in_content("8989898")
        assert posts == [], "Should be [] for not substring found"

    @pytest.mark.parametrize("s, expected_pks", [
        ("Ага", {1}),
        ("Вышел", {2}),
        ("на", {1, 2, 3}),
    ])
    def test_search_in_content_results(self, post_dao, s, expected_pks):
        posts = post_dao.search_in_content(s)
        pks = set([post.pk for post in posts])
        assert pks == expected_pks, f"Incorrect result searching for {s}"
