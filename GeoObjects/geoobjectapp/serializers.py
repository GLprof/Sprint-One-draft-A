from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from user.serializers import UserSerializer
from .models import GeoObject, GeoObjectCoords, GeoObjectLevel, GeoObjectImage

class CoordsS(serializers.ModelSerializer):
    model = GeoObjectCoords
    fields = ('latitude', 'longitude', 'height')