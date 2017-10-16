import sqlite3

connection = sqlite3.connect('teste3.db')

c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tb_customer_account (id_customer integer, cpf_cnpj text, nm_customer text, is_active text, vl_total float, contribuiu)')

create_table()

id = []
cpf = []
nome = []
status = []
saldo = []
contribuiu = int(0)
quem_contribuiu = []
valor_total = 0
valor_geral = 0
opcao = 0
aux = int(0)
aux1 = int(0)
sql = 'SELECT * FROM tb_customer_account'
sql1 = 'SELECT * FROM tb_customer_account WHERE contribuiu = ?'

def read_id(wordUsed):
    for row in c.execute(sql):
        id.append(int(row[0] + 1))
        aux = row[0]
    return aux
aux = read_id(sql)

#def read_cpf(wordUsed):
#    for row in c.execute(sql):
#        print(row[1])
#    return row[1]
#cpf = read_cpf(sql)
print('*** SISTEMA DE CLIENTES TESTE *** ')
while opcao != 3:
    print('''\n           1- Cadastrar cliente
           2- Calcular média dos saldos >560 e de id >1500 e <2700
           3- Sair\n
        ''')
    opcao = int(input('           Opção: '))
    if opcao == 1:
        id.append(int(aux + 1))
        print("Cadastro do {}º cliente (id) na base de dados.".format(aux + 1))
        print("Posição na lista (vetor): {}".format(aux))
        cpf.append(str(input('Digite o cpf: ')))
        nome.append(str(input('Digite o nome: ')))
        status.append(str(input('Digite o status (Ativo ou inativo): ')))
        saldo.append(float(input('Digite o saldo: R$')))
        # print(cpf[aux], nome[aux], status[aux], saldo[aux])
        saldo_aux = saldo[aux1]

        id_aux = id[aux]
        cpf_var = cpf[aux1]
        nome_var = nome[aux1]
        status_var = status[aux1]
        saldo_var = saldo[aux1]
        def dataentry():
            if (saldo_aux >= 560) and (1500 <= id_aux <= 2700):
                c.execute(
                    "INSERT INTO tb_customer_account (id_customer, cpf_cnpj, nm_customer, is_active, vl_total, contribuiu) VALUES (?,?,?,?,?,?)",
                    (id_aux, cpf_var, nome_var, status_var, saldo_var,'s'))
                connection.commit()

            else:
                c.execute("INSERT INTO tb_customer_account (id_customer, cpf_cnpj, nm_customer, is_active, vl_total, contribuiu) VALUES (?,?,?,?,?,?)",
                      (id_aux, cpf_var, nome_var, status_var, saldo_var,'n'))
                connection.commit()
        dataentry()
        if (saldo_aux >= 560) and (1500 <= id_aux <= 2700):
            contribuiu = contribuiu+1
            quem_contribuiu.append(aux)
            valor_total = valor_total + saldo_aux
            print("Este cliente faz parte do cálculo da média.")
        else:
            print("Este cliente NÃO faz parte do cálculo da média.")
        aux1 = aux1 + 1
        valor_geral = valor_geral + saldo_aux
        input('Aperte enter para continuar...')
    elif opcao == 2:
        print("Nº de cliente: {}".format(aux))
        def read_contribuiu(wordUsed):
            for row in c.execute(sql1, (wordUsed)):
                contribuiu_v = row[0]
            return contribuiu_v
        if contribuiu <= 0:
            contribuiu = 0
        else:
            contribuiu = read_contribuiu('s')-1
        print("Nº de clientes que contribuiram para a média: {}".format(contribuiu))
        def read_geral(wordUsed):
            v_total = 0
            for row in c.execute(sql):
                v_total = row[4] + v_total
            return v_total
        valor_geral = read_geral(sql)
        print("Saldo total: {}".format(valor_geral))
        def read_total(wordUsed):
            v_total = 0
            for row in c.execute(sql1, (wordUsed,)):
                v_total = row[4] + v_total
            return v_total
        valor_total = read_total('s')
        print("Saldo total dos clientes que fizeram parte do cálculo da média: {}".format(valor_total))
        if contribuiu <= 0:
            print("Ainda não existe média seguindo as regras propostas.")
        else:
            print("Média: {}".format(valor_total/contribuiu))
        print("Quem contribuiu para a média: ")
        if contribuiu <= 0:
            print("Ninguém.")
        else:
            def read_quem_contribuiu(wordUsed):
                for row in c.execute(sql1, (wordUsed)):
                    q_contribuiu = row
                    print(q_contribuiu)
                return q_contribuiu
            read_quem_contribuiu('s')



        input('Aperte enter para continuar...')
    elif opcao == 3:
        exit()
    else:
        print("Opção inválida.")