import django.http
from django import http
from fdfs_client.client import Fdfs_client

from rest_framework import serializers
from rest_framework.response import Response

from goods.models import SKUImage, SKU
from meiduo_mall.settings.dev import Fdfs_config_path
from celery_tasks.detail_html.tasks import get_detail_html


class ImageSeriazlier(serializers.ModelSerializer):
    # 返回图片关联的sku的id值
    # sku = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SKUImage
        fields = "__all__"



class SKUSeriazlier(serializers.ModelSerializer):
    '''返回sku的id和name'''

    class Meta:
        model = SKU
        fields = ('id', 'name')