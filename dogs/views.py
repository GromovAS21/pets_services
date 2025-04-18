"""URL для приложения Dog."""

from typing import Type

from django.db.models import Avg, Count
from rest_framework import viewsets

from dogs.models import Dog
from dogs.serializers import DogDetailSerializer, DogListSerializer, DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    """Представление собак."""

    queryset = Dog.objects.annotate(avg_age=Avg("breed__dogs__age"), num_same_breed=Count("breed__dogs"))
    serializer_class = DogSerializer

    def get_serializer_class(self) -> Type[DogSerializer]:
        """Возвращаем сериализаторы в зависимости от действия.

        Returns:
            Class: сериализатор для модели Dog
        """
        if self.action == "list":
            return DogListSerializer
        elif self.action == "retrieve":
            return DogDetailSerializer
        return DogSerializer
