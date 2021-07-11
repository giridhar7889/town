from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import generate_transaction

app_name='flask_bc'
urlpatterns = [

    path('make_transaction/',generate_transaction.as_view(), name="generate_transaction"),
   # path('view_transactions/', views.view_transactions, name="view_transactions"),
    #path('new_wallet/', views.new_wallet, name="new_wallet"),
    #path('/', views.new_wallet, name="new_wallet"),

    ]
