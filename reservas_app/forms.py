from django import forms
from reservas_app.models import Reservas
import datetime


estados = [
    ('Reservado', 'Reservado'),
    ('Completado', 'Completado'),
    ('Anulado', 'Anulado'),
    ('No Asiste','No asiste')
]

class FormReservas(forms.ModelForm):
    nombre = forms.CharField(label="Nombre Cliente")
    telefono = forms.CharField(label="Numero Celular Cliente")
    fechaReserva = forms.DateField(initial=datetime.date.today, label="Fecha Reserva")
    horaReserva = forms.TimeField(initial=datetime.time, label="Hora Reserva")
    cantidadClientes = forms.IntegerField(label="Cantidad Clientes",max_value=15,min_value=1)
    email = forms.EmailField(label="E-Mail")
    estadoReserva = forms.ChoiceField(choices=estados, label="Estado Actual")
    observacion = forms.CharField(label="Observaciones", required=False, widget=forms.Textarea)

    class Meta:
        model = Reservas
        fields = ['nombre','telefono','fechaReserva','horaReserva','cantidadClientes','email','estadoReserva','observacion']

    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fechaReserva.widget.attrs['class'] = 'form-control'
    horaReserva.widget.attrs['class'] = 'form-control'
    cantidadClientes.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    estadoReserva.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'