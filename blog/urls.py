from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.DetailPostView.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/remove', views.DeletePostView.as_view(), name='delete_post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', views.CategoryView, name='category'),


]
