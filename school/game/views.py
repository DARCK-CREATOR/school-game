from django.shortcuts import render,redirect,get_object_or_404
from .forms import Formulaire
from .models import Inscription,Score
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
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
    
@csrf_exempt
def save_score(request):
    if request.method=="POST":
        data = json.loads(request.body.decode("utf-8"))
        value = data.get("value")
        joueurs = data.get("joueur")
        joueur = Inscription.objects.get(id=joueurs)
        Score.objects.create(score=value,joueur=joueur)
      
        return JsonResponse({"message":"Score mise a jour"})
    return JsonResponse({"error":"Methode non autoriser frere"},status=400)
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
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    personnes = Inscription.objects.all().order_by("-date_creation")
    return render(request,"game/profil.html",{"personnes": personnes,"perso":perso,"score": score})

def classement(request):
    return render(request,"game/classement.html")
    
def niveau(request,id):
    return render(request,"game/niveau.html",{"joueur_id":id})

def debutant1(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant1.html",{"joueur_id":id, "score":score})
def niveau2(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/niveau2.html",{"joueur_id":id,"score":score})
    
def debutant3(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant3.html",{"joueur_id": id,"score":score})
    
def debutant4(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant4.html",{"joueur_id":id,"score":score})
    
def debutant5(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant5.html",{"joueur_id":id,"score":score})
    
def debutant6(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant6.html",{"joueur_id":id,"score":score})
    
def debutant7(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant7.html",{"joueur_id":id,"score":score})
    
def debutant8(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant8.html",{"joueur_id":id,"score":score})
    
def debutant9(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant9.html",{"joueur_id":id,"score":score})
    
def debutant10(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant10.html",{"joueur_id":id,"score":score})
    
def debutant11(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant11.html",{"joueur_id":id,"score":score})
    
def debutant12(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant12.html",{"joueur_id":id,"score":score})
    
def debutant13(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant13.html",{"joueur_id":id,"score":score})
    
def debutant14(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant14.html",{"joueur_id":id,"score":score})
    
def debutant15(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant15.html",{"joueur_id":id,"score":score})
    
def debutant16(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant16.html",{"joueur_id":id,"score":score})
    
def debutant17(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant17.html",{"joueur_id":id,"score":score})
    
def debutant18(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant18.html",{"joueur_id":id,"score":score})
    
def debutant19(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant19.html",{"joueur_id":id,"score":score})

def debutant20(request,id):
    score = Score.objects.filter(joueur=id).order_by("-id").first()
    return render(request,"game/debutant20.html",{"joueur_id":id,"score":score})

                          
