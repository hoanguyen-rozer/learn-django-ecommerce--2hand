from django.urls import path

from .views import AccountHomeView
from product.views import UserProductHistoryView

app_name = 'accounts' 

urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
    path('history/products/', UserProductHistoryView.as_view(), name='history'),
]