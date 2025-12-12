# furniture/views.py

from django.shortcuts import render
# DetailViewをインポートするために、views.genericから必要なクラスをインポートします
from django.views.generic import DetailView 
from .models import Item, RoomImage

## ---------------------------------------------
## 1. 一覧表示用ビュー (既存の関数を維持)
## ---------------------------------------------
def item_list(request):
    # 家具アイテムのリスト (記事一覧用)
    items = Item.objects.all()

    # カルーセルに表示する部屋の画像をすべて取得
    room_images = RoomImage.objects.filter(is_featured=True).order_by("id")

    # テンプレートに渡す辞書データ（コンテキスト）
    context = {"items": items, "room_images": room_images}

    return render(request, "furniture/item_list.html", context)

## ---------------------------------------------
## 2. 詳細表示用ビュー (新規追加)
## ---------------------------------------------
class ItemDetailView(DetailView):
    # どのモデルのデータを扱うか指定
    model = Item
    
    # 使用するテンプレートファイル名を指定
    # (このテンプレートファイルは別途作成が必要です: furniture/item_detail.html)
    template_name = 'furniture/item_detail.html'
    
    # テンプレート内でオブジェクトにアクセスする際に使用する変数名を指定
    # テンプレート内では {{ item }} としてアクセスできます
    context_object_name = 'item'
