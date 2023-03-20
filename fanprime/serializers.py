from rest_framework import serializers
from .models import Offer, Competence


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = "__all__"


class OfferSerializer(serializers.ModelSerializer):
    competences = CompetenceSerializer(many=True)

    class Meta:
        model = Offer
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        competences_data = validated_data.pop("competences")
        offer = Offer.objects.create(**validated_data)
        for competence_data in competences_data:
            competence, _ = Competence.objects.get_or_create(**competence_data)
            offer.competences.add(competence)
        return offer
