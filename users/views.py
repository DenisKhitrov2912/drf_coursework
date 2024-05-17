from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from users.models import User
from users.permissions import IsUserUser
from users.serializers import UserSerializer, UserSerializerForOthers


class UserCreateView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserDetailView(generics.RetrieveAPIView):
    """Просмотр пользователя"""
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user.id == self.get_object().id:
            return UserSerializer
        return UserSerializerForOthers


class UserUpdateView(generics.UpdateAPIView):
    """Обновление пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUserUser]


class UserDeleteView(generics.DestroyAPIView):
    """Удаление пользоватлея"""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUserUser | IsAdminUser]


class UserListView(generics.ListAPIView):
    """Список пользователей"""
    serializer_class = UserSerializerForOthers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
