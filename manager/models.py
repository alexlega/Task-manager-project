from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        related_name="workers",
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("manager:worker-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    CRITICAL = "P1"
    HIGH = "P2"
    MEDIUM = "P3"
    LOW = "P4"
    TASKS_PRIORITY = [
        (CRITICAL, 'Critical'),
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True
    )
    deadline = models.DateTimeField(null=True)
    # complete_date = models.DateTimeField(null=True)  # added new field
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=2,
        choices=TASKS_PRIORITY,
        default=LOW
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )

    class Meta:
        ordering = ["name"]
        default_related_name = "tasks"

    def get_absolute_url(self):
        return reverse("manager:task-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
