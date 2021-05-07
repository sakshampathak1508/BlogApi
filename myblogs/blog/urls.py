from knox import views as knox_views
from django.urls import path,include
from .views import LoginAPI
from . import views
urlpatterns = [
    path('blogs/',views.PostList.as_view(),name="PostList"),
    path('blogs/<int:id>',views.PostDetail.as_view(),name="PostDetail"),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/login/',LoginAPI.as_view(), name='login'),
    # path('api/logout/',views.knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/',views.knox_views.LogoutAllView.as_view(), name='logoutall'),
]