from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class PermissionSerialzier(serializers.ModelSerializer):
    """
        用户权限表序列化器
    """

    class Meta:
        model = Permission
        fields = "__all__"


class ContentTypeSerialzier(serializers.ModelSerializer):
    '''权限类型序列化器'''

    class Meta:
        model = ContentType
        fields = ('id', 'name')


class GroupSerialzier(serializers.ModelSerializer):
    '''权限组'''
    class Meta:
        model = Group
        fields = ('__all__')

