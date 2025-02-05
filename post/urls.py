from django.urls import path, include
from post.views import home, post, login_view, logout_view, registration, makepost, add_comment, createpost, dashboard, delete,editpost

urlpatterns = [
    path('', home, name='home'),
    path('makepost/', makepost, name='makepost'),
    path('createpost/', createpost, name='createpost'),
    path('post/<str:post_id>', post, name='post'),
    path('comment/<str:post_id>', add_comment, name='comment'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('editpost/<str:pk>',editpost,name='edit'),
    path('signup/', registration, name='signup'),
    path('@<str:username>/', dashboard, name='dashboard'),
    path('delete/<str:pk>',delete,name='delete')
]
