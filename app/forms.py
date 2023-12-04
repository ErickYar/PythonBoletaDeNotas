from django import forms

LISTA_CURSOS=(
    ("Python","Python"),
    ("Django","Django"),
    ("PHP","PHP"),
    ("Java","Java"),
    ("SQLite","SQLite"),
    ("JavaScript","JavaScript"),

)

# clase definir los datos del alumnos

class Alumno(forms.Form):
    #definir los datos
    código=forms.CharField()
    nombre=forms.CharField()
    curso=forms.ChoiceField(choices=LISTA_CURSOS)
    parcial=forms.IntegerField()
    practica=forms.IntegerField()
    final=forms.IntegerField()
