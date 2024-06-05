from datetime import datetime
import re

medicos = [
    {
        "nome": "Adalberto",
        "cpf": "12345678900",
        "rg": "MG123456",
        "crm": "CRM1234",
        "telefone": "(88) 99999-1234",
        "endereco": "Rua A, 123, Belo Horizonte",
        "sexo": "Masculino",
        "senha": "senha123"
    },
    {
        "nome": "Ray",
        "cpf": "98765432100",
        "rg": "SP987654",
        "crm": "CRM5678",
        "telefone": "(88) 99999-5678",
        "endereco": "Avenida B, 456, São Paulo",
        "sexo": "Masculino",
        "senha": "456"
    }
]
pacis = [
    {
        "nome": "Ana Luiza",
        "cpf": "11122233344",
        "rg": "MG111222",
        "telefone": "(31) 88888-1111",
        "endereco": "Rua C, 789, Belo Horizonte",
        "sexo": "Masculino",
        "convenio": "ConvenioX"
    },
    {
        "nome": "Duda Gomes",
        "cpf": "55566677788",
        "rg": "SP555666",
        "telefone": "(11) 88888-2222",
        "endereco": "Avenida D, 101, São Paulo",
        "sexo": "Feminino",
        "convenio": "ConvenioY"
    }
]
convenios = [
    {
        "nome": "ConvenioX",
        "telefone": "(31) 77777-3333",
        "endereco": "Rua E, 202, Belo Horizonte",
        "cnpj": "12345678000100",
        "planos": "Plano A, Plano B"
    },
    {
        "nome": "ConvenioY",
        "telefone": "(11) 77777-4444",
        "endereco": "Avenida F, 303, São Paulo",
        "cnpj": "98765432000100",
        "planos": "Plano C, Plano D"
    }
]

consultas = [
    {   
        "medico": "Dr. Adalberto",
        "paciente":"Sara V.",
        "data" : "16/09/2025",
        "hora inicial" : "12:00",
        "hora final" : "1:00",
        "descrição" : "consulta do ouvido"
    },
        {
            
        "medico": "Dr. Adalberto",
        "paciente":"Sara V.",
        "data" : "16/09/2024",
        "hora inicial" : "1:00",
        "hora final" : "5:00",
        "descrição" : "consulta braço"
    },
        {

        "medico": "Dr. Adalberto",
        "paciente":"Sara V.",
        "data" : "16/09/2026",
        "hora inicial" : "2:00",
        "hora final" : "3:00",
        "descrição" : "consulta da cabeça"
    }
]

compromissos = [
    {
        "data": "16/09/2024",
        "hora inicial": "10:00",
        "hora final": "11:00",
        "descrição": "Reunião com equipe"
    },
    {
        "data": "17/09/2024",
        "hora inicial": "14:00",
        "hora final": "15:00",
        "descrição": "Treinamento de software"
    }
]
def validar_nome(nome):
    return bool(re.match("^[a-zA-ZÀ-ú]+( [a-zA-ZÀ-ú]+)*$", nome))

def validar_data(data_str):
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    

def validar_horario(horario_str):
    try:
        datetime.strptime(horario_str, '%H:%M')
        return True
    except ValueError:
        return False

def validar_cpf(cpf):
    if len(cpf) != 11:
        return False
    if not cpf.isdigit():
        return False
    
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0
    
    if int(cpf[9]) != digito_1:
        return False
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito_2 = 11 - (soma % 11)
    if digito_2 > 9:
        digito_2 = 0
    
    if int(cpf[10]) != digito_2:
        return False
    
    return True

def validar_telefone(telefone):
    telefone = ''.join(filter(str.isdigit, telefone))
    
    if len(telefone) != 11:
        return False
    
    if telefone[:2] != '0':
        return False
    
    if telefone[2] != '9':
        return False
    
    return True

def validar_descricao(descricao):
    return len(descricao.strip()) > 0

def validar_rg(rg):
    if len(rg) != 9 or not rg.isdigit():
        return False
    
    return True

