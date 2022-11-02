from rest_framework import serializers
from candydendy.models import Candy


class CandySerializerFull(serializers.ModelSerializer):
    class Meta:
        model = Candy
        fields = [
            "name",
            "company",
            "company_country",
            "company_address",
            "company_site",
            "company_email",
            "company_phone_number",
            "company_director",
            "pricetag",
            "fats",
            "carbohydrates",
            "protein",
            "calories",
            "type",
            "rating"
        ]

class CandySerializerFree(serializers.ModelSerializer):
    class Meta:
        model = Candy
        fields = [
            "name",
            "fats",
            "carbohydrates",
            "protein",
            "calories",
            "type"
        ]