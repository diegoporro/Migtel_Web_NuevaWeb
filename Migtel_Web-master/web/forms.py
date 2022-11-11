from django import forms

CIUDAD = [
    ['Higuerote', 'Higuerote'],
    ['Caracas', 'Caracas'],
    ['Guarenas - Guatire', 'Guarenas - Guatire'],
]

METODOS_PAGO = [
    ['Zelle', 'Zelle'],
    ['Transferencia', 'Transferencia'],
    ['PayPal', 'PayPal'],
]


class ServicioForm(forms.Form):
    Nombres = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}))
    Telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '04141234567'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'algo@gmail.com'}))
    Ciudad = forms.ChoiceField(choices=CIUDAD, widget=forms.Select(attrs={'class': 'form-control'}))
    Zona = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zona'}))
    Direccion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Av principal...', 'style': 'resize: none'}))
    Mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cuerpo del mensaje', 'style': 'resize: none'}))

    def clean(self):
        Nombres = self.cleaned_data.get("Nombres")
        Telefono = self.cleaned_data.get("Telefono")
        Email = self.cleaned_data.get("Email")
        Ciudad = self.cleaned_data.get("Ciudad")
        Zona = self.cleaned_data.get("Zona")
        Direccion = self.cleaned_data.get("Direccion")
        Mensaje = self.cleaned_data.get("Mensaje")

        return super(ServicioForm, self).clean()


class PagoForm(forms.Form):
    Nombres = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}))
    Telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '04141234567'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'algo@gmail.com'}))
    Metodo_de_pago = forms.ChoiceField(choices=METODOS_PAGO, widget=forms.Select(attrs={'class': 'form-control'}))
    Monto = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234'}))
    Numero_de_Confirmacion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '012345'}))
    Fecha = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '01/01/2020', 'style': 'resize: none'}))
    Mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cuerpo del mensaje...', 'style': 'resize: none'}))
    Imagen = forms.ImageField(required=False)

    def clean(self):
        Nombres = self.cleaned_data.get("Nombres")
        Telefono = self.cleaned_data.get("Telefono")
        Email = self.cleaned_data.get("Email")
        Metodo_de_pago = self.cleaned_data.get("Metodo_de_pago")
        Monto = self.cleaned_data.get("Monto")
        Numero_de_Confirmacion = self.cleaned_data.get("Numero_de_Confirmacion")
        Fecha = self.cleaned_data.get("Fecha")
        Mensaje = self.cleaned_data.get("Mensaje")
        Imagen = self.cleaned_data.get("Imagen")

        return super(PagoForm, self).clean()


class ContactForm(forms.Form):
    Nombres = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-6', 'placeholder': 'Nombres'}))
    Telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-6', 'placeholder': '04141234567'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control col-6', 'placeholder': 'algo@gmail.com'}))
    Mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control col-6', 'placeholder': 'Cuerpo del mensaje...', 'style': 'resize: none'}))

    def clean(self):
        Nombres = self.cleaned_data.get("Nombres")
        Telefono = self.cleaned_data.get("Telefono")
        Email = self.cleaned_data.get("Email")
        Mensaje = self.cleaned_data.get("Mensaje")

        return super(ContactForm, self).clean()
