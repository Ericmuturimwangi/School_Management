from rest_framework.routers import DefaultRouter
from .views import SchoolClassViewSet, AttendanceViewSet, ResultViewSet, generate_performance_report
from django.urls import path

router = DefaultRouter()
router.register(r'classes', SchoolClassViewSet, basename='schoolclass')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'results', ResultViewSet, basename='results')

urlpatterns = router.urls

urlpatterns = router.urls + [
    path('performance_report/', generate_performance_report, name='performance_report'),
]