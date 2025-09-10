from django.views.generic import FormView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Endereco
from .forms import ConsultaCepForm
import requests
import certifi

class EnderecoCreateView(FormView):
    template_name = 'viacep/viacep_form.html'
    form_class = ConsultaCepForm
    success_url = reverse_lazy('endereco_list')

    def form_valid(self, form):
        cep = form.cleaned_data['cep'].replace('-', '').strip()

        if Endereco.objects.filter(cep=cep).exists():
            return super().form_valid(form)

        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/',verify =certifi.where())
        if response.status_code == 200:
            data = response.json()
            if 'erro' in data:
                form.add_error('cep', 'CEP inválido')
                return self.form_invalid(form)

            Endereco.objects.create(
                cep=cep,
                rua=data.get('logradouro', ''),
                bairro=data.get('bairro', ''),
                cidade=data.get('localidade', ''),
                estado=data.get('uf', ''),
            )
            return super().form_valid(form)
        else:
            form.add_error('cep', 'Erro ao consultar o serviço ViaCEP')
            return self.form_invalid(form)

class EnderecoListView(ListView):
    model = Endereco
    template_name = 'viacep/viacep_list.html'
    context_object_name = 'enderecos'

class EnderecoDetailView(DetailView):
    model = Endereco
    template_name = 'viacep/viacep_detail.html'
    context_object_name = 'endereco'

class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'viacep/viacep_delete.html'
    success_url = reverse_lazy('endereco_list')
