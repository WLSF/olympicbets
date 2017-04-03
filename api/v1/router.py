from .users.views import UserViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

api_urlpatterns = router.urls