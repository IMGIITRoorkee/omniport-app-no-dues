from django.urls import path, include
from rest_framework import routers


from no_dues.views.permission import PermissionViewset
from no_dues.views.profile import ProfileView
from no_dues.views.comments import PermissionCommentViewSet
from no_dues.views.subscriber_detail import SubscriberListView
from no_dues.views.subscriber_detail import SubscriberDetailView
from no_dues.views.mass_permission_status_update import (
    MassPermissionStatusUpdate
)
from no_dues.views.select_authorities import SelectAuthorities

app_name = 'no_dues'

router = routers.SimpleRouter()
router.register(r'permission', PermissionViewset, basename='permission')
router.register(r'comment', PermissionCommentViewSet, basename='comment')


urlpatterns = [
    path('', include(router.urls)),
    path('profile/', ProfileView.as_view()),
    path('subscriber/', SubscriberListView.as_view()),
    path('subscriber/<str:enrolment_number>/', SubscriberDetailView.as_view()),
    path('update_status/', MassPermissionStatusUpdate.as_view()),
    path('select_authorities/', SelectAuthorities.as_view()),
]
