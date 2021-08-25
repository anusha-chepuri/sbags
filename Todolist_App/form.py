from django import forms
from Todolist_App.models import Tasklist
class Taskform(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields =['task', 'done']
        fields =['task', 'done']