from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [

    path('get_chain/', views.get_chain, name="get_chain"),
    path('mine_block/', views.mine_block, name="mine_block"),
    path('is_valid/', views.is_valid, name="is_valid"),
]