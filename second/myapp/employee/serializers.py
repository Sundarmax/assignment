from employee.models import Employee
from rest_framework import serializers

class employeeListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = Employee
        fields  = ('emp_id','emp_name','manager_name')

    def to_representation(self, instance):
        data = super(employeeListSerializer, self).to_representation(instance)
        # check if current employee has a manager or not
        if data['manager_name'] is not None:
            try:
                empIns = Employee.objects.get(emp_id = int(data['manager_name']))
                data['manager_name'] = empIns.emp_name 
            except Exception as e:
                print(e)
                pass

        return data

