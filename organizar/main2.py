arvore=['B', ['A', ['C'], ['D', ['G'], ['H'], ['I'] ] ], ['J'], ['E', ['F'],]]

# Passa por todos os nós (vértices) da árvore e avisa
# quando encontra um nó-folha
def percorre(arvore):
  print('Visitando o nó: ',arvore[0])
  if len(arvore)==1: # É um vértice sem filhos pois a lista só tem um elemento
     print('É uma folha') 
  else:
     for filho in arvore[1:]: # Vai processar cada um dos filhos 
       percorre(filho)


print('Antes')
percorre(arvore)
print('Depois')