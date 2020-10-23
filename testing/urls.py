from django.urls import path

from testing.views.index import index
from testing.views.query_params import query_params_views

urlpatterns = (
    path('', index, name='profiles'),
    path('query_params/', query_params_views, name='query params'),
)