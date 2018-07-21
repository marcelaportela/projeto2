agenda =[] # lista dos professores : agenda([nome, cpf, departamento])
disciplinas=[] #lista das disciplinas : [disciplina,codigo]
alunos =[] #lista dos alunos está dividida em [nome_aluno,cpf_aluno]
turmas=[] #lista das turmas                  # a lista turmas está dividida nos tópicos:  0-codigo_turma
                                             #                                            1-periodo
                                             #                                            2-codigo_disciplina
                                             #                                            3-cpf_professor
                                             #                                            4-lista (lista dos cpfs dos alunos referentes a essa turma)

#------------------------------------------------------------------------------------------------------
def pede_nome():
     return(input("Nome: "))
                                        #pede o nome em geral

#------------------------------------------------------------------------------------------------------
def pede_cpf():
     return(input("CPF: "))
                                       #pede o cpf em geral
#------------------------------------------------------------------------------------------------------

def pede_departamento():
     return(input("Departamento: "))
                                            # pede o nome do departamento do professor

#-----------------------------------------------------------------------------------------------------
def pede_codigo():
    return(input("Código da disciplina"))         #pede o código da disciplina

#----------------------------------------------------------------------------------------------------
def pede_disciplina():
    return(input("Nome da disciplina:"))          # pede o nome da disciplina

#-------------------------------------------------------------------------------------------------------

def pede_codigo_turma():
     return(input("Código da turma:")) # pede o código da turma
#-------------------------------------------------------------------------------------------------------
def pede_periodo():
     return(input("Período:"))

def pede_cpf_professor():
     return(input("CPF do(a) professor(a): "))
def pede_cpf_aluno():
     return(input("CPF do(a) aluno(a): "))
# ver se nome precisa ser nomeprofessor

def mostra_dados_professor(nome, cpf,departamento):
     print("Nome: %s \n CPF: %s \n Departamento: %s \n" % (nome, cpf,departamento))

def mostra_dados_disciplina(disciplina,codigo):
    print("Nome da disciplina: %s \n Código da disciplina: %s " % (disciplina,codigo))
def mostra_dados_alunos(nome_aluno, cpf_aluno):
     print("Nome: %s \n CPF: %s \n" % (nome_aluno, cpf_aluno))
     
def mostra_dados_turma(codigo_turma,periodo,codigo_disciplina,cpf_professor,lista9):
   
     print("Código da turma: %s \n período: %s \n código da disciplina: %s \n CPF do Professor: %s\n" % (codigo_turma,periodo,codigo_disciplina,cpf_professor))
     print("Lista de cpfs dos alunos associados a essa turma:")
     #for z in lista9:
      #    print(z)
     print(lista9)
     print("\n")
     #for p, e in enumerate(lista9):
     #    print(e) não deu certo não sei porque
def pede_nome_arquivo_professores():
     return(input("Nome do arquivo de professores: "))
    
def pede_nome_arquivo_disciplinas():
     return(input("Nome do arquivo de disciplinas: "))
def pede_nome_arquivo_alunos():
     return(input("Nome do arquivo de alunos: "))
def pede_nome_arquivo_turmas():
     return(input("Nome do arquivo de turmas: "))
def pesquisa(nome):
     mnome = nome.lower()
     for p, e in enumerate(agenda):
         if e[0].lower() == mnome:
               return p
     return None
    
def pesquisa_disciplina(disciplina):
     mdisciplina = disciplina.lower()
     for p, e in enumerate(disciplinas):
         if e[0].lower() == mdisciplina:
               return p
     return None
def pesquisa_cpf_professor(cpf_professor):
     mcpf_prof = cpf_professor.lower()
     for p, e in enumerate(agenda):
         if e[1].lower() == mcpf_prof:
               return p
     return None

def pesquisa_codigo_disciplina(codigo):
     mcodigo = codigo
     for p, e in enumerate(disciplinas):
         #print(e[1])
         if e[1].lower() == mcodigo:
              #print(p)
              return p
     return None
