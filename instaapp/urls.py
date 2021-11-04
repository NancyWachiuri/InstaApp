from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[

    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.userPage,name='user-page'),
    path('user/',views.logoutUser,name='logout'),
    path('',views.logincup,name='auth'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.post, name='post_list'),
    path('new/', views.create_post, name='post'),
    path('',views.post,name='post_list'),
    path('add-comment/<int:pk>/', views.add_comment, name='add-comment'),
    path('delete-comment/<int:pk>/', views.delete_comment, name='delete-comment'),
    path('like/', views.like_post, name='like-post'),
    path('search_results/',views.search_results, name='search_results'),


]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    