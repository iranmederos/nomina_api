from rest_framework import serializers
from .models import Payroll

class PayrollSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user')
    class Meta:
        model = Payroll
        fields = ('id', 'user', 'payment_date', 'payroll_filename')

    def get_user(self, Payroll):
        return {
            "user_id": Payroll.user.id,
            "user_code_employee": Payroll.user.code_employee,
            "user_full_name": Payroll.user.get_full_name()
        }

