from rest_framework.routers import DefaultRouter
from .views import SchoolClassViewSet, AttendanceViewSet, ResultViewSet

router = DefaultRouter()
router.register(r'classes', SchoolClassViewSet, basename='schoolclass')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'results', ResultViewSet, basename='results')

urlpatterns = router.urls
