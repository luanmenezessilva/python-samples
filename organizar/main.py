from treelib import Node, Tree
import json


def main(data):
    print('MAIN:')
    for i in data['dados']:
        num = 1
        # print(i)
        # print(i['familia'])
        # print(i['descricao'])
        # print(i['familia_pai'])


def lista(data, index):
    print('indice: ', index)
    familia_pai = data[index]['familia_pai']
    if familia_pai == 0:
        print('Sem filhos')
    else:
        for filho in data[1:]:
            lista(filho)

    # print(index)
    # print('lista')
    # if index >= len(data):
    #     return 0

    # print(data[index])

    # familia_pai = data[index]['familia_pai']
    # if familia_pai > 0:
    #     lista(data, familia_pai)
    # else:
    #     lista(data, index + 1)
    # if data['dados'][index]['familia_pai'] > 0:
    #     index = data['dados'][index]['familia']
    #     lista(data, index)
    # else:
    #     print(data['dados'][index])
    #     # lista(data, index-1)
    #     lista(data, index)


def listaTree():
    tree = Tree()

    tree.create_node("CEO", "CEO")  # root
    tree.create_node("VP_1", "VP_1", parent="CEO")
    tree.create_node("VP_2", "VP_2", parent="CEO")
    tree.create_node("GM_1", "GM_1", parent="VP_1")
    tree.create_node("GM_2", "GM_2", parent="VP_2")
    tree.show()

def listaa(data):
    tree = Tree()

    tree.create_node("DADOS", "DADOS")  # root
    for i in data:
        familia = i['familia']
        pai = i['familia_pai']
        tree.create_node(familia, familia, parent=pai)    
    
    print(tree.show())


def listaSimples(data, index):
    print(data)

    familia = data[index]['familia']
    pai = data[index]['familia_pai']

    print('')
    print('familia:',familia)
    print('pai:', pai)



if __name__ == '__main__':
    file = open('data.json')
    out_file = open("myfile.json", "w")
    data = json.load(file)

    # main(data)

    # lista(data, len(data['dados'][0]))
    # print('lista')
    # lista(data['dados'], 0)
    # print(data['dados'][0])

    # listaa(data['dados'])

    print('')
    print('Lista Simples:')
    listaSimples(data['dados'], 0)

    json.dump(data['dados'][1], out_file, indent=3)

    file.close()
    out_file.close()
