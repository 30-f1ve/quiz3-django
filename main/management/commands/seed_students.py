from django.core.management.base import BaseCommand

from main.models import Student


class Command(BaseCommand):
    help = "Seeds the database with sample Student records for Quiz 3."

    def handle(self, *args, **options):
        sample_students = [
            {
                "first_name": "Janmell",
                "last_name": "Dacallos",
                "email": "janmell.dacallos@gmail.com",
                "course": "BSIT",
                "year_level": 3,
            },
            {
                "first_name": "MellJan",
                "last_name": "Dacallos",
                "email": "melljan.dacallos@gmail.com",
                "course": "BSIT",
                "year_level": 3,
            },
            {
                "first_name": "llemnaJ",
                "last_name": "sollacaD",
                "email": "llemnaj.sollacad@gmail.com",
                "course": "BSIT",
                "year_level": 3,
            },
        ]

        created_count = 0
        for data in sample_students:
            _, created = Student.objects.get_or_create(
                email=data["email"], defaults=data
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeding complete. {created_count} new student record(s) created. "
                f"Total students in database: {Student.objects.count()}."
            )
        )
