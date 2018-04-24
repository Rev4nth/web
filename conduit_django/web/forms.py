from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(
            max_length='200',
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    about = forms.CharField(
            max_length='200',
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            required=False,
        )
    content = forms.CharField(
            widget=forms.Textarea(attrs={'class': 'form-control'})
        )
