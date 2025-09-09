from django.shortcuts import render
from .forms import ConsultaCepForm
import requests

def consulta_cep(request):
    endereco = None

    if request.method == 'POST':
        form = ConsultaCepForm(request.POST)
        if form.is_valid():
            cep = form.cleaned_data['cep']
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            if response.status_code == 200:
                dados = response.json()
                if 'erro' not in dados:
                    endereco = {
                        'rua': dados.get('logradouro', ''),
                        'bairro': dados.get('bairro', ''),
                        'cidade': dados.get('localidade', ''),
                        'estado': dados.get('uf', ''),
                        'cep': cep
                    }
                else:
                    form.add_error('cep', 'CEP não encontrado.')
    else:
        form = ConsultaCepForm()

    return render(request, 'consulta_cep.html', {'form': form, 'endereco': endereco})




# Create your views here.
