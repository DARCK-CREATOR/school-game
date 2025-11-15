from django.urls import path
from . import views

urlpatterns= [
   path('',views.index,name="index"),
   path('inscription/',views.inscription,name="inscription"),
   path('connexion/',views.connexion,name="connexion"),
   path("niveau/",views.niveau,name="niveau"),
   path('profil/<int:id>/',views.profil,name="profil"),
   path('classement/',views.classement,name="classement"),
   path('debutant1/',views.debutant1,name="debutant1"),
   path('niveau2/',views.niveau2,name="niveau2"),
   path('debutant3/',views.debutant3,name="debutant3"),
   path('debutant4/',views.debutant4,name="debutant4"),
   path('debutant5/',views.debutant5,name="debutant5"),
   path('debutant6/',views.debutant6,name="debutant6"),
   path('debutant7/',views.debutant7,name="debutant7"),
   path('debutant8/',views.debutant8,name="debutant8"),
   path('debutant9/',views.debutant9,name="debutant9"),
   path('debutant10/',views.debutant10,name="debutant10"),
   path('debutant11/',views.debutant11,name="debutant11"),
   path('debutant12/',views.debutant12,name="debutant12"),
   path('debutant13/',views.debutant13,name="debutant13"),
   path('debutant14/',views.debutant14,name="debutant14"),
   path('debutant15/',views.debutant15,name="debutant15"),
   path('debutant16/',views.debutant16,name="debutant16"),
   path('debutant17/',views.debutant17,name="debutant17"),
   path('debutant18/',views.debutant18,name="debutant18"),
   path('debutant19/',views.debutant19,name="debutant19"),
   path('debutant20/',views.debutant20,name="debutant20"),


]
