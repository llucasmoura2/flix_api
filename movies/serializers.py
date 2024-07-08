from django.db.models import Avg
from rest_framework import serializers
from genres.serializers import GenreSerializer
from actors.serialiazers import ActorSerialiazer
from movies.models import Movie


class MovieModelSerialiazer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):

        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('O ano do filme não pode ser anterior a 1910')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('resumo não deve ser maior que 200 caracteres')
        return value


class movieDetailSerialiazer(serializers.ModelSerializer):
    actors = ActorSerialiazer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):

        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
