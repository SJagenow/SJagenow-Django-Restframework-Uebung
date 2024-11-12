from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketHayperlinkedSerializer, MarketSerializer, ProductCreateSerializer, ProductDetailSerializer, SellerSerializer
from market_app.models import Market, Product, Seller


@api_view(['GET','POST']) #decorator
def markets_view(request):
    if request.method == 'GET':
      markets = Market.objects.all()
      serializer = MarketHayperlinkedSerializer(markets, many=True,context={'request': request},fields=('id','url','name'))
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
      serializer = MarketSerializer(market,context={'request': request})
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
       serializer = SellerSerializer(sellers, many=True)
       return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        


@api_view(['GET', 'DELETE', 'PUT'])  # Decorator für die Methoden GET, DELETE, PUT
def seller_single_view(request, pk):
     try:
      seller = Seller.objects.get(pk=pk)
     except Seller.DoesNotExist:
      raise (f'Seller with id {pk} not found.')  # Fehlerbehandlung, falls der Verkäufer nicht existiert

     if request.method == 'GET':
        serializer = SellerSerializer(seller,context={'request': request})
        return Response(serializer.data)

     if request.method == 'PUT':
        serializer = SellerSerializer(seller, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

     if request.method == 'DELETE':
        seller.delete()
        return Response(status=204)  # 204 No Content, um anzuzeigen, dass die Löschung erfolgreich war

# PRODUCT

@api_view(['GET', 'POST'])
def products_view(request):
   if request.method == 'GET':
      products = Product.objects.all()
      serializer = ProductDetailSerializer(products, many = True)
      return Response(serializer.data)
   
   if request.method == 'POST':
       serializer = ProductCreateSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors)
       
       
  
