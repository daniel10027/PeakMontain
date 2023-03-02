from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from peak.views import Home, my_view

schema_view = get_swagger_view(title='Pastebin API')

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/routers', include((router.urls))),
    path('api/docs/', schema_view, name="doc"),
    path('api-auth/', include('rest_framework.urls')),
    path('home/api/', include(("peak.urls"))),
    path('home/', Home,name="home"),
    path('', my_view,name="my_view"),
]
