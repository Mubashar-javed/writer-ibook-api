import random

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from ibook.enums import ProjectStatus
from ibook.models import Project


class Command(BaseCommand):
    help = "Generate dummy project data for local development"

    def handle(self, *args, **kwargs):
        user = get_user_model().objects.first()
        if not user:
            user = get_user_model().objects.create_superuser(
                username="admin", email="admin@example.com", password="testing321"
            )
            self.stdout.write(
                self.style.SUCCESS(f"User created with username: {user.username}")
            )

        for i in range(100):
            project = Project.objects.create(
                title=f"Dummy Project {i+1}",
                content="This is a dummy project for local development.",
                status=random.choice(ProjectStatus.choices)[0],
                author=user,
            )
            self.stdout.write(
                self.style.SUCCESS(f"Dummy project {i+1} created with ID: {project.id}")
            )

        self.stdout.write(
            self.style.SUCCESS("Dummy project data generated successfully!")
        )
