from rest_framework.generics import ListAPIView

from .serializers import *
from .models import *


class SetApi(ListAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer


class LiftApi(ListAPIView):
    queryset = Lift.objects.all()
    serializer_class = LiftSerializer


class SessionApi(ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
