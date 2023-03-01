def montaMenu( id_pai, arrayCats, leftMost, rightMost ):
    nPosId = 0
    nPosIdPai = 1
    nPosNome = 2

    # print('<ul>')

    for i in range(leftMost, rightMost, 1):
        if arrayCats[ i ][nPosIdPai] == id_pai:
            # print("<li>")
            print(arrayCats[ i ][nPosNome])
            leftMost+=1
            print(leftMost)
            montaMenu( arrayCats[ i ][nPosId], arrayCats, leftMost, rightMost )
            # print("</li>")

    # print("</ul>")



if __name__ == '__main__':
    cats = [[1, 0, 'A Empresa'],[2, 1, 'Sobre Nós'],[3, 1, 'Objetivo'],[4, 3, 'Objetivo nossos'],[5, 0, 'Contato'],[6, 0, 'Produtos']]
    # cats = [[1, 0, 'A Empresa'],[2, 1, 'Sobre Nós'],[3, 1, 'Objetivo']]
    # cats = [[1, 0, 'A Empresa'],[2, 1, 'Sobre Nós']]

    print(cats)
    montaMenu(0, cats, 0, len(cats))