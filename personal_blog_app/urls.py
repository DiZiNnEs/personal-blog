from django.urls import path

from personal_blog_app.views import HomeView, PostView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('post/<int:pk>', PostView.as_view(), name='post_view'),
]
