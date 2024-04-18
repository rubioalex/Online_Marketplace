from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "name", "description", "price", "image")
        
        widgets = {
            'category': forms.Select(attrs={
                'class': 'newitem-field'
            }),
            
            'name': forms.TextInput(attrs={
                'class': 'newitem-field'
            }),
            
            'description': forms.Textarea(attrs={
                'class': 'newitem-field'
            }),
            
            'price': forms.TextInput(attrs={
                'class': 'newitem-field'
            }),
            
            'image': forms.FileInput(attrs={
                'class': 'newitem-field',
                'id': 'newitem-image-field'
            }),
        }
        

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "image", "is_sold")
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'newitem-field'
            }),
            
            'description': forms.Textarea(attrs={
                'class': 'newitem-field'
            }),
            
            'price': forms.TextInput(attrs={
                'class': 'newitem-field'
            }),
            
            'image': forms.FileInput(attrs={
                'class': 'newitem-field',
                'id': 'newitem-image-field'
            }),
        }