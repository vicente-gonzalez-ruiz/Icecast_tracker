from django.shortcuts import render

# Create your views here.
def saludo_function(request):
	nombre = "Roci"
	context = {
		'saludo':'Hello, how are you? From Koding',
		'nombre':nombre
	}
	#devolveremos los datos a la vista saludo.html para printarlos
	return render(request,'saludo3k.html',context)