def cadastrarMedicos():
    print("Você quer cadastrar um médico? Digite: S para sim e N para não.")
    resposta = input("").upper()
    if resposta == "S":
        print("Forneça o nome do médico:")
        nome = input("")
        if not validar_nome(nome):
            print("Nome inválido. Por favor, insira um nome válido.")
            return
        
        print("Forneça o CPF do médico:")
        cpf = input("")
        if not validar_cpf(cpf):
            print("CPF inválido. Por favor, insira um CPF válido.")
            return
        
        print("Qual o RG do médico?")
        rg = input("")
        print("O CRM do médico:")
        crm = input("")
        print("O telefone do médico:")
        telefone = input("")
        if not validar_telefone(telefone):
            print("Telefone inválido. Por favor, insira um telefone válido.")
            return
        
        print("O endereço do médico:")
        endereco = input("")
        print("A senha do médico:")
        senha = input("")
        print("O sexo do médico:")
        sexo = input("")
        print("Deseja salvar as informações? Digite: S para sim e N para não.")
        salvar = input("").upper()
        if salvar == "S":
            print("Sucesso!")
            medicos.append({
                "nome": nome,
                "cpf": cpf,
                "rg": rg,
                "crm": crm,
                "telefone": telefone,
                "endereco": endereco,
                "sexo": sexo,
                "senha": senha
            })
            print(medicos)
        else:
            print("Operação cancelada!")
    else:
        print("Operação cancelada!")

def cadastrarPacientes():
    print("Você quer cadastrar um paciente? Digite: S para sim e N para não.")
    resposta = input("").upper()
    if resposta == "S":
        print("Forneça o nome do paciente:")
        nome = input("")
        print("O endereço do paciente:")
        endereco = input("")
        print("O telefone do paciente:")
        telefone = input("")
        if not validar_telefone(telefone):
            print("Telefone inválido. Por favor, insira um telefone válido.")
            return
        
        print("O CPF do paciente:")
        cpf = input("")
        if not validar_cpf(cpf):
            print("CPF inválido. Por favor, insira um CPF válido.")
            return
        
        print("Qual o RG do paciente?")
        rg = input("")
        print("O sexo do paciente:")
        sexo = input("")
        print("Informe o convênio do paciente:")
        convenio = input("")
        print("Deseja salvar as informações? Digite: S para sim e N para não.")
        salvar = input("").upper()
        if salvar == "S":
            print("Sucesso!")
            pacis.append({
                "nome": nome,
                "endereco": endereco,
                "telefone": telefone,
                "cpf": cpf,
                "rg": rg,
                "sexo": sexo,
                "convenio": convenio
            })
            print(pacis)
        else:
            print("Operação cancelada!")
    else:
        print("Operação cancelada!")

def cadastrarConvenios():
    print("Você quer cadastrar um convênio? Digite: S para sim e N para não.")
    resposta = input("").upper()
    if resposta == "S":
        print("Forneça o nome do convênio:")
        nome = input("")
        print("O telefone para contato:")
        telefone = input("")
        if not validar_telefone(telefone):
            print("Telefone inválido. Por favor, insira um telefone válido.")
            return
        
        print("O endereço do convênio:")
        endereco = input("")
        print("O CNPJ do convênio:")
        cnpj = input("")
        if not validar_cpf(cnpj):
            print("CNPJ inválido. Por favor, insira um CNPJ válido.")
            return
        
        print("Informe os planos do convênio:")
        planos = input("")
        print("Deseja salvar as informações? Digite: S para sim e N para não.")
        salvar = input("").upper()
        if salvar == "S":
            print("Sucesso!")
            convenios.append({
                "nome": nome,
                "endereco": endereco,
                "telefone": telefone,
                "cnpj": cnpj,
                "planos": planos
            })
            print(convenios)
        else:
            print("Operação cancelada!")
    else:
        print("Operação cancelada!")

