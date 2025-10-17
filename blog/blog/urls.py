from django.contrib import admin
from django.urls import path, include

import user_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_app.index),
    path('user/', include("User.urls")),
    path('posts/', include("Posts.urls")),
]