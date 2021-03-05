from django.forms import ModelForm, CheckboxSelectMultiple
from app.models import Task, Schedule

class TaskForm(ModelForm):
    class Meta:
        model = Task
        labels = {
            "title" : "Task ",
            "page" : "Page ",
            "subject" : "Subject ",
            "week" : "Week ",
        }
        fields = ['title' , 'page', 'subject', 'week']

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        labels = {
            "monday" : "Monday",
            "tuesday" : "Tuesday",
            "wednesday" : "Wednesday",
            "thursday" : "Thursday",
            "friday" : "Friday",
            "saturday" : "Saturday",
        }
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        widgets = {
            'monday': CheckboxSelectMultiple,
            'tuesday': CheckboxSelectMultiple,
            'wednesday': CheckboxSelectMultiple,
            'thursday': CheckboxSelectMultiple,
            'friday': CheckboxSelectMultiple,
            'saturday': CheckboxSelectMultiple,
        }