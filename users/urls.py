from django.urls import path

from users.apps import UsersConfig
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserListView, UserCreateView, UserDetailView, UserUpdateView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserListView.as_view(), name='users'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
