"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# Задача 1
# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('product/<int:id>/', views.product_detail, name='product_detail'),
# # ]


# задача 2
# # from django.urls import re_path
# # from . import views

# # urlpatterns = [
# #     re_path(
# #         r'^profile/(?P<username>[a-zA-Z]+)/post/(?P<post_id>\d+)/$',
# #         views.profile_post_view,
# #         name='profile_post'
# #     ),
# # ]


# Задача 3
# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     # Маршрут с двумя параметрами
# #     path('greeting/<str:name>/<str:language>/', views.greeting_view, name='greeting_with_language'),
    
# #     # Маршрут с одним параметром (language будет использовать значение по умолчанию)
# #     path('greeting/<str:name>/', views.greeting_view, name='greeting_default'),
# # ]

