from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('sermons/', views.sermon_list, name='sermon_list'),
    path('books/', views.book_list, name='book_list'),
    path('songs/', views.song_list, name='song_list'),
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
