from rest_framework import serializers
from .models import Product, Album, Catalog, Category


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class ProductPopup(serializers.ModelSerializer):
    album_set = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'color', 'size', 'album_set', 'safety', 'interface']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):
    category_set = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Catalog
        fields = ['id', 'title', 'category_set']
