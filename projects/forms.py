from django.forms import ModelForm
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model= Project
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
            
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        for name, feild in self.fields.items():
            feild.widget.attrs.update({'class':'input'})
        
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add a title'})
        
        # self.fields['description'].widget.attrs.update({'class':'input', 'placeholder':'Describe'})

class ReviewForm(ModelForm):
    class Meta:
        model =  Review
        fields = ['value', 'body']
        
        labels = {
            'value': 'Place Your Vote' ,
            'body': 'Add a comment with your vote'
            
        }       
        
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        
        for _, feild in self.fields.items():
            feild.widget.attrs.update({'class':'input'})