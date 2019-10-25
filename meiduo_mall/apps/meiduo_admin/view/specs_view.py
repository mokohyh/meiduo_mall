from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SPUSpecification, SPU
from meiduo_admin.serializer.specs_serializer import SPUSpecificationSerializer, SPUSerializer
from meiduo_admin.utils import UserPageNum


class SpecsView(ModelViewSet):
    """商品的增删查改"""
    # 指定序列化器查询集和分页
    serializer_class = SPUSpecificationSerializer
    queryset = SPUSpecification.objects.all()
    pagination_class = UserPageNum

    def simple(self,request):
        spus = SPU.objects.all()
        ser = SPUSerializer(spus,many=True)
        return Response(ser.data)


