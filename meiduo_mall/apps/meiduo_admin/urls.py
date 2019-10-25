from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url

from meiduo_admin.view.images_view import ImagesView
from meiduo_admin.view.orders_view import OrderInfoView
from meiduo_admin.view.skus_view import SKUCategorieView, SKUGoodsView
from meiduo_admin.view.specs_view import SpecsView
from meiduo_admin.view.statistics_view import UserTotalCountView, UserDayCountView, UserActiveCountView, \
    UserOrderCountView, UserMonthCountView, GoodsDayView
from meiduo_admin.view.user_administration_view import UserView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    # 用户总数
    url(r'^statistical/total_count/$', UserTotalCountView.as_view()),
    # 日增用户
    url(r'^statistical/day_increment/$', UserDayCountView.as_view()),
    # 日活跃用户
    url(r'^statistical/day_active/$', UserActiveCountView.as_view()),
    # 日下单用户
    url(r'^statistical/day_orders/$', UserOrderCountView.as_view()),
    # 月注册量
    url(r'^statistical/month_increment/$', UserMonthCountView.as_view()),
    # 日访问商品量
    url(r'^statistical/goods_day_views/$', GoodsDayView.as_view()),

    #############用户
    url(r'^users/$', UserView.as_view()),


    ################## spu商品信息
    url(r'^goods/simple/$', SpecsView.as_view({'get':'simple'})),

    ################# 图片信息
    url(r'^skus/simple/$', ImagesView.as_view({'get':'simple'})),

]

################ 规格路由
route = DefaultRouter()
route.register('goods/specs', SpecsView, base_name='specs')
urlpatterns += route.urls


############### 图片路由
route = DefaultRouter()
route.register('skus/images', ImagesView, base_name='images')
urlpatterns += route.urls


##############  sku路由
route = DefaultRouter()
route.register('skus', SKUGoodsView, base_name='skus')
urlpatterns += route.urls

##############  订单路由
route = DefaultRouter()
route.register('orders', OrderInfoView, base_name='orders')
urlpatterns += route.urls