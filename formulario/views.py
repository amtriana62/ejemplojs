from django.shortcuts import render

# Create your views here.
from .forms import CalculadoraForm

def calcular_valores(request):
    if request.method == 'POST':
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            numero1 = form.cleaned_data['numero1']
            numero2 = form.cleaned_data['numero2']
            resultado = numero1 + numero2
            form.cleaned_data['resultado'] = resultado  # Agrega el resultado al formulario
    else:
        form = CalculadoraForm()

    return render(request, 'calcular_valores.html', {'form': form})
