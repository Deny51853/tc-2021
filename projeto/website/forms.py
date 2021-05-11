from django import forms
from django.forms import ModelForm
from .models import Automato, ExpressaoRegular, MaquinaTuring

class FormSequencia(forms.Form):
    sequencia = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Insira uma sequência', 'size': '25'}))

class FormAutomato(ModelForm):
    class Meta:
        model = Automato
        fields = '__all__'
        exclude = ['diagrama']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Autómato finito determinístico que aceita sequências...'}),
            'alfabeto': forms.TextInput(attrs={'class': 'form-control'}),
            'estados': forms.TextInput(attrs={'class': 'form-control'}),
            'estadoInicial': forms.TextInput(attrs={'class': 'form-control'}),
            'estadosAceitacao': forms.TextInput(attrs={'class': 'form-control'}),
            'dicTransicoes': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nome': 'Nome do autómato finito determinístico',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosAceitacao': 'Estados de aceitação',
            'dicTransicoes': 'Transições',
        }

        placeholders = {
            'nome': 'Nome do autómato finito determinístico',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosAceitacao': 'Estado de aceitação',
            'dicTransicoes': 'Transições'
        }

        help_texts = {
            'nome': 'Atribua um nome, com no máximo 3 palavras, que identifique o autómato finito determinístico.',
            'descricao': 'Descreva o tipo de sequências que o autómato reconhece.',
            'alfabeto': 'Insira os simbolos do alfabeto separados por espaços (ex.: "0 1").',
            'estados': 'Insira os nomes dos estados separados por espaços (ex.: "A B").',
            'estadoInicial': 'Insira o estado inicial.',
            'estadosAceitacao': 'Insira os estados separados por espaços (ex.: "A B").',
            'dicTransicoes': 'Insira as transições, estadoInicial-simbolo-estadoSeguinte, separadas por espaços (ex.: "A-0-B A-1-A").'
        }

class FormExpressaoRegular(ModelForm):
    class Meta:
        model = ExpressaoRegular
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Expressao regular que valida...'}),
            'regex': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'nome': 'Nome da expressão',
            'descricao': 'Descrição',
            'regex': 'Expressão Regular'
        }

        placeholders = {
            'nome': 'Nome da expressão',
            'descricao': 'Descrição',
            'regex': 'Expressão Regular'
        }

        help_texts = {
            'nome': 'Atribua um nome, com no máximo 3 palavras, que identifique a expressão regular.',
            'descricao': 'Descreva o tipo de sequências que a expressão regular reconhece.',
            'regex': 'Insira a expressão regular (ex.: "^[0-9]{4}-[0-9]{3}$").'
        }

class FormMaquinaTuring(ModelForm):
    class Meta:
        model = MaquinaTuring
        fields = '__all__'
        exclude = ['diagrama', 'sequenciaFinal']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Máquina de turing que aceita sequências...'}),
            'alfabeto': forms.TextInput(attrs={'class': 'form-control'}),
            'estados': forms.TextInput(attrs={'class': 'form-control'}),
            'estadoInicial': forms.TextInput(attrs={'class': 'form-control'}),
            'estadosAceitacao': forms.TextInput(attrs={'class': 'form-control'}),
            'dicTransicoes': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'nome': 'Nome da máquina de turing',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosAceitacao': 'Estados de aceitação',
            'dicTransicoes': 'Transições'
        }

        placeholders = {
            'nome': 'Nome da máquina de turing',
            'descricao': 'Descrição',
            'alfabeto': 'Alfabeto de símbolos',
            'estados': 'Estados',
            'estadoInicial': 'Estado inicial',
            'estadosAceitacao': 'Estado de aceitação',
            'dicTransicoes': 'Transições'
        }

        help_texts = {
            'nome': 'Atribua um nome, com no máximo 3 palavras, que identifique a máquina de turing.',
            'descricao': 'Descreva o tipo de sequências que a máquina de turing reconhece.',
            'alfabeto': 'Insira os simbolos do alfabeto separados por espaços (ex.: "0 1").',
            'estados': 'Insira os estados separados por espaços (ex.: "A B").',
            'estadoInicial': 'Insira o estado inicial.',
            'estadosAceitacao': 'Insira os estados separados por espaços (ex.: "A B").',
            'dicTransicoes': 'Insira as transições, estadoInicial-simbolo-estadoSeguinte, separadas por espaços (O símbolo "@" corresponde ao delta, ex.: "A-00R-B A-10L-A B-@@R-A").'
        }