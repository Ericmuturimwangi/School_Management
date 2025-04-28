from rest_framework.routers import DefaultRouter
from .views import SchoolClassViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'classes', SchoolClassViewSet, basename='schoolclass')
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = router.urls
