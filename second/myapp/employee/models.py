from django.db import models

class Employee(models.Model):

    emp_id          = models.IntegerField(primary_key=True)
    emp_name        = models.CharField(max_length=155)
    manager_name    = models.ForeignKey('self',related_name='employee_manager',on_delete=models.CASCADE ,blank=True,null=True)

    def __str__(self):
        return self.emp_name
