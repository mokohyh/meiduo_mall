from rest_framework import serializers

from goods.models import SKUImage, SKU


class ImageSeriazlier(serializers.ModelSerializer):
    # 返回图片关联的sku的id值
    sku = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SKUImage
        fields = ('sku', 'image', 'id')


class SKUSeriazlier(serializers.ModelSerializer):
    '''返回sku的id和name'''

    class Meta:
        model = SKU
        fields = ('id', 'name')