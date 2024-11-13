from django.urls import path
from .views import MarketsSingleView, products_view,sellers_view,seller_single_view,MarketsView,SellerOfMarketList

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketsSingleView.as_view() , name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', sellers_view),
    path('product/', products_view),
    path('seller/<int:pk>/', seller_single_view, name='seller_single')
]