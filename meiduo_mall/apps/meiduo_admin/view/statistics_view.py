from datetime import date, datetime, timedelta

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import GoodsVisitCount
from meiduo_admin.serializer.statistics_serializer import GoodsSerializer
from users.models import User


class UserTotalCountView(APIView):
    '''用户总数统计'''

    def get(self, request):
        # 获取当天的日期
        now_date = date.today()
        # 查询所有的用户
        count = User.objects.all().count()
        return Response({
            "count": count,
            "date": now_date
        })


class UserDayCountView(APIView):
    '''日增用户量'''

    def get(self, request):
        # 获取当天的日期
        now_date = date.today()
        # 查询所有的用户
        count = User.objects.filter(date_joined__gte=now_date).count()
        return Response({
            "count": count,
            "date": now_date
        })



class UserActiveCountView(APIView):
    '''日活跃量'''
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当天的日期
        now_date = date.today()
        # 获取当日登录用户数量  last_login记录最后登录时间
        count = User.objects.filter(last_login__gte=now_date).count()
        return Response({
            "count": count,
            "date": now_date
        })


class UserOrderCountView(APIView):
    '''下单用户'''
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当天的日期
        now_date = date.today()
        # 获取今天下单用户数量  last_login记录最后登录时间
        count = len(set(User.objects.filter(orders__create_time__gte=now_date)))
        return Response({
            "count": count,
            "date": now_date
        })


class UserMonthCountView(APIView):
    '''获取月增用户'''
    #指定管理权限、
    permission_classes = [IsAdminUser]

    def get(self, reuqest):
        # 获取当前日期
        now_date = datetime.today()

        # 获取一个月以前的日期
        start_date = now_date - timedelta(days=29)

        # 创建空列表保存每天的用户量
        date_list = []
        # 循环获取每一天的用户量
        for i in range(30):
            index_date = start_date + timedelta(days=i)
            # 指定下一天日期
            next_date = start_date + timedelta(days=i+1)
            # 查询出当天注册的人数
            count = User.objects.filter(date_joined__gte=index_date, date_joined__lt=next_date).count()

            date_list.append({
                'count':count,
                'date' : index_date
            })
        return Response(date_list)


class GoodsDayView(APIView):
    '''日分类访问量'''
    def get(self,request):
        # 获取当天日期
        now_date = datetime.today()
        # 获取当天访问的商品分类的数量的信息
        data = GoodsVisitCount.objects.filter(date=now_date)
        # 序列化器返回数量
        ser = GoodsSerializer(data, many=True)

        return Response(ser.data)