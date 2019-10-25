from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from meiduo_admin.serializer.orders_serializer import OrderInfoSerializer
from meiduo_admin.utils import UserPageNum
from orders.models import OrderInfo



class OrderInfoView(ReadOnlyModelViewSet):

    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializer
    pagination_class = UserPageNum


    # 修改订单的方法
    @action(methods=['put'], detail=True)
    def status(self,request,pk):
        # 获取订单对象
        order = self.get_object()
        # 获取status
        status = request.data.get('status')
        # 修改订单状态
        order.status = status
        order.save()
        # 返回结果
        ser = self.get_serializer(order)
        return Response({
            'order_id': order.order_id,
            'status': status
        })