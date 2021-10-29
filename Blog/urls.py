from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('img/<int:id>',views.viewimage,name='viewimg'),

    path('login',views.UserLogin,name='login'),
    path('logout',views.userlogout,name='logout'),
    path('signup',views.userSignUp,name='signup'),
    path('changepassword',views.changepassword,name='changepassword'),


    path('contact/',views.Contact,name='contact'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('profile',views.userprofile,name='profile'),
    path('profile/<int:id>',views.userprofile,name='viewuser'),


    path('likepost/<int:id>',views.like,name='likepost'),
    path('addpost',views.addpost,name='addpost'),
    path('search',views.search,name='search'),
    path('sort_today',views.sortby,name='sortby'),
    path('contact/',views.contact,name='contact'),
    path('delete/<int:id>',views.deletepost,name='delete'),
]
