from django.urls import path

import post_app

urlpatterns = [
    path('posts/', post_app.index, name='posts'),
]