from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from api.v1.results.models import Result, ResultType
from api.v1.results.serializers import ResultSerializer, ResultTypeSerializer

# Create your views here.

class ResultTypeViewSet(viewsets.ModelViewSet):
    '''
        This viewset allows to CRUD all the ResultTypes of the system.
    '''

    queryset = ResultType.objects.all().order_by('-id')
    serializer_class = ResultTypeSerializer

class ResultViewSet(viewsets.ModelViewSet):
    '''
        This viewset allows to CRUD all the Results of the system.
    '''

    queryset = Result.objects.all().order_by('-id')
    serializer_class = ResultSerializer