""" Arquivo principal do projeto """
from __future__ import print_function
import re
import os
import datetime
import codecs
import wget
from src.dict import utf8_to_utf8_right as fix_str
from flask import Flask

NOW = datetime.datetime.now()
app = Flask(__name__)

class Ator(object):
    """ Seta os dados do ator """
    def __init__(self, name, nr, pos=-1, segu=-1, segnd=-1):
        self.nome = name
        self.real = nr
        self.post = pos
        self.seg = segu
        self.segn = segnd

    def __repr__(self):
        return (self.nome, self.post, self.seg, self.segn, self.real)

    def  __str__(self):
        return str((self.nome, self.post, self.seg, self.segn, self.real))

# Ideia: ter uma hash pra mapear (nome_instagram => nome real)

def ator_from_url(url):
    """ Funcao recebe uma url e retorna um objeto do tipo ator """
    try:
        ator = re.findall(r'\.com\/(.*)\/', url)[0]
    except:
        return False

    try:
        # Impedir uso do arquivo velho e apaga-lo apos o uso
        os.system("rm {}.html".format(ator.nome))
    except:
        pass

    print("ator :: " + ator)

    try:
        html = open(wget.download(url=url, out=ator+".html"), 'r').read()
    except:
        with open('atores_removidos', 'a') as arquivo_removidos:
            arquivo_removidos.write(url+'\n')
            seguidores = 0
            posts = 0
            seguindo = 0
            nomereal = ator
        return Ator(name=ator, pos=posts, segu=seguidores, segnd=seguindo, nr=nomereal)

    seguidores = int(re.findall(r'edge_followed_by":\{"count":(\d+)', html)[0])
    posts = int(re.findall(r'"edge_owner_to_timeline_media":\{"count":(\d+)', html)[0])
    seguindo = int(re.findall(r'"edge_follow":\{"count":(\d+)', html)[0])
    nomereal = re.findall(r'"full_name":"(.*?")', html)[0][:-1]
    return Ator(name=ator, pos=posts, segu=seguidores, segnd=seguindo, nr=nomereal)

@app.route("/")
def hello():
    return "Hello World."

def main(debug=False, folder='../csv'):
    """ Monta a lista de urls usada para extrair as informcoes """
    try:
        os.system("rm *.html")
    except:
        pass

    if not os.path.exists(folder):
        os.makedirs(folder)

    path = './' + folder + '/'
    urls = []
    valid_urls = []

    with open('atores_lista', 'r') as arquivo_lista:
        for linha in arquivo_lista:
            urls.append(linha[:-1])  # Retira a quebra de linha

    with codecs.open(path + 'atores_dados ' + (NOW.strftime("%d-%m-%y-%H:%M")) + '.csv', 'w',
                     "utf-8") as arquivo_dados: 
        arquivo_dados.write('Nome real da conta,Conta,Seguidores,Seguindo,Postagens\n')

        for url in urls:
            print(url)
            ator = ator_from_url(url)

            if ator.seg !=0:
                string = (fix_str(ator.real) + ',' + 'https://www.instagram.com/' +
                          fix_str(ator.nome) + '/,' + str(ator.seg) + ',' + str(ator.segn) + ',' +
                          str(ator.post) + '\n')
                arquivo_dados.write(string)
                valid_urls.append(url)
            else:
                arquivo_dados.write(ator.real+';'+'/s' + ';' + '/s' + ';' +'/s'+ ';' + '/s'  +'\n')
                valid_urls.append(url)


   #  Atualizar a lista mantendo APENAS os links validos
   # with open('atores_lista', 'w') as arquivo_dados:
   #     for url in valid_urls:
   #         arquivo_dados.write(url+'\n')

    if not debug: # Nao remover se quiser debugar :)
        try:
            os.system("rm *.html")  # Impedir uso do arquivo velho e apaga-lo apos o uso
        except:
            pass

# Nao faz sentido: melhor deixar pra debug
# os.system("rm *.html")  # Impedir que se use arquivo velho e apagar apohs o uso
if __name__ == '__main__':
    main()