def pesquisa_aluno(nome_aluno):
     mnome_aluno = nome_aluno.lower()
     for p, e in enumerate(alunos):
         if e[0].lower() == mnome_aluno:
               return p
     return None
def pesquisa_cpf_aluno(cpf_aluno):
     lista3=[]
     #print("como chega")
     #print(cpf_aluno)
     #print("assim")
     for p, e in enumerate(alunos):
          #print(p)
          #print(e)
          if e[1] in cpf_aluno:
               lista3.append(p)
     if len(lista3)>0:
          return lista3
     #print("como fica")
     #print(e[1])
     #print("não entrou")
     return None
def pesquisa_turma(codigo_turma):
     mcodigo_turma = codigo_turma.lower()
     for p, e in enumerate(turmas):
         if e[0].lower() == mcodigo_turma:
              print(p)
              return p
     return None
def pesquisa_nome_professor(nome_professor):
     mcpf_prof = nome_professor.lower()
     #lista5=[]
     #print(mcpf_prof)
     #print(agenda)
     for p, e in enumerate(agenda):
          g=e[1]
          #print(g)
          if e[0].lower() == mcpf_prof:
              return g     
              
     return None
     
def pesquisa_turmas_por_professor(nome_professor):

     mnome_professor = nome_professor.lower()
     cpf_professor=pesquisa_nome_professor(mnome_professor)     # turmas([codigo_turma,periodo,codigo_disciplina,cpf_professor,lista])
     lista5=[]
     for p, e in enumerate(turmas):
         if e[3].lower() == cpf_professor:
              #print(p)
              j=turmas[p][0]
              lista5.append(j)
              return lista5
     return None
def pesquisa_nome_aluno(nome_aluno):
     mcpf_al = nome_aluno.lower()
     #lista5=[]
     #print(mcpf_prof)
     #print(agenda)
     for p, e in enumerate(alunos):
          g=e[1]
          #print(g)
          if e[0].lower() == mcpf_al:
              return g     
              
     return None
     
def pesquisa_turmas_por_aluno(nome_aluno):

     mnome_aluno = nome_aluno.lower()
     cpf_aluno=pesquisa_nome_aluno(mnome_aluno)     # turmas([codigo_turma,periodo,codigo_disciplina,cpf_professor,lista])
     lista8=[]
     for p, e in enumerate(turmas):
         if cpf_aluno in e[4]:
              #print(p)
              j=turmas[p][0]
              lista8.append(j)
     if len(lista8)>0:
          return lista8
     return None
     
    
def novo():
     global agenda
     nome = pede_nome()
     cpf = pede_cpf()
     departamento=pede_departamento()
     agenda.append([nome, cpf, departamento])
     
def nova_disciplina():
     global disciplinas
     disciplina = pede_disciplina()
    # print(disciplina)
     codigo = pede_codigo()
     #print(codigo)
     disciplinas.append([disciplina,codigo])
    # print(disciplinas)
    
def novo_aluno():
     global alunos
     nome_aluno = pede_nome()
     cpf_aluno = pede_cpf()
     alunos.append([nome_aluno,cpf_aluno])
def nova_turma():
     global turmas
     global lista # lista de cpfs para uma turma tal
     codigo_turma = pede_codigo_turma()
     periodo=pede_periodo()
     codigo_disciplina=pede_codigo()
     cpf_professor=pede_cpf_professor()
     lista2=[]
     print("Diga os cpfs dos alunos associados a essa turma: OBS.: 0 sai \n")
     while True:
          cpf_aluno=pede_cpf_aluno()
          if cpf_aluno=='0':
               break
          else:
               lista2.append(cpf_aluno)
     
     turmas.append([codigo_turma,periodo,codigo_disciplina,cpf_professor,lista2]) #(codigo_turma,periodo,codigo_disciplina,cpf_professor,cpf_aluno)

def apaga():
     global agenda
     nome = pede_nome()
     p = pesquisa(nome)
     if p != None:
         del agenda[p]
     else:
         print("Nome não encontrado.")
