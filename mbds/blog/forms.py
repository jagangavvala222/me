from django import forms
class EmailForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)#may be comments or maynot be comments so comment required=False

#comments form sections
from blog.models import comments
class commentform(forms.ModelForm):
    class Meta:
        model=comments
        fields=('name','email','body')

from blog.models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
