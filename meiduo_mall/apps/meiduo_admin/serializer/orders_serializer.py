from rest_framework import serializers

from orders.models import OrderInfo


class OrderInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderInfo
        feilds = "__all__"