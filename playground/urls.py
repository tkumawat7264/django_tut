from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

urlpatterns = [
    path('hello/', views.say_hello, name='hello'),
    path('test/', views.test_template, name='template-test'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/update/', views.profile_update, name='profile_update'),
    # path('profile/password/', views.password_update, name='password_update'),
    # path('profile/delete/', views.profile_delete, name='profile_delete'),
    # path('profile/<str:username>/', views.user_profile, name='user_profile'),
    # path('follow/<str:username>/', views.follow, name='follow'),
] + debug_toolbar_urls()