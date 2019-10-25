from rest_framework import serializers

from goods.models import SKU
from orders.models import OrderInfo,OrderGoods

class SKUSerializer(serializers.ModelSerializer):
    '''sku序列化器'''
    class Meta:
        model = SKU
        fields = ('name','default_image')



class OrderGoodsSerializer(serializers.ModelSerializer):
    '''订单商品序列化器'''
    sku = SKUSerializer()
    class Meta:
        model = OrderGoods
        fields = ('count','price','sku')



class OrderInfoSerializer(serializers.ModelSerializer):
    '''订单信息序列化器'''

    # 关联嵌套返回 用户表数据和订单商品表数据
    user = serializers.StringRelatedField(read_only=True)
    skus = OrderGoodsSerializer(many=True)
    class Meta:
        model = OrderInfo
        fields = "__all__"