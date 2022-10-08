from app import app
from exceptions.data_exceptions import DataSourceError


@app.errorhandler(404)
def page_error_404(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"На сервере произошла ошибка - {error}", 500


@app.errorhandler(DataSourceError)
def page_error_data_source_error(error):
    return f"Ошибка, на сайте поломались данные {error}", 500