def apaga_disciplina():
     global disciplinas
     disciplina = pede_disciplina()
     p = pesquisa_disciplina(disciplina)
     if p != None:
         del disciplinas[p]
     else:
         print("Disciplina não encontrada.")
def apaga_aluno():
     global alunos
     nome_aluno = pede_nome()
     p = pesquisa_aluno(nome_aluno)
     if p != None:
         del alunos[p]
     else:
         print("Nome não encontrado.")
def apaga_turma():
     global turmas
     codigo_turma = pede_codigo_turma()
     p = pesquisa_turma(codigo_turma)
     if p != None:
         del turmas[p]
     else:
         print("Turma não encontrada.")


def altera():
     p = pesquisa(pede_nome())
     if p != None:
         nome = agenda[p][0]
         cpf = agenda[p][1]
         departamento= agenda[p][2]
         print("Encontrado:")
         mostra_dados_professor(nome, cpf, departamento)
         nome = pede_nome()
         cpf = pede_cpf()
         departamento= pede_departamento()
         agenda[p] = [nome, cpf, departamento]
     else:
         print("Nome não encontrado.")

def altera_disciplina():
     p = pesquisa_disciplina(pede_disciplina())
     if p != None:
         disciplina = disciplinas[p][0]
         codigo = disciplinas[p][1]
         print("Encontrado:")
         mostra_dados_disciplina(disciplina,codigo)
         disciplina = pede_disciplina()
         codigo = pede_codigo()
         disciplinas[p] = [disciplina, codigo]
     else:
         print("Nome não encontrado.")


def altera_aluno():
     p = pesquisa_aluno(pede_nome())
     if p != None:
         nome_aluno = alunos[p][0]
         cpf_aluno = alunos[p][1]
         print("Encontrado:")
         mostra_dados_aluno(nome_aluno, cpf_aluno)
         nome_aluno = pede_nome()
         cpf_aluno = pede_cpf()
         alunos[p] = [nome_aluno, cpf_aluno]
     else:
         print("Nome não encontrado.")
         
def altera_turma():
     p = pesquisa_turma(pede_codigo_turma())
     if p != None:
         codigo_turma = turmas[p][0]
         periodo = turmas[p][1]
         codigo_disciplina= turmas[p][2]
         cpf_professor=turmas[p][3]
         lista_cpfs_alunos=turmas[p][4]
         print("Encontrado:")
         mostra_dados_turma(codigo_turma,periodo,codigo_disciplina,cpf_professor,lista_cpfs_alunos)
         
         codigo_turma = pede_codigo_turma()
         periodo = pede_periodo()
         codigo_disciplina= pede_codigo()
         cpf_professor=pede_cpf_professor()
         lista2=[]
         print("Diga os cpfs dos alunos associados a essa turma: OBS.: 0 sai \n")
         while True:
              cpf_aluno=pede_cpf_aluno()
              if cpf_aluno=="0":
                   break
              else:
                   lista2.append(cpf_aluno)
                         #([codigo_turma,periodo,codigo_disciplina,cpf_professor,lista])
         turmas[p] = [codigo_turma,periodo,codigo_disciplina,cpf_professor,lista2]
     else:
         print("Turma não encontrada.")

def lista():
     print("\nProfessores\n\n------")
     for e in agenda:
         mostra_dados_professor(e[0], e[1], e[2])
     print("------\n")
     
def lista_disciplina():
     print("\nDisciplinas\n\n------")
     for e in disciplinas:
         mostra_dados_disciplina(e[0], e[1])
     print("------\n")
     
def lista_alunos():
     print("\nAlunos\n\n------")
     for e in alunos:
         mostra_dados_alunos(e[0], e[1])
     print("------\n")
def lista_turmas():
     print("\nTurmas\n\n------")
     for e in turmas:
         mostra_dados_turma(e[0],e[1],e[2],e[3],e[4])
     print("------\n")
     
