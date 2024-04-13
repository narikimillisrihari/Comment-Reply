from django.contrib import admin
from django.urls import path
from fbapp import views

urlpatterns = [
    path('login/', views.login_view,name='login'),
    path('logout/', views.login_view,name='logout'),
    path('signup/',views.signup_view,name='signup'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('apppost/',views.addpost,name='apppost'),
    path('allpost/',views.allpost,name='allpost'),
    path('allpostdetail/<int:post_id>/',views.allpostdetail,name='allpostdetail'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('post_comment/<int:post_id>/', views.post_comment, name='post_comment'),
    path('post_details_comment/<int:post_id>/', views.post_details_comment, name='post_details_comment'),
    path('main_page_comment/<int:post_id>/', views.main_page_comment, name='main_page_comment'),
    path('main_page_reply/<int:post_id>/', views.main_page_reply, name='main_page_reply'),
    path('addcommentinside/<int:post_id>/', views.addcommentinside, name='addcommentinside'),
    path('delete_comment/<int:id>/', views.delete_comment, name='delete_comment'),
    path('delete_reply/<int:id>/', views.delete_reply, name='delete_reply'),
    path('comment_reply_view/<int:id>/', views.comment_reply_view, name='comment_reply_view'),

]