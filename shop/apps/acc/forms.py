from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=200)
    file = forms.FileField()
    description = forms.CharField(max_length=400)
    private = forms.BooleanField(required=False)

