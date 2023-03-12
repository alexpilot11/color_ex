"""color_ex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from colors import views as color_views
from . import views


router = routers.DefaultRouter()
router.register(r'experiments', color_views.ExperimentViewSet)
router.register(r'answers', color_views.AnswerViewSet)
router.register(r'questions', color_views.QuestionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'colors'))),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    re_path(r'^.*/?$', views.catchall),
]
