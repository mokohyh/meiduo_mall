from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from goods.models import GoodsCategory
from meiduo_admin.serializer.skus_serializer import SKUGoodsSerializer, SKUCategorieSerializer
from meiduo_admin.utils import UserPageNum


class SKUCategorieView(ListAPIView):

    serializer_class = SKUCategorieSerializer
    # 根据数据存储规律parent_id大于37为三级分类信息，查询条件为parent_id__gt=37
    queryset = GoodsCategory.objects.filter(parent_id__gt=37)

class SKUGoodsView(ModelViewSet):

    # 指定序列化器
    serializer_class = SKUGoodsSerializer
    # 指定分页器 进行分页返回
    pagination_class = UserPageNum
    # 重写get_queryset方法，判断是否传递keyword查询参数