def lê():
     global agenda
     global disciplinas
     global alunos
     global turmas
     nome_arquivo_professores = pede_nome_arquivo_professores()
     arquivo_professores = open(nome_arquivo_professores, "r", encoding = "utf-8")
     agenda=[]
     for l in arquivo_professores.readlines():
         nome, cpf, departamento = l.strip().split("#")
         agenda.append([nome, cpf, departamento])
     arquivo_professores.close()
     
     nome_arquivo_disciplinas=pede_nome_arquivo_disciplinas()
     arquivo_disciplinas = open(nome_arquivo_disciplinas, "r", encoding = "utf-8")
     disciplinas=[]
     for l in arquivo_disciplinas.readlines():
         disciplina, codigo = l.strip().split("#")
         disciplinas.append([disciplina, codigo])
     arquivo_disciplinas.close()
     alunos=[]
     nome_arquivo_alunos=pede_nome_arquivo_alunos()
     arquivo_alunos = open(nome_arquivo_alunos, "r", encoding = "utf-8")
     
     for l in arquivo_alunos.readlines():
         nome_aluno, cpf_aluno = l.strip().split("#")
         alunos.append([nome_aluno, cpf_aluno])
     arquivo_alunos.close()                                             #([codigo_turma,periodo,codigo_disciplina,cpf_professor,lista])
     turmas=[]
     nome_arquivo_turmas=pede_nome_arquivo_turmas()
     arquivo_turmas = open(nome_arquivo_turmas, "r", encoding = "utf-8")
     
     for l in arquivo_turmas.readlines():
         codigo_turma,periodo,codigo_disciplina,cpf_professor,lista = l.strip().split("#")
         turmas.append([codigo_turma,periodo,codigo_disciplina,cpf_professor,lista])
     arquivo_turmas.close()  

def grava():
     nome_arquivo_professores = pede_nome_arquivo_professores()
     arquivo_professores = open(nome_arquivo_professores, "w", encoding = "utf-8")
     for e in agenda:
         arquivo_professores.write("%s#%s#%s\n" % (e[0], e[1], e[2]))
     arquivo_professores.close()

def grava_disciplina():
     nome_arquivo_disciplinas = pede_nome_arquivo_disciplinas()
     arquivo_disciplinas = open(nome_arquivo_disciplinas, "w", encoding = "utf-8")
     for e in disciplinas:
         arquivo_disciplinas.write("%s#%s\n" % (e[0], e[1]))
     arquivo_disciplinas.close()

def grava_alunos():
     nome_arquivo_alunos = pede_nome_arquivo_alunos()
     arquivo_alunos = open(nome_arquivo_alunos, "w", encoding = "utf-8")
     for e in alunos:
         arquivo_alunos.write("%s#%s\n" % (e[0], e[1]))
     arquivo_alunos.close()
     
def grava_turmas():
     nome_arquivo_turmas = pede_nome_arquivo_turmas()
     arquivo_turmas = open(nome_arquivo_turmas, "w", encoding = "utf-8")
     for e in turmas:                                                          #([codigo_turma,periodo,codigo_disciplina,cpf_professor,lista])
         arquivo_turmas.write("%s#%s#%s#%s#%s\n" % (e[0], e[1], e[2],e[3],e[4]))
     arquivo_turmas.close()

