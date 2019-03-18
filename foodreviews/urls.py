from django.urls import path
from . import views


app_name = 'foodreviews'  

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.RestaurantsView.as_view(), name='restaurants'),    
    path('<int:pk>/reviews/', views.ReviewsView.as_view(), name='reviews'),
    path('reviews/add/', views.ReviewCreate.as_view(), name='add_review'),
    path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='update_review'),
    path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='delete_review'),
    path('reviews/<int:pk>/comment/', views.CommentCreate.as_view(), name='add_comment'),
    path('comment/<int:pk>/', views.ReplyCreate.as_view(), name='add_reply'),
    path('reviews/<int:review_id>/like/', views.like, name='like'),
    
    ]