from django.db import models


class Student(models.Model):
    """A simple Student model for Quiz #3 (Model -> View -> URL -> Template)."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    year_level = models.PositiveIntegerField(help_text="e.g. 1, 2, 3, 4")

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
