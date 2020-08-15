from .models import *
from django import forms


class FormSessionPlan(forms.Form):
    choices = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        label="Add lifts"
    )

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.fields['choices'].queryset = get_user_lifts_unique(request=args[0])
