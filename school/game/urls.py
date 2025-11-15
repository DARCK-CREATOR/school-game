from django.urls import path
from . import views

urlpatterns= [

   path('',views.index,name="index"),
   path('inscription/',views.inscription,name="inscription"),
   path('connexion/',views.connexion,name="connexion"),
   path("niveau/<int:id>/",views.niveau,name="niveau"),
   path("Save_Score/",views.save_score,name="Save_Score"),
   path('profil/<int:id>/',views.profil,name="profil"),
   path('classement/',views.classement,name="classement"),
   path('debutant1/<int:id>/',views.debutant1,name="debutant1"),
   path('niveau2/<int:id>/',views.niveau2,name="niveau2"),
   path('debutant3/<int:id>/',views.debutant3,name="debutant3"),
   path('debutant4/<int:id>/',views.debutant4,name="debutant4"),
   path('debutant5/<int:id>/',views.debutant5,name="debutant5"),
   path('debutant6/<int:id>/',views.debutant6,name="debutant6"),
   path('debutant7/<int:id>/',views.debutant7,name="debutant7"),
   path('debutant8/<int:id>/',views.debutant8,name="debutant8"),
   path('debutant9/<int:id>/',views.debutant9,name="debutant9"),
   path('debutant10/<int:id>/',views.debutant10,name="debutant10"),
   path('debutant11/<int:id>/',views.debutant11,name="debutant11"),
   path('debutant12/<int:id>/',views.debutant12,name="debutant12"),
   path('debutant13/<int:id>/',views.debutant13,name="debutant13"),
   path('debutant14/<int:id>/',views.debutant14,name="debutant14"),
   path('debutant15/<int:id>/',views.debutant15,name="debutant15"),
   path('debutant16/<int:id>/',views.debutant16,name="debutant16"),
   path('debutant17/<int:id>/',views.debutant17,name="debutant17"),
   path('debutant18/<int:id>/',views.debutant18,name="debutant18"),
   path('debutant19/<int:id>/',views.debutant19,name="debutant19"),
   path('debutant20/<int:id>/',views.debutant20,name="debutant20"),


]
