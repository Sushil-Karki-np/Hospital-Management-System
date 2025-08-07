from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)

urlpatterns = router.urls
