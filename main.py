import spacy

nlp = spacy.load('en_core_web_sm')
palavrasArquivo = []
listaTabela=[]
listaTabelaValor=[]

contadorReferenciaAtributo=-1
vetorClasse=[]
vetorReferenciaMetodoClasse=[]
vetorReferenciaAtributoMetodo=[]
vetorMetodo=[]
vetorAtributo=[]
vetorValorAtributo=[]
vetorReferenciaValorAtributo=[]
entrouIfGiven=False
examples = False
given=False
when=False
then=False
posSeta=False
i = 1
seta=False
palavrasSeta=[]
arquivo = open('caso01.txt', 'r')
contadorMetodo=0
contadorAtributo=0
for linha in arquivo:
    linha = linha.strip()
    palavrasArquivo.append(linha)
arquivo.close
for words in palavrasArquivo:
    doc = nlp(words)

    ##pegar palavras
    if "Given" in words:
        given=True
        when=False
        examples=False
    if "When" in words:
        given = False
        when=True
        examples=False
    if "Then" in words:
        then=True
        when=False
        examples=False
    if "Examples" in words:
        contadorReferenciaAtributo = contadorReferenciaAtributo + 1
        contadorAtributo = contadorAtributo + 1
        contadorMetodo = contadorMetodo + 1
        examples = True
        then=False
        given=False
        when=False
    if given:
        for token in doc:
            if token.text=="<":
                seta=True
            elif seta:
                if token.text==">":
                    seta=False
                else:
                    posSeta=True
                    palavrasSeta.append(token.text)
            elif posSeta:
                vetorAtributo.append(token.text)
                if not entrouIfGiven:
                    vetorClasse.append(token.text)
            elif token.pos_ != 'DET' and token.is_stop == False and token.pos_ != "ADJ" and \
                    token.pos != "PRON" and token.text != "|" and token.text != "" and token.text != ":" and token.text != "Given" :
                if not(vetorClasse.__contains__(token.text)):
                    entrouIfGiven=True
                    vetorClasse.append(token.text)
    posSeta=False
    if when:
        for token in doc:
            if token.text=="<":
                seta=True
            elif seta:
                if token.text==">":
                    seta=False
                else:
                    posSeta=True
                    palavrasSeta.append(token.text)
            elif posSeta:
                if not vetorAtributo.__contains__(token.text):
                    vetorAtributo.append(token.text)
            elif token.pos_ != 'DET' and token.is_stop == False and token.pos_ != "ADJ" and \
                    token.pos != "PRON" and token.text != "|" and token.text != "" and token.text != ":" and token.text != "Given" :
                vetorMetodo.append(token.text)
                vetorReferenciaMetodoClasse.append(contadorMetodo)

    if then:
        for token in doc:
            if token.text=="<":
                seta=True
            elif seta:
                if token.text==">":
                    seta=False
                else:
                    palavrasSeta.append(token.text)
            elif token.pos_ != 'DET' and token.is_stop == False and token.pos_ != "ADJ" and \
                    token.pos != "PRON" and token.text != "|" and token.text != "" and token.text != ":" and token.text != "Given" :
                vetorReferenciaAtributoMetodo.append(contadorAtributo)
                if not vetorAtributo.__contains__(token.text):
                        vetorAtributo.append(token.text)





    ##pegar dados tabela



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
                    vetorValorAtributo.append(token.text)
                    vetorReferenciaValorAtributo.append(contadorReferenciaAtributo)

            contadorReferenciaAtributo+1






print("classe:")
print(vetorClasse)
print("metodo")
print(vetorMetodo)
print("referencia metodo a classe")
print(vetorReferenciaMetodoClasse)
print("atributo")
print(vetorAtributo)
print("referencia atributo ao metodo")
print(vetorReferenciaAtributoMetodo)
print("valor atributo")
print(vetorValorAtributo)
print("referencia valor ao atributo")
print(vetorReferenciaValorAtributo)



