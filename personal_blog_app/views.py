from django.views.generic import TemplateView
from .models import Post


class HomeView(TemplateView):
    template_name = 'index.html'


class PostView(TemplateView):
    template_name = 'post.html'
