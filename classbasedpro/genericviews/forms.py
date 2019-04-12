from django import forms
class PersonForm(forms.Form):
    name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name',
            }
        )
    )
    desc = forms.CharField(help_text="write a brief about person",
        widget=forms.Textarea(
            attrs={
                    'class':'form-control',
                    'placeholder':'enter description',
            }
        )
    )

