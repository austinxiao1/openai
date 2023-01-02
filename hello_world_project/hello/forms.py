from django import forms

from hello.models import LogMessage, OpenAIPlay

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)  # NOTE: the trailing comma is required


class OpenAIPlayForm(forms.ModelForm): 
    question = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "question ...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="Question",
    )

    class Meta:
        model = OpenAIPlay
        fields = ("question", "model", "category")  # NOTE: the trailing comma is required