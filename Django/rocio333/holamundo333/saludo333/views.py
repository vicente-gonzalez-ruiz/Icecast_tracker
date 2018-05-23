from django.shortcuts import render #importamos render de django

# Create your views here.

def saludo(request):
	nombre = "Roci"
	tupla = (1,2,3,4,5,6,7,8,9,10);
	context = {
		'saludo':'Hello, how are you?',
		'tupla':tupla,
		'nombre':nombre
	}
	#devolveremos los datos a la vista saludo.html para printarlos
	return render(request,'saludo3.html',context)


