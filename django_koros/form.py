from django import forms
from django_koros.model import students


class EmpForm(forms.ModelForm):
    class Meta:
        model = students
        fields = "__all__"