def buscarMedicos():
    print("Informe o nome ou CRM do médico:")
    busm = input("")
    resultados = [medico for medico in medicos if busm.lower() == medico.get('nome', '').lower() or busm == medico.get('crm', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CRM: {resultado['crm']}")
    else:
        print("Nenhum médico encontrado.")

def buscarPacientes():
    print("Informe o nome ou CPF do paciente:")
    busp = input("")
    resultados = [paciente for paciente in pacis if busp.lower() == paciente.get('nome', '').lower() or busp == paciente.get('cpf', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CPF: {resultado['cpf']}")
    else:
        print("Nenhum paciente encontrado.")

def buscarConvenios():
    print("Informe o nome ou CNPJ do convênio:")
    busc = input("")
    resultados = [convenio for convenio in convenios if busc.lower() == convenio.get('nome', '').lower() or busc == convenio.get('cnpj', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CNPJ: {resultado['cnpj']}")
    else:
        print("Nenhum convênio encontrado.")

def alterarMedicos():
  
  print("Informe o CRM do médico a ser alterado")
  crm = input("")
  medico = next((medico for medico in medicos if medico['crm'] == crm), None)
  if medico:
        print(f"Dados atuais: {medico}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        nome = input(f"Nome ({medico['nome']}): ") or medico['nome']
        cpf = input(f"CPF ({medico['cpf']}): ") or medico['cpf']
        rg = input(f"RG ({medico['rg']}): ") or medico['rg']
        telefone = input(f"Telefone ({medico['telefone']}): ") or medico['telefone']
        endereco = input(f"Endereço ({medico['endereco']}): ") or medico['endereco']
        sexo = input(f"Sexo ({medico['sexo']}): ") or medico['sexo']
        senha = input(f"Senha ({medico['senha']}): ") or medico['senha']
        medico.update({
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereco,
            "sexo": sexo,
            "senha": senha
        })
        print("Dados do médico atualizados.")
        print(medicos)
  else:
        print("Médico não encontrado.")

def alterarPacientes():

    print("Informe o CPF do paciente a ser alterado")
    cpf = input("")
    paciente = next((paciente for paciente in pacis if paciente['cpf'] == cpf), None)
    if paciente:
        print(f"Dados atuais: {paciente}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        nome = input(f"Nome ({paciente['nome']}): ") or paciente['nome']
        rg = input(f"RG ({paciente['rg']}): ") or paciente['rg']
        telefone = input(f"Telefone ({paciente['telefone']}): ") or paciente['telefone']
        endereco = input(f"Endereço ({paciente['endereco']}): ") or paciente['endereco']
        sexo = input(f"Sexo ({paciente['sexo']}): ") or paciente['sexo']
        convenio = input(f"Convênio ({paciente['convenio']}): ") or paciente['convenio']
        paciente.update({
            "nome": nome,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereco,
            "sexo": sexo,
            "convenio": convenio
        })
        print("Dados do paciente atualizados.")
    else:
        print("Paciente não encontrado.")

def validar_data(data_str):
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    
def marcarCompromisso():
    print("Você deseja marcar um compromisso? Digite: S para sim E N para não.")
    com = input("")
    if com.lower() == "S":
        data = input("Informe a data do compromisso (formato DD/MM/AAAA): ")
        if not validar_data(data):
            print("Data inválida. Encerrando o programa.")
            return
        
        hi = input("Informe a hora inicial do compromisso (formato HH:MM): ")
        hf = input("Informe a hora final do compromisso (formato HH:MM): ")
        desc = input("Descreva o seu compromisso: ")
        
        compromissos.append({
            "data": data,
            "hora inicial": hi,
            "hora final": hf,
            "descrição": desc
        })
        print("Compromisso marcado com sucesso!")
        print(f"Seu compromisso foi agendado com os seguintes dados: {compromissos[-1]}")
    else:
        print("Programa cancelado!")

def marcarConsulta():
    print("Você quer marcar uma consulta? (sim/não)")
    mc = input("")
    if mc.lower() == "sim":
        nm = input("Informe o nome do médico: ")
        mencontrado = next((medico for medico in medicos if medico['nome'] == nm), None)
        if mencontrado:
            pnome = input("Informe o nome do paciente: ")
            pencontrado = next((paciente for paciente in pacis if paciente['nome'] == pnome), None)
            if pencontrado:
                data = input("Informe a data da consulta (formato DD/MM/AAAA): ")
                if not validar_data(data):
                    print("Data inválida. Encerrando o programa.")
                    return
                
                hi = input("Informe a hora inicial da consulta (formato HH:MM): ")
                hf = input("Informe a hora final da consulta (formato HH:MM): ")
                desc = input("Descreva a consulta: ")
                
                consultas.append({
                    "data": data,
                    "hora inicial": hi,
                    "hora final": hf,
                    "medico": nm,
                    "paciente": pnome,
                    "descrição": desc
                })
                print("Consulta marcada com sucesso!")
                print(f"Os dados da consulta são: {consultas[-1]}")
            else:
                print("Paciente não encontrado.")
        else:
            print("Médico não encontrado.")
    else:
        print("Programa cancelado!")

def emitirRelatorio():
    print("Qual relatório você deseja emitir?")
    print("1 - Médicos cadastrados")
    print("2 - Pacientes cadastrados")
    print("3 - Convênios")
    print("4 - Consultas realizadas em um intervalo de data")
    print("5 - Compromissos realizados em um intervalo de data")
    
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print("Médicos cadastrados:")
        for medico in medicos:
            print(f"Nome: {medico['nome']}, CPF: {medico['cpf']}, CRM: {medico['crm']}, Telefone: {medico['telefone']}")
    elif escolha == "2":
        print("Pacientes cadastrados:")
        for paciente in pacis:
            print(f"Nome: {paciente['nome']}, CPF: {paciente['cpf']}, Telefone: {paciente['telefone']}")
    elif escolha == "3":
        print("Convênios:")
        for convenio in convenios:
            print(f"Nome: {convenio['nome']}, CNPJ: {convenio['cnpj']}, Telefone: {convenio['telefone']}")
    elif escolha == "4":
        data_inicio = input("Informe a data de início (formato DD/MM/AAAA): ")
        if not validar_data(data_inicio):
            print("Data de início inválida. Encerrando o programa.")
            return
        
        data_fim = input("Informe a data de fim (formato DD/MM/AAAA): ")
        if not validar_data(data_fim):
            print("Data de fim inválida. Encerrando o programa.")
            return
        
        print(f"Consultas de {data_inicio} a {data_fim}:")
        for consulta in consultas:
            data_consulta = consulta.get("data", "")
            if data_inicio <= data_consulta <= data_fim:
                print(f"Data: {consulta['data']}, Horário: {consulta['hora inicial']}-{consulta['hora final']}, Médico: {consulta['medico']}, Paciente: {consulta['paciente']}, Descrição: {consulta['descrição']}")
    elif escolha == "5":
        data_inicio = input("Informe a data de início (formato DD/MM/AAAA): ")
        if not validar_data(data_inicio):
            print("Data de início inválida. Por favor reinicie o encerre o programa.")
            return
        
        data_fim = input("Informe a data de fim (formato DD/MM/AAAA): ")
        if not validar_data(data_fim):
            print("Data de fim inválida. Por favor reinicie o encerre o programa.")
            return
        
        print(f"Compromissos de {data_inicio} a {data_fim}:")
        for compromisso in compromissos:
            data_compromisso = compromisso.get("data", "")
            if data_inicio <= data_compromisso <= data_fim:
                print(f"Data: {compromisso['data']}, Horário: {compromisso['hora inicial']}-{compromisso['hora final']}, Descrição: {compromisso['descrição']}")
    else:
        print("Opção inválida. Encerrando o programa.")

a = True
while a:
   
   lang = input("1 - Cadastrar Médico\n"
                "2 - Cadastrar Paciente\n"
                "3 - Cadastrar Convênio\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer?")
   match lang:
       
    case "1":
        cadastrarMedicos()
        
    case "2":
        cadastrarPacientes()

    case "3": 
        cadastrarConvenios()
        
    case "4":
        buscarMedicos()
        
    case "5":
        buscarPacientes()
        
    case "6":
        buscarConvenios()
      
    case "7":
        alterarMedicos()
        
    case "8":
        alterarPacientes()
        
    case "9":
        marcarCompromisso()
        
    case "10":
        marcarConsulta()
        
    case "11":
        emitirRelatorio()
             
    case "12":
           a = False
        
    case _:
           print("Escolha uma opção válida")     
