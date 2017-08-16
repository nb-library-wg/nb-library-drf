from django.contrib.auth.models import User
from rest_framework import viewsets
from library.api.models import Book
from library.api.serializers import (
    BookSerializer,
    UserSerializer,
)


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()[:10]
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
