from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = get_user_model()
        if not user.objects.filter(email='jin@landcorp.io').exists():
            user.objects.create_superuser(username='chungjin93',
                                          email='jin@landcorp.io',
                                          password='Wjdwls93@')
