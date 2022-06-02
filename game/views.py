from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateDestroyAPIView,

                                    )
from rest_framework.permissions import IsAuthenticated

from .models import Game
from .serializers import GameSerializer


class GameListView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)


class GameDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)
    