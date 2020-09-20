from django.shortcuts import render, redirect
from .models import Oferta
from cuenta.models import Categoria,Matricula_Titulo,Titulo
from .forms import OfertaForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    ofertas=Oferta.objects.all()  
    contexto = {"ofertas" : ofertas}
    return render(request, "bolsa/index.html",contexto)

@login_required
def new_oferta(request):
    if request.user.tipo_usuario=="trabajador":
        if request.method == "POST":
            form= OfertaForm(request.POST,request.FILES)        
            if form.is_valid():
                oferta=form.save(commit=False)
                oferta.oferente = request.user
                #cargar titulo automaticamente
                id_titulo=Matricula_Titulo.objects.filter(trabajador_id=request.user.id).values()[0]
                titulo=Titulo.objects.filter(id=id_titulo["titulo_id"]).values()[0]
                cat=Categoria.objects.filter(id=titulo["categoria_id"]).values()[0]
                oferta.categoria_id=cat["id"]
                oferta.save()
                return redirect("oferta", oferta.id)
            else:
                contexto={"form":form,}
                return render(request, "bolsa/new.html",contexto)
        #Metodo Get        
        form = OfertaForm()
        contexto={"form":form,}
        return render(request, "bolsa/new.html",contexto)
    else:
        return redirect("index")

def show_oferta(request,id):
    oferta=Oferta.objects.get(pk=id)
    usuario=oferta.oferente
    contexto = {
    "oferta":oferta,}
    return render(request,"bolsa/oferta.html",contexto)

def show_categoria(request,id):
    cat=Categoria.objects.get(pk=id)
    ofertas = Oferta.objects.filter(categoria=cat.id)
    contexto = {"ofertas":ofertas,}
    return render(request, "bolsa/index.html",contexto)

def borrar_oferta(request,id):
    oferta=Oferta.objects.get(pk=id)
    if oferta.oferente == request.user:
        if request.method == "POST":
            if oferta.oferente == request.user:
                oferta.delete()
                return redirect("index")            
        else:
            oferta.delete()
            return redirect("index")

def editar_oferta(request, id):
    oferta = Oferta.objects.get(pk = id)
    if oferta.oferente == request.user:
        if request.method == "GET":
            form = OfertaForm(instance = oferta)
            contexto = {
                "form" : form,
                "editar" : "editar"
            }
            return render(request, "bolsa/new.html", contexto)
        elif request.method == "POST":
            form = OfertaForm(request.POST,request.FILES, instance = oferta)
            print(form.is_valid())
            print(form)
            if form.is_valid():
                print(form.cleaned_data)
                ofer = form.save()
                return redirect("oferta", ofer.id)
            else:
                contexto = {
                "form" : form,
                "editar" : "editar"
                }
                return render(request, "bolsa/new.html", contexto)


