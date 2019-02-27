from django.urls import path
from . import views


app_name = 'foodreviews'  

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.RestaurantsView.as_view(), name='restaurants'),    
    path('<int:pk>/reviews/', views.ReviewsView.as_view(), name='reviews'),

]