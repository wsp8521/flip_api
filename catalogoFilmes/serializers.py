from django.db.models import Avg
from rest_framework import serializers
from catalogoFilmes.models import Genre, Actor, Movie, Reviews


#Serializer Genre
class SerializerGenere(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'

#Serializer Actor
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'

#Serializer Movie
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
    #validação
    def validate_realese_data(self,value):
        if value.year<1990:
            raise serializers.ValidationError("Informe um filme posteiror a 1990")
        return value
        
    def validate_sinpse(self, value):
        if len(value)>250:
            raise serializers.ValidationError("Sinopse ultrapassou o limite de 250 caracteres")
        return value
    
#
class MovieSerializerGet(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)#criando campo somente leitura
    genre =SerializerGenere()
    actors = ActorSerializer(many=True)
    class Meta:
        model=Movie
        fields=['id','rate','title','genre','actors','realese_data','sinpse']

     #criando campo calculado
    def get_rate(self, obj):
        reviews = obj.reviws.aggregate(Avg('stars'))['stars__avg']

        if reviews:
            return round(reviews,1)
        return None


#Serializer Review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields='__all__'