from django import http
from fdfs_client.client import Fdfs_client
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.serializer.images_serializer import ImageSeriazlier, SKUSeriazlier

from meiduo_admin.utils import UserPageNum
from meiduo_mall.settings.dev import Fdfs_config_path
from celery_tasks.detail_html.tasks import get_detail_html



class ImagesView(ModelViewSet):
    queryset = SKUImage.objects.all()
    serializer_class = ImageSeriazlier
    pagination_class = UserPageNum
    permission_classes = [IsAdminUser]

    def simple(self,request):
        data = SKU.objects.all()
        ser = SKUSeriazlier(data, many=True)
        return Response(ser.data)



    # 重写create方法
    def create(self,request, *args, **kwargs):
        '''保存图片'''
        # 获取前端的信息，图片
        image = request.FILES.get('image')
        # 创建连接对象,导入fdfs的配置文件
        client = Fdfs_client(Fdfs_config_path)
        # 向fastdfs系统上传图片
        ret = client.upload_by_buffer((image.read()))
        # 判断是否上传成功
        if ret['Status'] != 'Upload successed.':
            return http.HttpResponseBadRequest('上传失败')
        # 获取上传后路径
        image_url = ret['Remote file_id']
        # 获取sku_id
        sku_id = int(request.data.get('sku')[0])
        # 保存路径到图片表中
        sku = SKU.objects.get(id=sku_id)
        img = SKUImage.objects.create(sku=sku, image=image_url)

        # 生成新的详情页页面
        get_detail_html.delay(img.sku.id)
        # 响应结果
        return Response(
            {
                'id': img.id,
                'sku': sku_id,
                'image': img.image.url
            },
            status=201  # 前端需要接受201状态
        )