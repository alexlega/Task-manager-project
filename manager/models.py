from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

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
    description = models.TextField()
    deadline = models.DateTimeField(null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=2,
        choices=TASKS_PRIORITY,
        default=LOW
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
