# Create your views here.
from django.views.generic.list import ListView
from models import Post
from django.views.generic.detail import DetailView
from forms import CommentForm
from django.http import HttpResponseRedirect
from django.db import models


class BlogView(ListView):
    model = Post

    def get_queryset(self):
        qs = super(BlogView, self).get_queryset()
        qs = qs.annotate(comments_count = models.Count('comments'))
        return qs


class PostView(DetailView):
    model = Post
    context_object_name = 'post'
    
    
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        obj = kwargs['object']
        context['comment_form'] = CommentForm()
        context['comments'] = obj.comments.all()
        return context

    def post(self, request, **kwargs):
        comment_form = CommentForm(request.POST)
        self.object = self.get_object()
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = self.object
            comment.save()
            return HttpResponseRedirect('')
        context = self.get_context_data(object=self.object)
        context['comment_form'] = comment_form
        return self.render_to_response(context)
    

    