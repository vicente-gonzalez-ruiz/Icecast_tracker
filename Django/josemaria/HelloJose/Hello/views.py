from django.shortcuts import render

# Create your views here.
def helloJ(request):
	nombre = "Jose"
	}
	#devolveremos los datos a la vista hello.htmll para printarlos
	return render(request,'hello.html',nombre)



