from django.shortcuts import render
from .models import Juego
from .models import Usuario
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from .decorators import check_if
from .forms import RegistroUsuarioForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'juegos/index.html', context)

def browse(request):
    juegos = Juego.objects.all()
    context = {
        'juegos': juegos,
    }
    return render(request, 'juegos/browse.html', context)

def details(request):
    
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Usuario registrado exitosamente"
            return render(request, 'juegos/details.html', {'form': form, 'mensaje': mensaje})
        else:
            # Imprimir los errores del formulario en la consola
            print("Errores del formulario:", form.errors)
            mensaje = "Error al registrar usuario. Por favor, intenta de nuevo."
            return render(request, 'juegos/details.html', {'form': form, 'mensaje': mensaje})
    else:
        form = RegistroUsuarioForm()
        return render(request, 'juegos/details.html', {'form': form})


def profile(request):
    context = {}
    return render(request, 'juegos/profile.html', context)

def streams(request):
    context = {}
    return render(request, 'juegos/streams.html', context)

def crud(request):
    juegos = Juego.objects.all()
    context = {
        'juegos': juegos,
    }
    return render(request, 'juegos/crud.html', context)

def crud_add(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        genero = request.POST.get('genero')
        precio = request.POST.get('precio')
        imagen = request.POST.get('imagen')
        juego = Juego(nombre=nombre, genero=genero, precio=precio, imagen=imagen)
        juego.save()
        context = {
            'mensaje': 'juego agregado correctamente',
        }
        return render(request, 'juegos/crud_add.html', context)
    else:
        context = {}
        return render(request, 'juegos/crud_add.html', context)

def crud_find(request, pk):
    juego = Juego.objects.get(idJuego=pk)
    context = {
        'juego': juego,
    }
    return render(request, 'juegos/crud_edit.html', context)

def crud_edit(request):
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        genero = request.POST.get('genero')
        precio = request.POST.get('precio')
        imagen = request.POST.get('imagen')
        juego = Juego(nombre=nombre, genero=genero, precio=precio, imagen=imagen)
        juego.save()
        juegos = Juego.objects.all()
        context = {
            'mensaje': 'juego editado correctamente',
            'juegos': juegos,
        }
        return render(request, 'juegos/crud.html', context)



def crud_genero(request):
    context = {}
    return render(request, 'juegos/crud_genero.html', context)

def user_add(request):
    context = {}
    return render(request, 'juegos/user_add.html', context)

def user_update(request):
    context = {}
    return render(request, 'juegos/user_update.html', context)

def crud_delete(request, pk):
    juego = Juego.objects.get(idJuego=pk)
    juego.delete()
    juegos = Juego.objects.all()
    context = {
        'mensaje': 'juego eliminado correctamente',
        'juegos': juegos,
    }
    return render(request, 'juegos/crud.html', context)

@user_passes_test(check_if)
def crud_view(request):
    # Lógica del CRUD
    return render(request, 'juegos/crud.html')


    
