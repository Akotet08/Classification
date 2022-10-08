from django import forms

class ImageForm(forms.Form):
    upload_image  = forms.ImageField(widget=forms.TextInput(attrs={'class': 'custom-file-input', 'type':"file", 'name':"upload_image", 'accept':"image/*", 'id':"id_upload_image"}))