from django.db import models
from django.conf import settings
from graphviz import Digraph
import re

# Create your models here.

class Automato(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    alfabeto = models.CharField(max_length=100)
    estados = models.CharField(max_length=100)
    estadoInicial = models.CharField(max_length=100)
    estadosAceitacao = models.CharField(max_length=100)
    dicTransicoes = models.CharField(max_length=1000)
    diagrama = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    def printAlfabeto(self):
        return str(set(self.alfabeto.split()))

    def printEstados(self):
        return str(set(self.estados.split()))

    def printEstadosAceitacao(self):
        return str(set(self.estadosAceitacao.split()))

    def printDicTransicoes(self):
        dicTransicoes = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicTransicoes.split()}

        tabela = []

        linha = ['']
        for simbolo in self.alfabeto.split():
            linha.append(simbolo)
        tabela.append(linha)

        for estado in self.estados.split():
            linha = [estado]
            for simbolo in self.alfabeto.split():
                linha.append(dicTransicoes[(estado, simbolo)])
            tabela.append(linha)

        return tabela

    def desenharDiagrama(self):
        d = Digraph(name=self.descricao)

        d.graph_attr['rankdir'] = 'LR'
        d.edge_attr.update(arrowhead='vee', arrowsize='1')
        d.node_attr['shape'] = 'circle'

        d.node('Start', label='', shape='none')

        estadosTransicao = set(self.estados.split()) - set(self.estadosAceitacao.split())
        for estado in estadosTransicao:
            d.node(estado)

        for estado in self.estadosAceitacao.split():
            d.node(estado, shape='doublecircle')

        d.edge('Start', self.estadoInicial)

        for transicao_comma in self.dicTransicoes.split():
            transicao = transicao_comma.split('-')
            d.edge(transicao[0], transicao[2], label = transicao[1])

        d.format = 'svg'
        self.diagrama = f"website/images/afd/{self.filename}.svg"
        d.render(f"website/static/website/images/afd/{self.filename}")

    def validarSequencia(self, sequencia):
        estado = self.estadoInicial

        dicTransicoes = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicTransicoes.split()}

        for simbolo in sequencia:
            if simbolo in self.alfabeto:
                estado = dicTransicoes[(estado, simbolo)]
            else:
                return False

        if estado in self.estadosAceitacao:
            return True
        else:
            return False

class ExpressaoRegular(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    regex = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    def printRegex(self):
        return self.regex

    def validarSequencia(self, sequencia):
        regex = re.compile(self.regex)

        if re.match(regex, sequencia):
            return True
        else:
            return False

class MaquinaTuring(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    alfabeto = models.CharField(max_length=100)
    estados = models.CharField(max_length=100)
    estadoInicial = models.CharField(max_length=100)
    estadosAceitacao = models.CharField(max_length=100)
    dicTransicoes = models.CharField(max_length=1000)
    diagrama = models.CharField(max_length=100)
    sequenciaFinal = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    def printAlfabeto(self):
        return str(set(self.alfabeto.split()))

    def printEstados(self):
        return str(set(self.estados.split()))

    def printEstadosAceitacao(self):
        return str(set(self.estadosAceitacao.split()))

    def printDicTransicoes(self):
        dicTransicoes = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicTransicoes.split()}

        tabela = []

        linha = ['']
        for simbolo in self.alfabeto.split():
            linha.append(simbolo)
        tabela.append(linha)

        temp = linha[1:]
        for estado in self.estados.split():
            linha = [estado]
            for simbolo in temp:
                encontrado = False
                for dicEstado, dicSimbolo in dicTransicoes:
                    if dicSimbolo[0] == simbolo and dicEstado == estado:
                        linha.append(dicSimbolo[1] + dicSimbolo[2] + " -> " + dicTransicoes[(estado, dicSimbolo)])
                        encontrado = True
                        break
                if encontrado == False:
                    linha.append("-")
            tabela.append(linha)

        return tabela

    def desenharDiagrama(self):
        d = Digraph(name=self.descricao)

        d.graph_attr['rankdir'] = 'LR'
        d.edge_attr.update(arrowhead='vee', arrowsize='1')
        d.node_attr['shape'] = 'circle'

        d.node('Start', label='', shape='none')

        estadosTransicao = set(self.estados.split()) - set(self.estadosAceitacao.split())
        for estado in estadosTransicao:
            d.node(estado)

        for estado in self.estadosAceitacao.split():
            d.node(estado, shape='doublecircle')

        d.edge('Start', self.estadoInicial)

        dicTransicoes = {}
        for item in self.dicTransicoes.split():
            transicao = item.split('-')

            if (transicao[0], transicao[2]) not in dicTransicoes.keys():
                dicTransicoes[(transicao[0], transicao[2])] = transicao[1]
            else:
                dicTransicoes[(transicao[0], transicao[2])] = dicTransicoes[(transicao[0], transicao[2])] + ", " + transicao[1]

        for estados in dicTransicoes:
            d.edge(estados[0], estados[1], label = dicTransicoes[estados])

        d.format = 'svg'
        self.diagrama = f"website/images/mt/{self.filename}.svg"
        d.render(f"website/static/website/images/mt/{self.filename}")

    def validarSequencia(self, sequencia):
        estadoAtual = self.estadoInicial
        sequencia = '@' + sequencia + '@'

        dicTransicoes = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicTransicoes.split()}

        cabecaLeitura = 1
        movAnterior = ''
        while True:
            if sequencia[cabecaLeitura] in self.alfabeto:
                for estado, simbolo in dicTransicoes:
                    if estado == estadoAtual and sequencia[cabecaLeitura] == simbolo[0]:
                        if sequencia[cabecaLeitura] == '@':
                            if movAnterior == 'R':
                                sequencia = sequencia + '@'
                            elif movAnterior == 'L':
                                sequencia = '@' + sequencia
                            else:
                                sequencia = '@' + sequencia + '@'

                        sequencia = sequencia[:cabecaLeitura] + simbolo[1] + sequencia[cabecaLeitura + 1:]
                        
                        if simbolo[2] == 'R':
                            cabecaLeitura += 1
                            movAnterior = 'R'
                            estadoAtual = dicTransicoes[(estado, simbolo)]
                            break
                        elif simbolo[2] == 'L':
                            cabecaLeitura -= 1
                            movAnterior = 'L'
                            estadoAtual = dicTransicoes[(estado, simbolo)]
                            break
                        else:
                            return False
                else:
                    break
            else:
                return False

        if estadoAtual in self.estadosAceitacao:
            self.sequenciaFinal = sequencia
            return True
        else:
            return False