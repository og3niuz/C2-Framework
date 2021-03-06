from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api import views




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'agents', views.AgentViewSet, base_name='agent')
router.register(r'commands', views.CommandViewSet, base_name='command')
router.register(r'complete', views.AgentCommandHistoryViewSet, base_name='complete')
router.register(r'groups', views.GroupViewSet, base_name='group')
router.register(r'log', views.LogViewSet, base_name='log'),
router.register(r'report', views.ReportViewSet, base_name='report')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]