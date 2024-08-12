import tkinter as tk
from tkinter import messagebox
import os
import random

class SAS:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("School Administration System")

        self.pasta_dados = "c:/Users/cicer/Downloads/ps3/ps3"
        #if not os.path.exists(self.pasta_dados):
            #os.makedirs(self.pasta_dados)

        self.check_directory(self.pasta_dados)

        self.create_main_menu()

    def check_directory(self, path): #tratamento de exceções para ver se existe um diretório onde serao salvos os dados
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError as e:
            messagebox.showerror("Erro", f"Não foi possível criar o diretório: {e}")
            self.root.quit()

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Seja Bem-Vindo(a)!").pack(pady=20)
        
        tk.Button(self.root, text="Aluno(a)", command=self.menu_aluno).pack(pady=10)
        tk.Button(self.root, text="Professor(a)", command=self.menu_professor).pack(pady=10)
        tk.Button(self.root, text="Funcionário(a)", command=self.menu_funcionario).pack(pady=10)
        tk.Button(self.root, text="Responsável", command=self.menu_responsavel).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def menu_aluno(self):
        self.clear_window()
        tk.Label(self.root, text="Seja bem-vindo, Aluno(a)!").pack(pady=20)
        tk.Button(self.root, text="Já possuo cadastro", command=lambda: self.cadastro_existente('aluno')).pack(pady=10)
        tk.Button(self.root, text="Novo cadastro", command=lambda: self.novo_cadastro('aluno')).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=10)

    def menu_professor(self):
        self.clear_window()
        tk.Label(self.root, text="Seja bem-vindo, Professor(a)!").pack(pady=20)
        tk.Button(self.root, text="Já possuo cadastro", command=lambda: self.cadastro_existente('professor')).pack(pady=10)
        tk.Button(self.root, text="Novo cadastro", command=lambda: self.novo_cadastro('professor')).pack(pady=10)
        tk.Button(self.root, text = "Voltar", command=self.create_main_menu).pack(pady=10)

    def menu_funcionario(self):
        self.clear_window()
        tk.Label(self.root, text="Seja bem-vindo, Funcionário(a)!").pack(pady=20)
        tk.Button(self.root, text="Já possuo cadastro", command=lambda: self.cadastro_existente('funcionario')).pack(pady=10)
        tk.Button(self.root, text="Novo cadastro", command=lambda: self.novo_cadastro('funcionario')).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=10)

    def menu_responsavel(self):
        self.clear_window()
        tk.Label(self.root, text="Seja bem-vindo, Responsável!").pack(pady=20)
        tk.Button(self.root, text="Já possuo cadastro", command=lambda: self.cadastro_existente('responsavel')).pack(pady=10)
        tk.Button(self.root, text="Novo cadastro", command=lambda: self.novo_cadastro('responsavel')).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=10)


    def cadastro_existente(self, tipo):
        self.clear_window()
        arquivos = {
            'aluno': "alunos.txt",
            'professor': "professores.txt",
            'funcionario': "funcionarios.txt",
            'responsavel': "responsaveis.txt"
        }
        arquivo = os.path.join(self.pasta_dados, arquivos[tipo])

        tk.Label(self.root, text=f"Digite seu número de matrícula ({tipo}):").pack(pady=20)
        matricula_entry = tk.Entry(self.root)
        matricula_entry.pack(pady=10)


        def buscar_matricula():
            matricula = matricula_entry.get()
            if os.path.exists(arquivo):
                with open(arquivo, 'r') as f:
                    encontrado = False
                    for linha in f:
                        if linha.startswith(matricula):
                            messagebox.showinfo("Cadastro Encontrado", linha)
                            encontrado = True
                            if tipo == 'responsavel':
                                self.acoes_responsavel(matricula)

                            if tipo == 'professor':
                                self.acoes_professor(matricula)

                            break

                    if not encontrado:
                        messagebox.showwarning("Erro", "Matrícula não encontrada.")
            else:
                messagebox.showwarning("Erro", "Nenhum arquivo txt encontrado.")

        tk.Button(self.root, text="Buscar", command=buscar_matricula).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=10)

    def acoes_responsavel(self, matricula):
            self.clear_window()
            tk.Button(self.root, text="Ver Frequência do aluno(a)", command=lambda: self.ver_frequencia(matricula)).pack(pady=20)
            tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=20)

    def ver_frequencia(self, matricula):
            self.clear_window()
            arquivos = {'frequencia': "frequencia.txt"}
            arquivo = os.path.join(self.pasta_dados, arquivos['frequencia'])
        
            texto = tk.Text(self.root, wrap=tk.WORD, height=20, width=50)
            texto.pack(pady=10)
            
            try: #tratamento de exceções para verificar se o arquivo de frequencia existe no diretorio
                if os.path.exists(arquivo):
                    with open(arquivo, 'r') as f:
                        conteudo = f.read()
                        texto.insert(tk.END, conteudo)
            except OSError:
                messagebox.showwarning("Erro", f"Não foi possível acessar esse arquivo, verifique se existe no diretório!")

            tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=20)

    def acoes_professor(self, matricula):
            self.clear_window()
            tk.Button(self.root, text="Cadastrar Avaliação", command=lambda: self.cadastrar_prova(matricula)).pack(pady=20)
            tk.Button(self.root, text="Cadastrar Disciplina e Horário", command=lambda: self.cadastrar_aulas(matricula)).pack(pady=20)
            tk.Button(self.root, text="Cadastrar Frequência", command=lambda: self.cadastrar_frequencia(matricula)).pack(pady=20)
            tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=20)

    def cadastrar_prova(self, matricula):
        self.clear_window()
        tk.Label(self.root, text=f"Digite o nome da sua disciplina:").pack(pady=20)
        disciplinaprova_entry = tk.Entry(self.root)
        disciplinaprova_entry.pack(pady=5)

        tk.Label(self.root, text=f"Digite o dia da avaliação:").pack(pady=20)
        diaprova_entry = tk.Entry(self.root)
        diaprova_entry.pack(pady=5)

        tk.Label(self.root, text=f"Digite o horário da avaliação:").pack(pady=20)
        horarioprova_entry = tk.Entry(self.root)
        horarioprova_entry.pack(pady=5)

        def salvar_avaliacoes():
            disciplinaprova = disciplinaprova_entry.get()
            diaprova = diaprova_entry.get()
            horarioprova = horarioprova_entry.get()
            arquivo_aulas = os.path.join(self.pasta_dados, "avaliacoes.txt")
            
            try: #tratamento de exceções para salvar informações sobre as provas
                with open(arquivo_aulas, 'a') as f:
                    f.write(f"{matricula},{disciplinaprova},{diaprova},{horarioprova}\n")
                messagebox.showinfo("Avaliação cadastrada com sucesso!")
            except OSError:
                 messagebox.showwarning("Erro", f"Não foi possível salvar as informações nesse arquivo, verifique se existe no diretório!")

        tk.Button(self.root, text="Salvar", command=salvar_avaliacoes).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=10)

    def cadastrar_aulas(self, matricula):
        self.clear_window()
        tk.Label(self.root, text=f"Digite o nome da sua disciplina:").pack(pady=20)
        disciplina_entry = tk.Entry(self.root)
        disciplina_entry.pack(pady=5)

        tk.Label(self.root, text=f"Digite o horário da sua disciplina:").pack(pady=20)
        horario_entry = tk.Entry(self.root)
        horario_entry.pack(pady=5)

        def salvar_aulas():
            disciplina = disciplina_entry.get()
            horario = horario_entry.get()
            arquivo_aulas = os.path.join(self.pasta_dados, "aulas.txt")
            
            try: #tratamento de exceção para salvar as informaçoes da disciplinas e horario das aulas ministradas pelo professor
                with open(arquivo_aulas, 'a') as f:
                    f.write(f"{matricula},{disciplina},{horario}\n")
                messagebox.showinfo("Aula cadastrada com sucesso!")
            except OSError:
                messagebox.showwarning("Erro", f"Não foi possível salvar as informações nesse arquivo, verifique se existe no diretório!")


        tk.Button(self.root, text="Salvar", command=salvar_aulas).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=10)

    def cadastrar_frequencia(self, matricula):
        self.clear_window()
        arquivos = {'aluno': "alunos.txt"}
        arquivo = os.path.join(self.pasta_dados, arquivos['aluno'])
        
        texto = tk.Text(self.root, wrap=tk.WORD, height=20, width=50)
        texto.pack(pady=10)

        try: #tratamento de exceção para verificar se o arquivo aluno.txt existe no diretorio
            if os.path.exists(arquivo):
                with open(arquivo, 'r') as f:
                    conteudo = f.read()
                    texto.insert(tk.END, conteudo)
        except OSError:
            messagebox.showwarning("Erro", f"Não foi possível acessar o arquivo, verifique se existe no diretório!")

        tk.Label(self.root, text=f"Digite a data de hoje:").pack(pady=20)
        dia_entry = tk.Entry(self.root)
        dia_entry.pack(pady=5)

        tk.Label(self.root, text=f"Digite a matrícula junto com a quantidade de faltas por aula do aluno(a) hoje:").pack(pady=20)
        faltas_entry = tk.Entry(self.root)
        faltas_entry.pack(pady=5)

        def salvar_frequencia():
            dia = dia_entry.get()
            faltas = faltas_entry.get()
            arquivo_frequencia = os.path.join(self.pasta_dados, "frequencia.txt")
            
            try: #tratamento de exceção para frequencia dos alunos
                with open(arquivo_frequencia, 'a') as f:
                    f.write(f"{matricula} | {dia}\n{faltas}\n\n")
                messagebox.showinfo("Frequência cadastrada com sucesso!")
            except OSError:
                messagebox.showwarning("Erro", f"Não foi possível salvar as informações nesse arquivo, verifique se existe no diretório!")

        tk.Button(self.root, text="Salvar", command=salvar_frequencia).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=10)
        
    def novo_cadastro(self, tipo):
        self.clear_window()
        arquivos = {
            'aluno': "alunos.txt",
            'professor': "professores.txt",
            'funcionario': "funcionarios.txt",
            'responsavel': "responsaveis.txt"
        }
        arquivo = os.path.join(self.pasta_dados, arquivos[tipo])

        tk.Label(self.root, text=f"Novo cadastro de {tipo}").pack(pady=20)
        tk.Label(self.root, text="Nome Completo:").pack(pady=5)
        nome_entry = tk.Entry(self.root)
        nome_entry.pack(pady=5)

        tk.Label(self.root, text="Idade:").pack(pady=5)
        idade_entry = tk.Entry(self.root)
        idade_entry.pack(pady=5)

        tk.Label(self.root, text="Sexo (F/M):").pack(pady=5)
        sexo_entry = tk.Entry(self.root)
        sexo_entry.pack(pady=5)

        tk.Label(self.root, text="Observação Médica (Sim/Não):").pack(pady=5)
        saude_entry = tk.Entry(self.root)
        saude_entry.pack(pady=5)

        tk.Label(self.root, text="Se sim, descreva suas observações:").pack(pady=5)
        descricao_saude_entry = tk.Entry(self.root)
        descricao_saude_entry.pack(pady=5)

        def salvar_cadastro():
            nome = nome_entry.get()
            idade = idade_entry.get()
            sexo = sexo_entry.get()
            saude = saude_entry.get().lower()
            descricao_saude = descricao_saude_entry.get() if saude == 'sim' else "Não possuo observações médicas."

            matricula = str(random.randint(1000, 9999))

            try: #tratamento de exceção para info de aluno, resp, func, e prof
                with open(arquivo, 'a') as f:
                    f.write(f"{matricula},{nome},{idade},{sexo},{descricao_saude}\n")
                messagebox.showinfo("Cadastro Realizado", f"Cadastro realizado com sucesso! Seu número de matrícula é: {matricula}")
            except OSError:
                messagebox.showwarning("Erro", f"Não foi possível salvar as informações nesse arquivo, verifique se existe no diretório!")

        tk.Button(self.root, text="Salvar", command=salvar_cadastro).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=10)

    def run(self):
        self.root.mainloop()

sistema = SAS()
sistema.run()
