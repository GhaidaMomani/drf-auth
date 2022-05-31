from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import (
                                        ListCreateAPIView
                                    )
from rest_framework.permissions import IsAuthenticated

from .models import game
from .serializers import GameSerializer


class GameListView(ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)


