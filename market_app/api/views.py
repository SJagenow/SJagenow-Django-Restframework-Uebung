from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer, ProductDetailSerializer,SellerDetailSerializer
from market_app.models import Market, Product, Seller


@api_view(['GET','POST']) #decorator
def markets_view(request):
    if request.method == 'GET':
      markets = Market.objects.all()
      serializer = MarketSerializer(markets, many=True)
      return Response(serializer.data)
    

    if request.method == 'POST':
       serializer = MarketSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
       else:
          return Response(serializer.errors)




@api_view(['GET', 'DELETE', 'PUT']) #decorator
def market_single_view(request, pk):

    if request.method == 'GET':
      market = Market.objects.get(pk=pk)
      serializer = MarketSerializer(market)
      return Response(serializer.data)
    
    if request.method == 'PUT':
      market = Market.objects.get(pk=pk)
      serializer = MarketSerializer(market, data=request.data, partial=True)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors)

    if request.method == 'DELETE':
       market = Market.objects.get(pk=pk)
       serializer = MarketSerializer(market)
       market.delete()
       return Response(serializer.data)



@api_view(['GET','POST']) #decorator
def sellers_view(request):
    if request.method == 'GET':
      sellers = Seller.objects.all()
      serializer = SellerDetailSerializer(sellers,many=True )
      return Response(serializer.data)
    





@api_view(['GET', 'POST'])
def products_view(request):
   if request.method == 'GET':
      products = Product.objects.all()
      serializer = ProductDetailSerializer(products, many = True)
      return Response(serializer.data)