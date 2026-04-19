"""
Create or update the initial admin user for the CMS panel.

Usage (production — credentials from environment):
    export SMM_ADMIN_USERNAME=owner
    export SMM_ADMIN_EMAIL=owner@example.org
    export SMM_ADMIN_PASSWORD='a-long-random-passphrase'
    python manage.py create_admin

Usage (one-off, explicit):
    python manage.py create_admin --username owner --email owner@example.org --password secret

If the user already exists, their password and staff/superuser flags are
refreshed — this is idempotent and safe to re-run on every deploy.
"""
import os
import secrets
import string
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create or update the CMS admin user (idempotent).'

    def add_arguments(self, parser):
        parser.add_argument('--username', default=os.environ.get('SMM_ADMIN_USERNAME'))
        parser.add_argument('--email',    default=os.environ.get('SMM_ADMIN_EMAIL'))
        parser.add_argument('--password', default=os.environ.get('SMM_ADMIN_PASSWORD'))
        parser.add_argument('--generate-password', action='store_true',
                            help='Generate a strong random password and print it once.')

    def handle(self, *args, **opts):
        User = get_user_model()

        username = opts['username']
        email    = opts['email'] or ''
        password = opts['password']

        if not username:
            raise CommandError('Provide --username or set SMM_ADMIN_USERNAME.')

        if opts['generate_password'] or not password:
            if opts['generate_password']:
                password = _gen_password()
                self.stdout.write(self.style.WARNING(
                    f'Generated password (save this — it will not be shown again): {password}'
                ))
            else:
                raise CommandError(
                    'Provide --password, set SMM_ADMIN_PASSWORD, or pass --generate-password.'
                )

        user, created = User.objects.get_or_create(username=username, defaults={'email': email})
        user.email = email or user.email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        verb = 'created' if created else 'updated'
        self.stdout.write(self.style.SUCCESS(f'[OK] Admin user {verb}: {username}'))


def _gen_password(n=20):
    alpha = string.ascii_letters + string.digits + '!@#$%^&*-_+='
    return ''.join(secrets.choice(alpha) for _ in range(n))
