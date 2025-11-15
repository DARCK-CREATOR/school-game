from django.shortcuts import render,redirect,get_object_or_404
from .forms import Formulaire
from .models import Inscription
def index(request):
    return render(request,"game/index.html")
    
def inscription(request):
    if request.method == "POST":
        form = Formulaire(request.POST,request.FILES)
        
        if form.is_valid():
            perso =form.save()
            return redirect("profil",id=perso.id)
    else:
        form = Formulaire()
    return render(request,"game/inscription.html",{"form":form})
          
def connexion(request):
    message = ""
    if request.method == "POST":
        nom = request.POST.get("nom")
        password = request.POST.get("password")
        try:
            perso = Inscription.objects.get(nom=nom,password=password)
            return redirect("profil",id=perso.id)
        except Inscription.DoesNotExist:
            message = "Nom ou mot de passe incorrect ! "
            
        
    return render(request,"game/connexion.html",{"message": message})
    
def profil(request,id):
    perso = get_object_or_404(Inscription,id=id)
    
    personnes = Inscription.objects.all().order_by("-date_creation")
    return render(request,"game/profil.html",{"personnes": personnes,"perso":perso})

def classement(request):
    return render(request,"game/classement.html")
    
def niveau(request):
    return render(request,"game/niveau.html")
    
def debutant1(request):
    return render(request,"game/debutant1.html")
    
def niveau2(request):
    return render(request,"game/niveau2.html")
    
def debutant3(request):
    return render(request,"game/debutant3.html")
    
def debutant4(request):
    return render(request,"game/debutant4.html")
    
def debutant5(request):
    return render(request,"game/debutant5.html")
    
def debutant6(request):
    return render(request,"game/debutant6.html")
    
def debutant7(request):
    return render(request,"game/debutant7.html")
    
def debutant3(request):
    return render(request,"game/debutant3.html")
    
def debutant8(request):
    return render(request,"game/debutant8.html")
    
def debutant9(request):
    return render(request,"game/debutant9.html")
    
def debutant10(request):
    return render(request,"game/debutant10.html")
    
def debutant11(request):
    return render(request,"game/debutant11.html")
    
def debutant12(request):
    return render(request,"game/debutant12.html")
    
def debutant13(request):
    return render(request,"game/debutant13.html")
    
def debutant14(request):
    return render(request,"game/debutant14.html")
    
def debutant15(request):
    return render(request,"game/debutant15.html")
    
def debutant16(request):
    return render(request,"game/debutant16.html")
    
def debutant17(request):
    return render(request,"game/debutant17.html")
    
def debutant18(request):
    return render(request,"game/debutant18.html")
    
def debutant19(request):
    return render(request,"game/debutant19.html")

def debutant20(request):
    return render(request,"game/debutant20.html")

                          
