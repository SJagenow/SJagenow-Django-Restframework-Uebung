from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketHayperlinkedSerializer, MarketSerializer, ProductSerializer, SellerListSerializer, SellerSerializer
from market_app.models import Market, Product, Seller
from rest_framework.views import APIView
from rest_framework import mixins,generics,viewsets

class ListRetrieveViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
   pass
class ListCreateRetrieveViewSet(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
   pass

#nicht veränderbar
class ProductViewSet(ListRetrieveViewSet):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer

class SellerViewSet(ListCreateRetrieveViewSet):
   queryset = Seller.objects.all()
   serializer_class = SellerSerializer


# class ProductViewSetOld(viewsets.ViewSet):
#   queryset = Product.objects.all()


#   def list(self, request):
#       serializer = ProductSerializer(self.queryset, many=True)
#       return Response(serializer.data)

#   def retrieve(self, request, pk=None):
      
#       product = get_object_or_404(self.queryset, pk=pk)
#       serializer = ProductSerializer(product)
    
#       return Response(serializer.data)

#   def create(self, request):
#       serializer = ProductSerializer(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data)
#       else:
#          return Response(serializer.errors)

 
#   def destroy(self, request, pk=None):
#       product = get_object_or_404(self.queryset, pk=pk)
#       serializer = ProductSerializer(product)
#       product.delete()
#       return Response(serializer.data)



class MarketsView(generics.ListCreateAPIView):
   
   queryset = Market.objects.all()
   serializer_class = MarketSerializer

#    def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)

#    def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)




# @api_view(['GET','POST']) #decorator
# def markets_view(request):
    # if request.method == 'GET':
    #   markets = Market.objects.all()
    #   serializer = MarketHayperlinkedSerializer(markets, many=True,context={'request': request},fields=('id','url','name'))
    #   return Response(serializer.data)
    

    # if request.method == 'POST':
    #    serializer = MarketSerializer(data=request.data)
    #    if serializer.is_valid():
    #       serializer.save()
    #       return Response(serializer.data)
    #    else:
    #       return Response(serializer.errors)







# class MarketsSingleView(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
   
#     queryset = Market.objects.all()
#     serializer_class = MarketSerializer

#     def get(self, request, *args, **kwargs):
#      return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#      return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#      return self.destroy(request, *args, **kwargs)

class MarketsSingleView(generics.RetrieveUpdateDestroyAPIView):
   
     queryset = Market.objects.all()
     serializer_class = MarketSerializer


class SellerOfMarketList(generics.ListCreateAPIView):
   serializer_class = SellerListSerializer

   def get_queryset(self):
       pk = self.kwargs.get('pk')
       market = Market.objects.get(pk = pk)
       return market.sellers.all()

   def perform_create(self, serializer):
      pk = self.kwargs.get('pk')
      market = Market.objects.get(pk = pk)
      serializer.save(markets={market})





# @api_view(['GET', 'DELETE', 'PUT']) #decorator
# def market_single_view(request, pk):

#     if request.method == 'GET':
#       market = Market.objects.get(pk=pk)
#       serializer = MarketSerializer(market,context={'request': request})
#       return Response(serializer.data)
    
#     if request.method == 'PUT':
#       market = Market.objects.get(pk=pk)
#       serializer = MarketSerializer(market, data=request.data, partial=True)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#       else:
#           return Response(serializer.errors)

#     if request.method == 'DELETE':
#        market = Market.objects.get(pk=pk)
#        serializer = MarketSerializer(market)
#        market.delete()
#        return Response(serializer.data)
    
   



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
      serializer = ProductSerializer(products, many = True)
      return Response(serializer.data)
   
   if request.method == 'POST':
       serializer = ProductSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors)
       
       
  
