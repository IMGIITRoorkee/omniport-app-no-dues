from django.urls import path

from no_dues.views.hello_world import HelloWorld

app_name = 'no_dues'

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello_world'),
]
