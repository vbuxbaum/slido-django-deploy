from django.urls import path
from slido_app.views import index, register_visitor, create_visitor, create_question


urlpatterns = [
    path("", index, name="homepage"),
    path("login/", register_visitor, name="login"),
    path("visitor/new", create_visitor, name="create_visitor"),
    path("question/new", create_question, name="create_question"),
]
