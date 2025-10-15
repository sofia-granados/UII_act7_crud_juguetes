from django.shortcuts import render, redirect, get_object_or_404
from .models import Juguetes

# Create your views here.
# Listar estudiantes
def index(request):
    juguetes = Juguetes.objects.all()
    return render(request, 'listar_juguetes.html', {'juguetes': juguetes})

def ver_juguetes(request, id):
    juguetes = get_object_or_404(Juguetes, id=id) 
    return render(request, 'ver_juguetes.html', {'juguete': juguetes}) 

# Agregar juguete
def agregar_juguetes(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria = request.POST['categoria'] 
        garantia = request.POST['garantia'] 
        reseña = request.POST['reseña'] 
        precio = request.POST['precio'] 
        Juguetes.objects.create(nombre=nombre, categoria=categoria, garantia=garantia, reseña=reseña, precio=precio)
        return redirect('inicio') 
    return render(request, 'agregar_juguetes.html') 

# Editar juguete
def editar_juguetes(request, id):
    juguetes = get_object_or_404(Juguetes, id=id) 
    if request.method == 'POST':
        juguetes.nombre = request.POST['nombre']
        juguetes.categoria = request.POST['categoria'] 
        juguetes.garantia = request.POST['garantia'] 
        juguetes.reseña = request.POST['reseña'] 
        juguetes.precio = request.POST['precio'] 
        juguetes.save()
        return redirect('inicio')
    return render(request, 'editar_juguetes.html', {'juguete': juguetes}) 


def borrar_juguetes(request, id):
    juguetes = get_object_or_404(Juguetes, id=id) 
    if request.method == 'POST':
        juguetes.delete()
        return redirect('inicio')
    return render(request, 'borrar_juguetes.html', {'juguete': juguetes}) 
