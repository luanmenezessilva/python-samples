def montaMenu( idPai, cats ):    
    tam = len(cats)
    nPosId = 0
    nPosIdPai = 1
    nPosNome = 2

    print(cats[idPai][nPosNome])    
    for i in range(1, tam, 1):
        if cats[i][nPosIdPai] == idPai:
            print(cats[i][nPosNome])
            montaMenu( cats[i][nPosId], cats)        




if __name__ == '__main__':

    cats = [[1, 0, 'A Empresa'],[2, 1, 'Sobre Nós'],[3, 1, 'Objetivo'],[4, 3, 'Objetivo nossos'],[5, 0, 'Contato'],[6, 0, 'Produtos']]
    # cats = [[1, 0, 'A Empresa'],[2, 1, 'Sobre Nós'],[3, 1, 'Objetivo']]
    # cats = [[1, 0, 'A Empresa'],[2, 1, 'Sobre Nós']]

    montaMenu(1, cats)
