from django.urls import path

from .views import (
    index,
    TaskTypeListView, TaskTypeCreateView, TaskTypeUpdateView, TaskTypeDeleteView, TaskListView,
    TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, WorkerUpdateView, WorkerDeleteView,
    WorkerDetailView, WorkerCreateView, WorkerListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tast-types/",
        TaskTypeListView.as_view(),
        name="task-types-list",
    ),
    path(
        "tast-types/create/",
        TaskTypeCreateView.as_view(),
        name="task-types-create",
    ),
    path(
        "tast-types/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-types-update",
    ),
    path(
        "tast-types/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-types-delete",
    ),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"
    ),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update",
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),
]

app_name = "taxi"
