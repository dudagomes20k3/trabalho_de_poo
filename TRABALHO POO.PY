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

agenda = [
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

def cadastrarMedicos():
      #Aqui vai seu codigo 
    print("Você quer cadastar um medico? (sim/não)")
    rm=input("")
    if rm=="sim":
        print("Forneça o nome do médico")
        nomem=input("")
        print("Forneça o CPF do medico")
        cpf= input("")
        print("Qual o RG do medico?")
        rg= input("")
        print("O CRM do medico")
        crm= input("")
        print("O telefone do medico")
        tele= input("")
        print("O endereço do medico")
        ende= input("")
        print("O senha do medico")
        senha= input("")
        print("O sexo do medico")
        exo=input("")
        print("Deseja salvar as informaçoes? (S/N)")
        q=input()
        if q == "sim":
            print("Sucesso")
            medicos.append({"nome": nomem,
                     "cpf": cpf,
                     "rg": rg,
                     "crm": crm,
                    "telefone": tele,
                    "endereco": ende,
                    "sexo": exo,
                    "senha": senha})
            print(medicos)
        else:
            print("Programa cancelado!")
            breakpoint
    else:
      print("Programa cancelado!")
      breakpoint
     
def cadastrarPacientes():
 
    print("Você quer cadastar um paciente? (sim/não)")
    rp=input("")
    if rp=="sim":
     print("Forneça o nome do paciente")
     nomep= input("")
     print("O endereço do paciente")
     endep= input("")
     print("O telefone do paciente")
     telep= input("")
     print("O CPF do paciente")
     cpfp= input("")
     print("Qual o RG do paciente?")
     rgp= input("")
     print("O sexo do paciente")
     sexop= input("")
     print("Informe o convenio do paciente")
     convp = input("")
     print("Deseja salvar as informaçoes?(sim/não)")
     b=input()
     if b == "sim":
         print("Sucesso!")
         pacis.append({
 
             "nome": nomep,
             "endereco": endep,
             "telefone": telep,
             "cpf": cpfp,
             "rg": rgp,
             "sexo": sexop,
             "convenio": convp
     })
         print(pacis)
     
     else:
            print("Programa cancelado!")
            breakpoint
    else:
       print("Programa cancelado!")
       breakpoint
    
def cadastrarConvenios():
  
    print("Você quer cadastar um convênio? (sim/não)")
    rc=input("")
    if rc=="sim":
     print("Forneça o nome do convênio")
     nomec= input("")
     print("O seu telefone para contato")
     telec= input("")
     print("O seu endereço")
     endec= input("")
     print("O CPF do convênio")
     cpfc= input("")
     planos = input("")
     print("Deseja salvar as informaçoes?(sim/não)")
     c=input()
     if c == "sim":
         print("Sucesso!")
         convenios.append({
 
             "nome": nomec,
             "endereco": endec,
             "telefone": telec,
             "palnos": planos
     })
         print(convenios)
     else:
            print("Programa cancelado!")
            breakpoint
    else:
       print("Programa cancelado!")
       breakpoint

def buscarMedicos():

    print("Informe o nome ou CRM do médico")
    busm = input("")
    resultados = [medico for medico in medicos if busm in medico['nome'] or busm in medico['crm']]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CRM: {resultado['crm']}")
    else:
        print("Nenhum médico encontrado.")

def buscarPacientes():

    print("Informe o nome ou CPF do paciente:")
    busp = input("")
    resuls = [paciente for paciente in pacis if busp in paciente['nome'] or busp in paciente['cpf']]
    if resuls:
        for resultado in resuls:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CPF: {resultado['cpf']}")
    else:
        print("Nenhum paciente encontrado.")

def buscarConvenios():
  
    print("Informe o nome ou CNPJ do convênio")
    busc = input("")
    resultados = [convenio for convenio in convenios if busc in convenio['nome'] or busc in convenio['cnpj']]
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

def marcarCompromisso():
  
  print("Você deseja marcar um compromisso?")
  com=input("")
  if com=="sim":
      print("Informe a data que você deseja (formato: DD/MM/AAAA):")
      data=input("")
      print("Informe a hora que você deseja iniciar sua consulta (formato: HH:MM - HH:MM):")
      hi=input("")
      print("Informe a hora que você deseja finalizar sua consulta (formato: HH:MM - HH:MM):")
      hf=input("")
      print("Descreva o seu compromisso")
      desc=input("")
      print("Você deseja salvar essas informações?")
      rc=input("")
      print(f"Seu compromisso foi agendado confira os dados: {agenda}")
  else:
      print("Programa Encerrado")
      breakpoint
  
def marcarConsulta():
    print("Você quer marcar uma consulta?")
    mc = input("")
    if mc == "sim":
        print("Informe o nome do médico:")
        nm = input("")
        mencontrado = next((medico for medico in medicos if medico['nome'] == nm), None)
        if mencontrado:
            print("Informe o nome do paciente:")
            pnome = input("")
            pencontrado = next((paciente for paciente in pacis if paciente['nome'] == pnome), None)
            if pencontrado:
                print("Informe a data da consulta (formato: DD/MM/AAAA):")
                data = input("")
                print("Informe o horário da consulta (formato: HH:MM - HH:MM):")
                horario = input("")
                print("Consulta marcada com sucesso!")
                agenda.append({
                    "data": data,
                    "horario": horario,
                    "medico": nm,
                    "paciente": pnome
                })
            else:
                print("Paciente não encontrado.")
        else:
            print("Médico não encontrado.")
    else:
        print("Programa Cancelado.")

def emitirRelatorio():
 print("Qual relatório você deseja emitir?")
 print("1 - Médicos cadastrados")
 print("2 - Pacientes cadastrados")
 print("3 - Convênios")
 print("4 - Consultas realizadas em um intervalo de data")
 
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
     print("Informe a data de início (formato DD/MM/AAAA):")
     data_inicio = input("")
     data_fim = input("Informe a data de fim (formato DD/MM/AAAA): ")
     print(f"Consultas de {data_inicio} a {data_fim}:")
     for consulta in agenda:
         data_consulta = consulta.get("data", "")
         if data_inicio <= data_consulta <= data_fim:
             print(f"Data: {consulta['data']}, Horário: {consulta.get('horario', consulta.get('hora inicial', ''))}-{consulta.get('hora final', '')}, Médico: {consulta.get('medico', '')}, Paciente: {consulta.get('paciente', '')}, Descrição: {consulta.get('descrição', '')}")
 else:
     print("Opção inválida.")

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
          
        