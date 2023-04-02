from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from manager.models import Worker, Task, Position


# class ListWidget(forms.Textarea):
#     def __init__(self, *args, **kwargs):
#         self.new_item_text = kwargs.pop('new_item_text', 'Add a new item')
#         super().__init__(*args, **kwargs)
#
#     def render(self, name, value, attrs=None, renderer=None):
#         if value is None:
#             value = ''
#         output = '<ul>'
#         for line in value.split('\n'):
#             output += f'<li>{line.strip()}</li>'
#         output += '</ul>'
#         output += f'<input type="text" placeholder="{self.new_item_text}">'
#         return output


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


    # description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Task
        fields = "__all__"

    def save(self, commit=True):
        task = super().save(commit=False)
        if commit:
            task.save()
            self.save_m2m()
        return task


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
        )


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["first_name", "last_name", "position", "email"]


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by task..."})
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by task type..."})
    )


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by position..."})
    )


class NewWorkerForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewWorkerForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
