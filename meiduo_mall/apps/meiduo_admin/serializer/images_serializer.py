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

    def create(self, validated_data):
        request = self.context.get('request')
        # 获取前端的信息，图片
        image = request.FILES.get('image')
        # 创建连接对象,导入fdfs的配置文件
        client = Fdfs_client(Fdfs_config_path)
        # 向fastdfs系统上传图片
        ret = client.upload_by_buffer((image.read()))
        # 判断是否上传成功
        if ret['Status'] != 'Upload successed.':
            raise serializers.ValidationError({'error':'图片上传失败'})
        # 获取上传后路径
        image_url = ret['Remote file_id']
        # # 获取sku_id
        # sku_id = int(request.data.get('sku')[0])
        # sku = ser.validated_data['sku']
        # 保存路径到图片表中
        img = SKUImage.objects.create(sku=validated_data['sku'], image=image_url)

        # 生成新的详情页页面
        get_detail_html.delay(img.sku.id)

        return img


    def update(self, instance, validated_data):
        request = self.context.get('request')
        # 获取前端的信息，图片
        image = request.FILES.get('image')
        # 创建连接对象,导入fdfs的配置文件
        client = Fdfs_client(Fdfs_config_path)
        # 向fastdfs系统上传图片
        ret = client.upload_by_buffer((image.read()))
        # 判断是否上传成功
        if ret['Status'] != 'Upload successed.':
            raise serializers.ValidationError({'error': '图片上传失败'})
        # 获取上传后路径
        image_url = ret['Remote file_id']
        # # 获取sku_id
        # sku_id = int(request.data.get('sku')[0])
        # sku = ser.validated_data['sku']
        # 更新操作图片表中
        instance.image=image_url
        instance.save()

        # 生成新的详情页页面
        get_detail_html.delay(instance.sku.id)

        return instance



class SKUSeriazlier(serializers.ModelSerializer):
    '''返回sku的id和name'''

    class Meta:
        model = SKU
        fields = ('id', 'name')