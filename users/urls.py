from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, ProfileView,
    MockFinancialDataView, MockAdminRuleManagementView
)

urlpatterns = [
    # Auth & Profile
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Business Logic (Mock-objects)
    path('business-data/', MockFinancialDataView.as_view(), name='business_data'),
    path('admin/manage-rules/', MockAdminRuleManagementView.as_view(), name='manage_rules'),
]
