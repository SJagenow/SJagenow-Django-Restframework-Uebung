from django.urls import path
from .views import markets_view, market_single_view, products_view,sellers_view,seller_single_view,MarketsView

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', market_single_view , name='market-detail'),
    path('seller/', sellers_view),
    path('product/', products_view),
    path('seller/<int:pk>/', seller_single_view, name='seller_single')
]