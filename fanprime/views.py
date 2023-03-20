from rest_framework import generics
from .models import Offer, Competence
from .serializers import OfferSerializer, CompetenceSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from rest_framework.response import Response


class OfferListCreate(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class CompetenceListCreate(generics.ListCreateAPIView):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer


class OfferRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class CompetenceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer


def index(request):
    return render(request, "index.html")
