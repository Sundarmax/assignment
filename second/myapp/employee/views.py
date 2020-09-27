# Imports from core django rest framework  
from rest_framework.decorators import action,api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly
    )
from rest_framework import status,views
from rest_framework.response import Response

# Imports from employee app.
from employee.models import Employee
from employee.serializers import employeeListSerializer

# Function based view in DRF
@api_view(['GET'])
@permission_classes((AllowAny,))
def get_employee_data(request):
    if request.method == 'GET':
        employeeIns = Employee.objects.all()
        serializer  = employeeListSerializer(employeeIns,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
