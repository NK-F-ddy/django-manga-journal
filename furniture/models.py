# furniture/models.py

from django.db import models

# ----------------------------------------
# 1. 家具アイテムモデル (記事一覧に使用)
# ----------------------------------------
# furniture/models.py

from django.db import models

# 満足度の選択肢を定義
RATING_CHOICES = (
    (1, "★☆☆☆☆☆☆☆☆☆ (1/10)"),
    (2, "★★☆☆☆☆☆☆☆☆ (2/10)"),
    (3, "★★★☆☆☆☆☆☆☆ (3/10)"),
    (4, "★★★★☆☆☆☆☆☆ (4/10)"),
    (5, "★★★★★☆☆☆☆☆ (5/10)"),
    (6, "★★★★★★☆☆☆☆ (6/10)"),
    (7, "★★★★★★★☆☆☆ (7/10)"),
    (8, "★★★★★★★★☆☆ (8/10)"),
    (9, "★★★★★★★★★☆ (9/10)"),
    (10, "★★★★★★★★★★ (10/10)"),
)


# ----------------------------------------
# 1. 家具アイテムモデル (記事一覧に使用)
# ----------------------------------------
class Item(models.Model):
    # ... 既存のフィールド ...
    name = models.CharField(max_length=100, verbose_name="家具名")
    type = models.CharField(max_length=50, verbose_name="種類")
    description = models.TextField(verbose_name="説明", blank=True)
    review = models.TextField(
        verbose_name="使ってみた感想",
        blank=True,
        help_text="家具を実際に使用した感想やレビューを記載します。",
    )
    image = models.ImageField(
        verbose_name="家具画像", upload_to="furniture_images/", null=True, blank=True
    )

    # ⬇️ 【新規追加フィールド】

    # 1. 販売中/製造中止の記載欄
    is_discontinued = models.BooleanField(default=False, verbose_name="製造中止")

    # 2. 販売元URLリンクの貼り付け場所
    shop_url = models.URLField(
        max_length=200,
        blank=True,
        verbose_name="販売元URL",
        help_text="販売元のオンラインストアなどのURLを貼り付けてください。",
    )

    # 3. 満足度10段階評価
    rating = models.IntegerField(
        choices=RATING_CHOICES, default=5, verbose_name="満足度評価 (10段階)"
    )

    # ⬆️ 【新規追加フィールド】

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "家具アイテム"


# ----------------------------------------
# 2. 部屋のコーディネート画像モデル (カルーセルに使用)
# ----------------------------------------
class RoomImage(models.Model):
    title = models.CharField(max_length=100, verbose_name="タイトル", blank=True)

    # 部屋全体の画像ファイル
    room_photo = models.ImageField(
        verbose_name="部屋の画像", upload_to="room_photos/", null=False, blank=False
    )
    description = models.TextField(verbose_name="説明", blank=True)

    # カルーセルに表示するかどうかのフラグ
    is_featured = models.BooleanField(default=True, verbose_name="カルーセルに表示する")

    def __str__(self):
        return self.title if self.title else f"部屋の画像 ({self.id})"

    class Meta:
        verbose_name_plural = "部屋のコーディネート画像"
