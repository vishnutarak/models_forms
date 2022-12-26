from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpadeForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'

class AccessRecordsForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'

