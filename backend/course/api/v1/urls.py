from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("recording", RecordingViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("event", EventViewSet)
router.register("group", GroupViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("lesson", LessonViewSet)
router.register("category", CategoryViewSet)
router.register("module", ModuleViewSet)
router.register("course", CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
