from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializer.permission_servializer import PermissionSerialzier, ContentTypeSerialzier, GroupSerialzier
from meiduo_admin.utils import UserPageNum


class PermissionView(ModelViewSet):
    serializer_class = PermissionSerialzier
    queryset = Permission.objects.all()
    pagination_class = UserPageNum

    # 获取权限类型数据
    def content_types(self, request):
        content = ContentType.objects.all()
        ser = ContentTypeSerialzier(content, many=True)
        return Response(ser.data)



class GroupView(ModelViewSet):
    serializer_class = GroupSerialzier
    queryset = Group.objects.all()
    pagination_class = UserPageNum

    def simple(self,request):
        data = Group.objects.all()
        ser = GroupSerialzier(data, many=True)
        return Response(ser.data)