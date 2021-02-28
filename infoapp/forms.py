from django import forms
from infoapp.models import Student

class StudentForm(forms.ModelForm):
    def clean_marks(self):
        inputmarks=self.cleaned_data['marks']
        if inputmarks>100:
            raise forms.ValidationError('Marks should be less than 100')
        return inputmarks
    def clean_name(self):
        inputname=self.cleaned_data['name']
        bool=inputname.isalpha()
        if bool==False:
            raise forms.ValidationError('name should not contain other than alphabetics')
        return inputname
    class Meta:
        model=Student
        fields='__all__'
