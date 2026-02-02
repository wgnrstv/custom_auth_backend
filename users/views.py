from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserUpdateSerializer
from .permissions import HasResourcePermission

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UserUpdateSerializer
        return UserSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

class MockFinancialDataView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, HasResourcePermission]
    required_resource = 'FinancialData'
    required_permission = 'view'

    def get(self, request):
        return Response({
            "message": "Access granted to Financial Data",
            "data": [
                {"id": 1, "balance": 1000, "currency": "USD"},
                {"id": 2, "balance": 500, "currency": "EUR"}
            ]
        })

class MockAdminRuleManagementView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, HasResourcePermission]
    required_resource = 'RulesManagement'
    required_permission = 'edit'

    def post(self, request):
        return Response({"message": "Rules updated by Admin"})
