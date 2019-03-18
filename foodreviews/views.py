from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Restaurant, Review, Comment, Reply, Like
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms

class IndexView(generic.ListView):
    template_name = 'foodreviews/index.html'
    context_object_name = 'categories'
    model = Category

class RestaurantsView(generic.DetailView):
    model = Category
    template_name = 'foodreviews/restaurants.html'

class ReviewsView(generic.DetailView):
    model = Restaurant
    template_name = 'foodreviews/reviews.html'

def like(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    new_like, created = Like.objects.get_or_create(liked_by=request.user, review_id=review_id)
    return HttpResponseRedirect('/foodreviews/%i/reviews/' % review.restaurant.pk)

class ReviewCreate(CreateView):
    model = Review
    fields = ['restaurant', 'photo', 'rating', 'experience_text']
    template_name = 'foodreviews/add_review.html'
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.pub_date = timezone.now()
        return super().form_valid(form)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ReviewUpdate(UpdateView):
    model = Review
    fields = ['rating', 'photo', 'experience_text']
    template_name = 'foodreviews/update_review.html'

class ReviewDelete(DeleteView):
    model = Review
    fields = ['restaurant', 'rating', 'photo', 'experience_text']
    template_name = 'foodreviews/delete_review.html'

    def get_success_url(self):
        return reverse('foodreviews:reviews', kwargs={'pk': self.object.restaurant.id})

class CommentCreate(CreateView):
    model = Comment
    fields = ['review', 'comment_text']
    template_name = 'foodreviews/add_comment.html'

    def get_initial(self):
        review = get_object_or_404(Review, id=self.kwargs.get('pk'))
        return {
            'review':review,
        }

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.created_date = timezone.now()
        return super().form_valid(form)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ReplyCreate(CreateView):
    model = Reply
    fields = ['comment', 'reply_text']
    template_name = 'foodreviews/add_reply.html'

    def get_initial(self):
        comment = get_object_or_404(Comment, id=self.kwargs.get('pk'))
        return {
            'comment':comment,
        }

    def form_valid(self, form):
        form.instance.replied_by = self.request.user
        form.instance.reply_date = timezone.now()
        return super().form_valid(form)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)