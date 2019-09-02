from django import forms

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50) # 텍스트 입력form
    #file = forms.FileField()
    image = forms.ImageField()