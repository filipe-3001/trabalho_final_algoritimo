dic_nome = {}
dic_tipo = {}
dic_preco = {}
dic_disp = {}
login_geral = {}
login_g = {}
login_preco = {}
login_p = {}

def cadastro():
    codigo = int(input('Digite o código do produto:'))
    nome = input('Digite o nome:')
    tipo = input('Digite o tipo:')
    preco = float(input('Digite o preço:'))
    disponivel = input('Está disponível para venda?')
    dic_nome[codigo] = nome
    dic_tipo[codigo] = tipo
    dic_preco[codigo] = preco
    dic_disp[codigo] = disponivel


def consulta():
    cod_cons = int(input("Digite o código do produto: "))
    if cod_cons in dic_nome:
        print(f'Nome: {dic_nome[cod_cons]}\nTipo:{dic_tipo[cod_cons]}\nPreço:{dic_preco[cod_cons]}\nEm estoque:{dic_disp[cod_cons]}')
    else:
        print("Este código não existe!")


def atualizar():
    at_cod = int(input("Digite o código do produto:"))
    print("Atualização!!!!")
    at_nome = input("Digite o nome:")
    at_tipo = input("Digite o tipo:")
    at_preco = input("Digite o preço:")
    at_disp = input("Em estoque:")
    dic_nome.update({at_cod: at_nome})
    dic_tipo.update({at_cod: at_tipo})
    dic_preco.update({at_cod: at_preco})
    dic_disp.update({at_cod: at_disp})


def relatorio():
    peneira = int(input('Digite o número da opção que você deseja:\n0 - Todos os produtos \n1 - Somente filmes \n2 - Somente séries \n3 - Documentários \n4 - Produtos disponíveis para venda\n5 - Produtos indisponíveis para venda'))
    if peneira == 0:
        for item_rel in dic_nome:
            print(f"Código:{item_rel}, Nome:{dic_nome[item_rel]}, Tipo:{dic_tipo[item_rel]}, Preço:{dic_preco[item_rel]}, Em estoque:{dic_disp[item_rel]}")
    elif peneira == 1:
        for item_film in dic_tipo:
            if dic_tipo[item_film] == 'filme':
                print(f"Código:{item_film}, Nome:{dic_nome[item_film]}, Tipo:{dic_tipo[item_film]}, Preço:{dic_preco[item_film]}, Em estoque:{dic_disp[item_film]}")
    elif peneira == 2:
        for item_ser in dic_tipo:
            if dic_tipo[item_ser] == 'serie':
                print(f"Código:{item_ser}, Nome:{dic_nome[item_ser]}, Tipo:{dic_tipo[item_ser]}, Preço:{dic_preco[item_ser]}, Em estoque:{dic_disp[item_ser]}")
    elif peneira == 3:
        for item_doc in dic_tipo:
            if dic_tipo[item_doc] == 'documentario':
                print(f"Código:{item_doc}, Nome:{dic_nome[item_doc]}, Tipo:{dic_tipo[item_doc]}, Preço:{dic_preco[item_doc]}, Em estoque:{dic_disp[item_doc]}")
    elif peneira == 4:
        for item_sim in dic_disp:
            if dic_disp[item_sim] == 'sim':
                print(f"Código:{item_sim}, Nome:{dic_nome[item_sim]}, Tipo:{dic_tipo[item_sim]}, Preço:{dic_preco[item_sim]}, Em estoque:{dic_disp[item_sim]}")
    elif peneira == 5:
        for item_nao in dic_disp:
            if dic_disp[item_nao] == 'nao':
                print(f"Código:{item_nao}, Nome:{dic_nome[item_nao]}, Tipo:{dic_tipo[item_nao]}, Preço:{dic_preco[item_nao]}, Em estoque:{dic_disp[item_nao]}")


def regis_comp():
    login = input('Informe o login:')
    cod_list = []
    nome_list = []
    tipo_list = []
    preco_list = []
    data_list = []
    cod_while = 1
    while cod_while != 0:
        cod_prod = int(input('Digite o código do produto:'))
        if cod_prod in dic_nome:
            if dic_disp[cod_prod] == 'sim':
                confirm_regis = input(f'Confirmar produto:{dic_nome[cod_prod]}')
                if confirm_regis == 'sim':
                    data = data_global
                    regis_nome = dic_nome.get(cod_prod)
                    regis_tipo = dic_tipo.get(cod_prod)
                    regis_preco = dic_preco.get(cod_prod)           
                    cod_list.append(cod_prod)
                    nome_list.append(regis_nome)
                    tipo_list.append(regis_tipo)
                    preco_list.append(regis_preco)
                    data_list.append(data)
                else:
                    continue    
            else:
                print("O produto não está disponível!")
                continue
        else:
            print("O código não existe!")
            continue
        regis_term = input('Terminar compra?')
        if regis_term == 'sim':
            break
        else:
            continue
    regis_add_list = input("Já comprou aqui antes?")
    if regis_add_list == 'sim':
        login_g[login] = cod_list, nome_list, tipo_list, preco_list, data_list
        login_geral[login] = login_geral[login] + login_g[login]
        login_p[login] = preco_list
        login_preco[login] = login_preco[login] + login_p[login]
    else:    
        login_geral[login] = cod_list, nome_list, tipo_list, preco_list, data_list
        login_preco[login] = preco_list
    print("Código:  |  Nome:  |  Tipo:  |  Preço:  |  Data:")
    for regis_itens in range(len(cod_list)):
        print(f'{cod_list[regis_itens]}  |  {nome_list[regis_itens]}  |  {tipo_list[regis_itens]}  |  {preco_list[regis_itens]}  |  {data_list[regis_itens]}')
    regis_total = sum(preco_list)
    print(f'Total: {regis_total}')


