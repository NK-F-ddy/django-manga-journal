# my_furniture_site/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # ルートパス ('') にアクセスがあったら furniture/urls.py に処理を任せる
    path("", include("furniture.urls")),
]

# 開発環境 (DEBUG=True) でユーザーアップロードファイル (MEDIA) を提供する設定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
