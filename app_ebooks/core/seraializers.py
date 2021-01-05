from rest_framework import serializers

from core.models import EBooks, Reviews


class ReviewSerializer(serializers.ModelSerializer):

    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reviews
        fields = (
            "created_at",
            "updated_at",
            "review_author",
            "rating",
        )


class EBookSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = EBooks
        fields = (
            "name",
            "completed",
            "author",
            "description",
            "publication_date",
            "reviews",
        )
