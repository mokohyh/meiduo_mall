from rest_framework import serializers

from goods.models import GoodsCategory


class SKUCategorieSerializer(serializers.ModelSerializer):
    """
        商品分类序列化器
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class SKUGoodsSerializer(serializers.Serializer):
    pass
