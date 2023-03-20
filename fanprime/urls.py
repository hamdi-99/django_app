from .views import (
    CompetenceRetrieveUpdateDestroy,
    OfferListCreate,
    CompetenceListCreate,
    OfferRetrieveUpdateDestroy,
)
from . import views

"""fanprime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("offers/", OfferListCreate.as_view(), name="offer-list-create"),
    path("competences/", CompetenceListCreate.as_view(), name="competence-list-create"),
    path(
        "offers/<int:pk>/",
        OfferRetrieveUpdateDestroy.as_view(),
        name="offer-retrieve-update-destroy",
    ),
    path(
        "competences/<int:pk>/",
        CompetenceRetrieveUpdateDestroy.as_view(),
        name="competence-retrieve-update-destroy",
    ),
]
