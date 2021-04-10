from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.login.views import RegisterView
from rest_framework.authtoken import views
from graphene_django.views import GraphQLView
from core.schema import schema

urlpatterns = [
    path('login/', views.obtain_auth_token, name='auth_login'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('admin/', admin.site.urls),
    path(r"graphql", GraphQLView.as_view(graphiql=True, schema=schema))
]