def historico():
    for his in login_geral:
        print("Login:  |  Data:  |  Valor Total:")
        his_val = sum(login_preco[his])
        print(f"{his}  |  {data_global}  |  {his_val}")


dic_nome[0] = 'Thor'
dic_tipo[0] = 'filme'
dic_preco[0] = 30.00
dic_disp[0] = 'sim'

dic_nome[1] = 'Homem de Ferro'
dic_tipo[1] = 'filme'
dic_preco[1] = 30.00
dic_disp[1] = 'sim'

dic_nome[2] = 'Sem Limites'
dic_tipo[2] = 'serie'
dic_preco[2] = 35.50
dic_disp[2] = 'sim'

dic_nome[3] = 'The Witcher'
dic_tipo[3] = 'serie'
dic_preco[3] = 35.50
dic_disp[3] = 'sim'

dic_nome[4] = 'O Soldado que não Existiu'
dic_tipo[4] = 'filme'
dic_preco[4] = 30.00
dic_disp[4] = 'nao'

dic_nome[5] = '1917'
dic_tipo[5] = 'filme'
dic_preco[5] = 30.00
dic_disp[5] = 'nao'

dic_nome[6] = 'Professor Polvo'
dic_tipo[6] = 'documentario'
dic_preco[6] = 42.50
dic_disp[6] = 'nao'

dic_nome[7] = 'Privacidade Hackeada'
dic_tipo[7] = 'documentario'
dic_preco[7] = 42.50
dic_disp[7] = 'sim'

dic_nome[8] = 'Arremesando Alto'
dic_tipo[8] = 'filme'
dic_preco[8] = 30.00
dic_disp[8] = 'sim'

dic_nome[9] = 'The Umbrella Academy'
dic_tipo[9] = 'serie'
dic_preco[9] = 35.50
dic_disp[9] = 'nao'

dic_nome[10] = 'O Dilema das Redes'
dic_tipo[10] = 'documentario'
dic_preco[10] = 42.50
dic_disp[10] = 'sim'

dic_nome[11] = 'Pelé'
dic_tipo[11] = 'documentario'
dic_preco[11] = 42.50
dic_disp[11] = 'sim'

dic_nome[12] = 'The 100'
dic_tipo[12] = 'serie'
dic_preco[12] = 35.50
dic_disp[12] = 'sim'

dic_nome[13] = 'Vikings'
dic_tipo[13] = 'serie'
dic_preco[13] = 35.50
dic_disp[13] = 'sim'

dic_nome[14] = 'O Homem de Toronto'
dic_tipo[14] = 'filme'
dic_preco[14] = 30.00
dic_disp[14] = 'sim'

dic_nome[15] = 'Agente Oculto'
dic_tipo[15] = 'filme'
dic_preco[15] = 30.00
dic_disp[15] = 'nao'

dic_nome[16] = 'Fungos Fantásticos'
dic_tipo[16] = 'documentario'
dic_preco[16] = 42.50
dic_disp[16] = 'nao'

dic_nome[17] = 'Forrest Gump'
dic_tipo[17] = 'filme'
dic_preco[17] = 30.00
dic_disp[17] = 'nao'

dic_nome[18] = 'Perdidos no Espaço'
dic_tipo[18] = 'serie'
dic_preco[18] = 35.50
dic_disp[18] = 'sim'

dic_nome[19] = 'O Resgate do Soldado Ryan'
dic_tipo[19] = 'filme'
dic_preco[19] = 30.00
dic_disp[19] = 'sim'

dic_nome[20] = 'The Last Kingdom'
dic_tipo[20] = 'serie'
dic_preco[20] = 35.50
dic_disp[20] = 'nao'


data_global = input("Digite o data de hoje:")
princip_while = 1
while princip_while != 0:
    a = int(input("Digite a opção que você quer:\n1 - Cadastrar produtos\n2 - Buscar Produtos\n3 - Atualizar Produtos\n4 - Relatório de Produtos\n5 - Registrar Compra\n6 - Relátorio de Compras\n7 - Sair "))
    if a == 1:
        cadastro()
    elif a == 2:
        consulta()
    elif a == 3:
        atualizar()
    elif a == 4:
        relatorio()
    elif a == 5:
        regis_comp()
    elif a == 6:
        historico()
    elif a == 7:
        break
    else:
        continue