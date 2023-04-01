from django.shortcuts import render

# Create your views here.
def index(request):
    tituloVista = 'Formulario'
    context = {
        'titulo': tituloVista,
    }
    return render(request, 'encuesta/formulario.html', context)
def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave':request.POST['password'],
        'educacion':request.POST['educacion'],
        'nacionalidad':request.POST['nacionalidad'],
        'idiomas':request.POST.getlist('idiomas'),
        'correo':request.POST['email'],
        'website':request.POST['sitioweb'],
    }
    return render(request,'encuesta/respuesta.html', context)
def calculadora(request):
    tituloVista = 'Formulario01'
    context = {
        'titulo': tituloVista,
    }
    return render(request, 'encuesta/formulario01.html', context)
def calcular(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        operacion = request.POST.getlist('operacion', '')
        resultado= 0
        print (type(operacion))
        if 'suma' in operacion:
            resultado = num1 + num2
        elif 'resta' in operacion:
            resultado = num1 - num2
        elif 'multiplicacion' in operacion:
            resultado = num1 * num2
        return render(request, 'encuesta/resultado.html', {'resultado': resultado})
    return render(request, 'encuesta/formulario01.html')