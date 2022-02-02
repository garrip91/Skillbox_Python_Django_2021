from rest_framework import routers
from .api import UserViewSet



router = routers.DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls