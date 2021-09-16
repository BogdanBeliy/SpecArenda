from django.urls import path
from .views import AdsByCategory, CatigoriesView, OrganisationDetailView


urlpatterns = [
    path('organisation/<slug:slug>/', OrganisationDetailView.as_view(), name='org_detail'),
    path('category/<slug:slug>/', AdsByCategory.as_view(), name='ad_by_category'),
    path('', CatigoriesView.as_view(), name='parent_category'),
]
