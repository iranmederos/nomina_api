# images/management/commands/createsu.py

# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from authentication.models import CustomUser, Roles


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(username='admin').exists():
            role = Roles.objects.create(
                rol_name = 'Administrador'
            )
 
            CustomUser.objects.create_superuser(
                code_employee=1221,
                username='1221', 
                password='1234',
                identification_card='VGO134ZG10JH39JVGUK7',
                rfc_equivalet='91NVAI9YUGGXDDA5',
                nss='65HJ6041RDKKJHKOVF94',
                first_name='Yuridia',
                last_name='Salazar',
                email='iran.mederos@syncronik.team',
                date_start='2021-01-01',
                rol=role
            )
        print('Superuser has been created with all field requireds.') 
