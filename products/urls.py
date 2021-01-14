#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2021-01-13 22:51
# software: PyCharm

from django.urls import path
from .views import ProductViewSet, UserApi

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserApi.as_view())
]
