from django.shortcuts import render,redirect
from reservas_app.models import Reservas
from reservas_app.forms import FormReservas

# Create your views here.
def index(request):
    data = {"profile":"profile.png"}
    return render(request, 'index.html',data)

def listaReserva(request):
    reservas = Reservas.objects.all()
    data = {'reservas': reservas}
    return render(request,"lista.html",data)

def eliminarReserva(request, IN_id):
    reservas = Reservas.objects.get(id = IN_id)
    reservas.delete()
    return redirect('/reservas')

def agregarReserva(request):
    form = FormReservas()
    if (request.method == 'POST'):
        form = FormReservas(request.POST)
        if (form.is_valid()):
            form.save()
        return redirect('/reservas')
    data = {'form':form}
    return render(request,'agregar.html', data)

def modificarReserva(request, IN_id):
    proyecto = Reservas.objects.get(id = IN_id)
    form = FormReservas(instance=proyecto)

    if (request.method == 'POST'):
        form = FormReservas(request.POST, instance=proyecto)
        if (form.is_valid()):
            form.save()
        return redirect('/reservas')
    data = {'form': form}
    return render (request, 'agregar.html', data)