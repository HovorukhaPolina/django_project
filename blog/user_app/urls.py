from django.urls import path

import user_app

urlpatterns = [
    path('profile/', user_app.index, name='profile'),
]