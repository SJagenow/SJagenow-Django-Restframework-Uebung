from django.urls import path, include
from .views import MarketsSingleView, ProductViewSet, SellerViewSet, products_view,sellers_view,seller_single_view,MarketsView,SellerOfMarketList
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'sellerss', SellerViewSet)

urlpatterns = [
    path('', include(router.urls)) ,
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketsSingleView.as_view() , name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', sellers_view),
    path('product/', products_view),
    path('seller/<int:pk>/', seller_single_view, name='seller-detail')
]