import spacy

nlp = spacy.load('en_core_web_sm')
palavrasArquivo = []
listaTabela=[]
listaTabelaValor=[]


vetorClasse=[]
vetorMetodo=[]
vetorAtributo=[]

examples = False

i = 1

arquivo = open('caso01.txt', 'r')

for linha in arquivo:
    linha = linha.strip()
    palavrasArquivo.append(linha)
arquivo.close
for words in palavrasArquivo:
    doc = nlp(words)

    ##pegar palavras





    ##pegar dados tabela

    if "Examples" in words:
        examples = True
    if examples:
        if i < 2:
            if not ("Examples" in words):
                for token in doc:
                    if token.text != "|" and token.text != "" and token.text != ":" and token.text != "Examples":
                        listaTabela.append(token.text)

                i = i + 1
        else:
            for token in doc:
                if token.pos_ == "NUM" and token.text != "|":
                    listaTabelaValor.append(token.text)




tamanhoVariaveisTabela=listaTabela.__len__()
print(tamanhoVariaveisTabela)
print(listaTabela)
print(listaTabelaValor)
x=0
for palavras in listaTabelaValor:
    if(x==3):
        x=0
    print(listaTabela[x])
    print(palavras)
    x=x+1

