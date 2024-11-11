from rest_framework import serializers
from market_app import models
from market_app.models import Market, Seller , Product
 
def validate_no_X(value):
       errors= []
       if 'X' in value:
           errors.append('no X in location') 
       if 'Y' in value:
           errors.append('no Y in location')

       if errors:
           raise serializers.ValidationError(errors)
       return value

class MarketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255,validators=[validate_no_X] )
    description = serializers.CharField()
    net_worth = serializers.DecimalField(max_digits=100, decimal_places=2)

    def create(self, validated_data):
        return Market.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
      instance.name = validated_data.get('name', instance.name)
      instance.location = validated_data.get('location', instance.location)
      instance.description = validated_data.get('description', instance.description)
      instance.net_worth = validated_data.get('net_worth', instance.net_worth)
      instance.save()
      return instance
    
class SellerDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    contact_info = serializers.CharField()
    # markets = MarketSerializer(many=True, read_only=True)
    markets = serializers.StringRelatedField(many=True)

class SellerCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    contact_info = serializers.CharField()
    markets = serializers.ListField(child=serializers.IntegerField(), write_only=True)


    def validate_markets(self, value):
        markets = Market.objects.filter(id_in=value)
        if len(markets) != len(value):
             raise serializers.ValidationError({"message": "passt halt nicht mit den ids"})
        return value
    
    def create(self, validated_data):
        market_ids= validated_data.pop('markets')
        seller = Seller.objects.create(**validated_data)
        markets = Market.objects.filter(id_in=market_ids)
        seller.markets.set(markets)
        return seller
    
    # PRODUCT 
    
class ProductDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(max_length=255)
        description = serializers.CharField(max_length=555)
        price = serializers.DecimalField(max_digits=50, decimal_places=2)
        markets = serializers.PrimaryKeyRelatedField(many=True, queryset=Market.objects.all())
        seller = serializers.PrimaryKeyRelatedField(many=True, queryset=Seller.objects.all())

class ProductCreateSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)
        description = serializers.CharField(max_length=555)
        price = serializers.DecimalField(max_digits=50, decimal_places=2)
        markets = serializers.PrimaryKeyRelatedField(many=True, queryset=Market.objects.all())
        seller = serializers.PrimaryKeyRelatedField(many=True, queryset=Seller.objects.all())


        def validate_markets(self, value):
          markets = Market.objects.filter(id_in=value)
          if len(markets) != len(value):
              raise serializers.ValidationError({"message": "passt halt nicht mit den ids"})
          return value
        
        def validate_seller(self, value):
          seller = Seller.objects.filter(id_in=value)
          if len(seller) != len(value):
              raise serializers.ValidationError({"message": "passt halt nicht mit den ids"})
          return value
    
        def create(self, validated_data):
         market_ids= validated_data.pop('markets')
         product = Product.objects.create(**validated_data)
         markets = Market.objects.filter(id_in=market_ids)
         product.markets.set(markets)
         return product