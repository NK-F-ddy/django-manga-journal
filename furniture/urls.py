# furniture/urls.py

from django.urls import path
from . import views
# views.pyで定義した ItemDetailView を使うために、それをインポートしている views から参照します

urlpatterns = [
    # 1. 一覧表示（トップページ）: / にアクセス
    path('', views.item_list, name='item_list'),
    
    # 2. 詳細表示: /item/1/, /item/2/ のようにアクセス (新規追加)
    # <int:pk> はプライマリーキー（ID）を受け取るためのパスコンバーターです
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
]
