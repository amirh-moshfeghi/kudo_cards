import datetime

from django.core import serializers
from django.core.mail import EmailMessage
from django.core.serializers import json
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Kudo
from .permissions import IsOwnerOrReadOnly, IsAdminOfTeamOnly, IsAdminOfDepartmentOnly
from .serializers import KudoSerializer
from .pagination import CustomPagination
from .filters import KudoFilter


class ListCreateKudoAPIView(ListCreateAPIView):
    """
    create kudo instances
    """


    serializer_class = KudoSerializer
    queryset = Kudo.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = KudoFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        employee_email = self.request.POST.get('employee')
        current_date = datetime.datetime.now()
        email = EmailMessage(
            'a note to remember',
            'thank you',
            employee_email,
            []
        )
        email.send()
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyKudoAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = KudoSerializer
    queryset = Kudo.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class RetrieveEmployeeAPIView(APIView):
    """
    Retrieve, update or delete a employee instance.
    """

    @csrf_exempt
    def get_object(self, pk):
        try:
            return Kudo.objects.values('id', 'title').filter(employee_id=pk)
        except ValueError:
            raise Http404

    @csrf_exempt
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        s_logs = list(snippet.values('title', 'id'))
        return JsonResponse(s_logs, safe=False)


class RetrieveTeamAPIView(APIView):

    """
    Retrieve, update or delete a team instance.
    """
    permission_classes = [IsAuthenticated, IsAdminOfTeamOnly, IsAdminOfDepartmentOnly]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return Kudo.objects.filter(team_id=pk)
        except ValueError:
            raise Http404

    @csrf_exempt
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        s_logs = list(snippet.values('title', 'id'))
        return JsonResponse(s_logs, safe=False)


class RetrieveDepartmentAPIView(APIView):
    """
    Retrieve, update or delete a department instance.
    """
    permission_classes = [IsAuthenticated, IsAdminOfDepartmentOnly]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return Kudo.objects.filter(department_id=pk)
        except ValueError:
            raise Http404

    @csrf_exempt
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        s_logs = list(snippet.values())
        return JsonResponse(s_logs, safe=False)


