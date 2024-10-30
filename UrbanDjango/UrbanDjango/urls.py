"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from task2.views import index, Index2
# from task3.views import platform, games, cart
# from task4.views import platform, games, cart
from task5.views import  sign_up_by_html, sign_up_by_django


# urlpatterns = [                                               # task2
#     path('admin/', admin.site.urls),
#     path('', index),
#     path('2/', Index2.as_view())
# ]

# urlpatterns = [                                                  # task3
#     path('admin/', admin.site.urls),
#     path('', platform, name='platform'),
#     path('games/', games, name='games'),
#     path('cart/', cart, name='cart')
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  sign_up_by_html),
    path('2/', sign_up_by_django),
]