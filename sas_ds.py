import os
import tkinter as tk
from tkinter import messagebox


#  Template Method
class GerenciadorArquivo:
    def __init__(self, caminho):
        self.caminho = caminho

    def manipular_arquivo(self):
        # Tenta ler o arquivo
        if os.path.exists(self.caminho):
            with open(self.caminho, 'r') as f:
                return f.read()  # Retorna o conteúdo do arquivo
        else:
            messagebox.showwarning("Erro", f"Não foi possível acessar o arquivo {self.caminho}.")
            return ""

    def salvar_arquivo(self, conteudo):
        # Tenta salvar no arquivo
        try:
            with open(self.caminho, 'a') as f:
                f.write(conteudo)
            messagebox.showinfo("Sucesso", "Informações salvas com sucesso!")
        except OSError:
            messagebox.showwarning("Erro", f"Não foi possível salvar no arquivo {self.caminho}.")


# Strategy
class SalvarNota:
    def __init__(self, pasta_dados):
        self.caminho = os.path.join(pasta_dados, "notas.txt")

    def salvar(self, matricula, matricula_aluno, nota):
        gerenciador = GerenciadorArquivo(self.caminho)
        conteudo = f"Professor: {matricula}\nAluno: {matricula_aluno} | Nota: {nota}\n\n"
        gerenciador.salvar_arquivo(conteudo)


class SalvarPagamento:
    def __init__(self, pasta_dados):
        self.caminho = os.path.join(pasta_dados, "pagamentos.txt")

    def salvar(self, matricula, aluno, dia, status):
        gerenciador = GerenciadorArquivo(self.caminho)
        conteudo = f"Responsável: {matricula} | Aluno: {aluno}\nPagamento realizado no dia: {dia}\nStatus: {status}\n\n"
        gerenciador.salvar_arquivo(conteudo)


class SalvarFolhaPagamento:
    def __init__(self, pasta_dados):
        self.caminho = os.path.join(pasta_dados, "folha_pagamento.txt")

    def salvar(self, matricula, salario, data):
        gerenciador = GerenciadorArquivo(self.caminho)
        conteudo = f"Funcionário: {matricula} | Salário: {salario} | Data de pagamento: {data}\n\n"
        gerenciador.salvar_arquivo(conteudo)


# Singleton para a classe principal
class SAS:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SAS, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Automação Escolar")
        self.root.geometry("400x400")
        self._estrategia = None
        self._pasta_dados = "c:/Users/cicer/Downloads/ps3/ps3"  # Caminho para os arquivos de dados

    def set_estrategia(self, estrategia):
        self._estrategia = estrategia

    def salvar_dados(self, matricula, *args):
        if self._estrategia:
            self._estrategia.salvar(matricula, *args)

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Menu Principal").pack(pady=20)
        tk.Button(self.root, text="Cadastrar Nota (Professor)", command=lambda: self.cadastrar_nota("1234")).pack(pady=10)
        tk.Button(self.root, text="Registrar Pagamento (Responsável)", command=lambda: self.registrar_pagamento("1234")).pack(pady=10)
        tk.Button(self.root, text="Ver Folha de Pagamento (Funcionário)", command=lambda: self.ver_folha_pagamento("1234")).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def cadastrar_nota(self, matricula):
        self.clear_window()
        
        tk.Label(self.root, text="Digite a matrícula do aluno:").pack(pady=20)
        matricula_aluno_entry = tk.Entry(self.root)
        matricula_aluno_entry.pack(pady=5)

        tk.Label(self.root, text="Digite a nota do aluno:").pack(pady=20)
        nota_entry = tk.Entry(self.root)
        nota_entry.pack(pady=5)
        
        def salvar_nota():
            matricula_aluno = matricula_aluno_entry.get()
            nota = nota_entry.get()
            
            # Usando o strategy 
            self.set_estrategia(SalvarNota(self._pasta_dados))
            self.salvar_dados(matricula, matricula_aluno, nota)
        
        tk.Button(self.root, text="Salvar", command=salvar_nota).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=10)

    def registrar_pagamento(self, matricula):
        self.clear_window()
        
        tk.Label(self.root, text="Digite o nome do aluno:").pack(pady=20)
        aluno_entry = tk.Entry(self.root)
        aluno_entry.pack(pady=5)

        tk.Label(self.root, text="Digite a data de pagamento:").pack(pady=20)
        dia_entry = tk.Entry(self.root)
        dia_entry.pack(pady=5)

        tk.Label(self.root, text="Digite o status do pagamento:").pack(pady=20)
        status_entry = tk.Entry(self.root)
        status_entry.pack(pady=5)
        
        def salvar_pagamento():
            aluno = aluno_entry.get()
            dia = dia_entry.get()
            status = status_entry.get()
            
            # Usando o strategy
            self.set_estrategia(SalvarPagamento(self._pasta_dados))
            self.salvar_dados(matricula, aluno, dia, status)
        
        tk.Button(self.root, text="Salvar", command=salvar_pagamento).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=10)

    def ver_folha_pagamento(self, matricula):
        self.clear_window()
        
        caminho_folha = os.path.join(self._pasta_dados, "folha_pagamento.txt")
        gerenciador_folha = GerenciadorArquivo(caminho_folha)
        
        texto = tk.Text(self.root, wrap=tk.WORD, height=20, width=50)
        texto.pack(pady=10)
        
        conteudo = gerenciador_folha.manipular_arquivo()
        if conteudo:
            texto.insert(tk.END, conteudo)
        
        tk.Button(self.root, text="Voltar", command=self.create_main_menu).pack(pady=20)

    def run(self):
        self.create_main_menu()
        self.root.mainloop()


# Inicialização do sistema
if __name__ == "__main__":
    app = SAS()
    app.run()
