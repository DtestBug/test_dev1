from django.urls import path
from pets import views

from rest_framework.routers import SimpleRouter, DefaultRouter


# 定义路由对象
router = DefaultRouter()


# router.register(r'pets/', views.PetsViewSet)
urlpatterns = [
    # 创建，list查询
    path('pets/', views.PetsViews.as_view()),

    # 单个查询，删除，更新需要加上内有字段（必须是唯一，id优先）
    path('pets/<name>', views.PetsView.as_view())
]
urlpatterns += router.urls