def ata():
     codigo=pede_codigo() # codigo da disciplina
     lê() # le os arquivos
     indice_disciplina=pesquisa_codigo_disciplina(codigo) # procura o indice da disciplina pra pegar o nome dela

     if indice_disciplina!= None:
          disciplina=disciplinas[indice_disciplina][0]
     else:
          print("none")
     codigo_turma=pede_codigo_turma()
     indice_turma=pesquisa_turma(codigo_turma)
     periodo=turmas[indice_turma][1]
     cpf_professor=turmas[indice_turma][3]
     lista=turmas[indice_turma][4]
     #print(lista)
     indice_professor=pesquisa_cpf_professor(cpf_professor) # procura o indice do cpf do professor pra achar o nome dele
     nome=agenda[indice_professor][0]
     
     
     print("---------------Ata de presença UFRPE---------------")
     
     print("Nome da disciplina: %s"%disciplina)                                  # turmas([codigo_turma,periodo,codigo_disciplina,cpf_professor,lista])
     print("Código da disciplina: %s"%codigo)
     print("Período da turma: %s"%periodo)                                                                           # professores: agenda([nome, cpf, departamento])
     print("Profesor associado: %s"%nome)                                                                      # alunos [nome_aluno,cpf_aluno]
     print ("Lista de alunos:\n")
     #print(lista)
     indice_aluno=pesquisa_cpf_aluno(lista)
     #print(indice_aluno)
     if indice_aluno!= None:
          for e in indice_aluno:
               print("%s | %s"%(alunos[e][0],alunos[e][1]))                                                                           # disciplinas [disciplina,codigo]
     print("---------------------------------------------------")
def turmas_por_professor():
     lê()
     nome_professor=pede_nome()
     #print(nome_professor)
     lista4=pesquisa_turmas_por_professor(nome_professor)
     #print(lista4)
     print("---------------- Listas de turmas do professor(a) %s-----------------\n"%(nome_professor))

     if lista4!=None:
          for e in lista4:
               print(e)
     else:
          print("Professor não encontrado")
     print("--------------------------------------------------------------------\n")

def turmas_por_aluno():
     lê()
     nome_aluno=pede_nome()
     #print(nome_professor)
     lista7=pesquisa_turmas_por_aluno(nome_aluno)
     #print(lista7)
     print("---------------- Listas de turmas do aluno(a) %s-----------------\n"%(nome_aluno))

     if lista7!=None:
          for e in lista7:
               print(e)
     else:
          print("Aluno não encontrado")
     print("--------------------------------------------------------------------\n")


def valida_faixa_inteiro(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
     print("""
   1 - Novo Professor
   2 - Altera Professor
   3 - Apaga Professor
   4 - Lista Professor
   5 - Grava Professor
   6 - Lê Professor
   7 - Nova Disciplina
   8 - Altera Disciplina
   9 - Apaga Disciplina
   10 - Lista Disciplina
   11 - Grava Disciplina
   12 - Lê Disciplina
   13 - Novo aluno
   14 - Altera aluno
   15 - Apaga aluno
   16 - Lista aluno
   17- Grava aluno
   18 - Lê aluno
   19 - Nova turma
   20 - Altera turma
   21 - Apaga turma
   22 - Lista turma
   23 - Grava turma
   24 - Lê turma
   25 - Ata de Disciplina
   26 - Turmas por professor
   27 - Turmas por aluno

   0 - Sai
""")
     return valida_faixa_inteiro("Escolha uma opção: ",0,27)

while True:
     opção = menu()
     if opção == 0:
         break
     elif opção == 1:
         novo()
     elif opção == 2:
         altera()
     elif opção == 3:
         apaga()
     elif opção == 4:
         lista()
     elif opção == 5:
         grava()
     elif opção == 6:
         lê()

     elif opção == 7:
         nova_disciplina()
     elif opção == 8:
         altera_disciplina()
     elif opção == 9:
         apaga_disciplina()
     elif opção == 10:
         lista_disciplina()
     elif opção == 11:
         grava_disciplina()
     elif opção == 12:
         lê()

     elif opção == 13:
         novo_aluno()
     elif opção == 14:
         altera_aluno()
     elif opção == 15:
         apaga_aluno()
     elif opção == 16:
         lista_alunos()
     elif opção == 17:
         grava_alunos()
     elif opção == 18:
         lê()

     elif opção == 19:
         nova_turma()
     elif opção == 20:
         altera_turma()
     elif opção == 21:
         apaga_turma()
     elif opção == 22:
         lista_turmas()
     elif opção == 23:
         grava_turmas()
     elif opção == 24:
         lê()
     elif opção == 25:
         ata()
     elif opção == 26:
         turmas_por_professor()
     elif opção == 27:
         turmas_por_aluno()
