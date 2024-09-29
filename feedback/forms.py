from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'experience']
        widgets = {
            'experience': forms.Textarea(attrs={'placeholder': 'Deel uw ervaring hier...'}),
        }
        labels = {
            'name': 'Uw naam (optioneel):',
            'experience': 'Uw ervaring:',
        }
