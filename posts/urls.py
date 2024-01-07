from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('create/', views.create_post, name='create_post-page'),
    path('<int:post_id>/comment/',views.add_comment, name='add_comment'),
    path('<int:post_id>/like/', views.like_post, name='like_post'),
    path('<int:post_id>/post', views.post_detail, name='post-detail'),
    path('add_hashtags/', views.create_hashtag, name='addhashtag-page'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete-comment'),
    path('search/', views.search_product, name='search-page'),
    path('hashtag/<str:hashtag>/', views.hashtag, name='hashtag' )
]