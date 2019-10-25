from rest_framework.viewsets import ReadOnlyModelViewSet

from meiduo_admin.serializer.orders_serializer import OrderInfoSerializer
from meiduo_admin.utils import UserPageNum
from orders.models import OrderInfo



class OrderInfoView(ReadOnlyModelViewSet):

    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializer
    pagination_class = UserPageNum