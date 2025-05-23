from django.urls import path
from .views import check_login, register, get_account_balance, api_buy_asset, api_sell_asset, get_holdings, get_user_account_info


urlpatterns = [
    path('check_login/', check_login, name='check_login'),
    path('register/',     register,    name='register'),
    path('get_account_balance/', get_account_balance, name='get_account_balance'),
    path('buy/', api_buy_asset, name='buy_asset'),    
    path('sell/', api_sell_asset, name='sell_asset'),
    path('get_holdings/', get_holdings, name='get_holdings'),
    path('get_user_account_info/', get_user_account_info, name = 'get_user_account_info'),
]