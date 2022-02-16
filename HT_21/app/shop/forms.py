from django import forms


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EditProduct(forms.Form):

    name = forms.CharField(max_length=200, widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    sku = forms.CharField(widget=forms.NumberInput())
    price = forms.DecimalField(max_digits=9, decimal_places=2, widget=forms.NumberInput())
