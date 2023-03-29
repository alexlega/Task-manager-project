from django.urls import path

from .views import (
    index, WorkerListView, TaskListView, TaskTypeListView, PositionListView, WorkerCreateView, WorkerDetailView,
    WorkerDeleteView, WorkerUpdateView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView,
    PositionCreateView, PositionDetailView, PositionDeleteView, TaskTypeCreateView, TaskTypeDetailView,
    TaskTypeDeleteView,

    # TaskTypeListView, TaskTypeCreateView, TaskTypeUpdateView, TaskTypeDeleteView, TaskListView,
    # TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, WorkerUpdateView, WorkerDeleteView,
    # WorkerDetailView, WorkerCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "task-types/",
        TaskTypeListView.as_view(),
        name="task-type-list",
    ),
    # path(
    #     "task-types/create/",
    #     TaskTypeCreateView.as_view(),
    #     name="task-types-create",
    # ),
    # path(
    #     "task-types/<int:pk>/update/",
    #     TaskTypeUpdateView.as_view(),
    #     name="task-types-update",
    # ),
    # path(
    #     "task-types/<int:pk>/delete/",
    #     TaskTypeDeleteView.as_view(),
    #     name="task-types-delete",
    # ),
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
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "posiitions/create/",
        PositionCreateView.as_view(),
        name="position-create",
    ),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
    path(
        "task-types/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create",
    ),
    path(
        "task-types/<int:pk>/",
        TaskTypeDetailView.as_view(),
        name="task-type-detail",
    ),
    path(
        "task-types/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
]

app_name = "taxi"
