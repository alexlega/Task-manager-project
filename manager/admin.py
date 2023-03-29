from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Worker, Task, TaskType, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "is_completed", "deadline"]
    list_filter = ("name",)
    search_fields = ("name",)


admin.site.register(TaskType)
admin.site.register(Position)
