from django import forms

from .models import Apply , job






class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','website','cv','cover_letter']
        labels = {
            'name':'Your Name',
            'email':'Your Email',
            'website':'Your Website',
            'cv':'Your CV',
            'cover_letter':'Cover Letter',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'website': forms.URLInput(attrs={'class':'form-control'}),
            'cv': forms.FileInput(attrs={'class':'form-control'}),
            'cover_letter': forms.Textarea(attrs={'class':'form-control'}),
        }


class jobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('owner','slug',)
        labels = {
            'title':'Title',
            'job_type':'Job Type',
            'description':'Description',
            'published_at':'Published At',
            'vacancy':'Vacancy',
            'salary':'Salary',
            'experience':'Experience',
            'category':'Category',
            'image':'Image',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'job_type': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'published_at': forms.DateTimeInput(attrs={'class':'form-control'}),
            'vacancy': forms.NumberInput(attrs={'class':'form-control'}),
            'salary': forms.NumberInput(attrs={'class':'form-control'}),
            'experience': forms.NumberInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }