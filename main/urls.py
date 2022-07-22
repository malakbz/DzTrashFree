from django.urls import path
from . import views
from .views import (event_create_view,
                     SignUpView,
                     participate_event)

urlpatterns = [
    path('user-events/', views.participate_event, name='user-events'),
 
    path('organisation-events/', views.organisation_events,
         name='organisation-events'),


    path('user-posts/', views.user_posts, name='user-posts'),
    path('user-home/', views.userpost_create_view, name='user-home'),
    path('organisation-home/', views.organisation_home, name='organisation-home'),

    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.loginpage, name='login'),
    path('home/', views.home, name='home'),

    path('create-event/', event_create_view, name='create-view'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('user-profile/', views.updat_profile,
         name='user-profile'),
    #     path('user-profile/', views.userProfile,
    #          name='user-profile'),

    path('organisation-posts/', views.event_create_view,
         name='organisation-posts'),
    #     path('organisation-posts/',  PostListView.as_view(),
    #          name='organisation-posts'),
]
