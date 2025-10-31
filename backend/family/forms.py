from django import forms
from .models import Person
from django.core.exceptions import ValidationError



class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        instance = self.instance  # The Person object being edited

        spouses = cleaned_data.get('spouses', [])
        parents = cleaned_data.get('parents', [])

        # Prevent self from being added as a spouse
        if instance.pk and instance in spouses:
            raise ValidationError("فرد نمی‌تواند همسر خود باشد.")

        # Prevent self from being added as a parent
        if instance.pk and instance in parents:
            raise ValidationError("فرد نمی‌تواند والد خود باشد.")

        return cleaned_data