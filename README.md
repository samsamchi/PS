# Projetos de Software

- Este é um projeto feito em Python que utiliza a biblioteca Tkinter para a interface gráfica, além de implementar 10 funcionalidades requisitadas pela disciplina, junto com a aplicação dos conceitos de POO.
- O padrões de projetos usados foram: Singleton, Strategy, Template Method.
- O arquivo "sas_ds.py" é o arquivo que contém o código com os padrões de projetos. Para executar basta mudar apenas o nome, conforme explico logo abaixo.

# Aplicação dos Padrões de Projeto (Design Patterns) no código

 # Singleton:
- A classe SAS possui um atributo de classe _instance que será usado para armazenar a única instância da classe.
- O método __new__ é sobrescrito para verificar se já existe uma instância. Se não existir, cria uma nova; se já existir, retorna a instância existente.

 # Strategy:
- Existem três classes de estratégia: SalvarNota , SalvarPagamento e SalvarFolhaPagamento.
- Cada uma dessas classes tem um método salvar, que lida com um tipo específico de dados (nota, pagamento, folha de pagamento). No método salvar , cada classe manipula os dados de forma específica e salva  os dados no arquivo correspondente.
- A classe SAS tem o método set_estrategia para configurar qual estratégia será usada no momento da execução (por exemplo, salvar uma nota, um pagamento ou uma folha de pagamento).

 # Template Method:
- A classe GerenciadorArquivo define dois métodos principais: manipular_arquivo (para ler o conteúdo de um arquivo) e salvar_arquivo (para salvar conteúdo no arquivo).
- Os dois métodos fornecem uma estrutura comum para ler e escrever arquivos, mas os dados que são manipulados no arquivo dependem da estratégia utilizada (nota, pagamento, folha de pagamento).

# Pré-requisitos

- Python 3.x.x;
- Biblioteca Tkinter.
  
# Instruções para Executar

- Clone este repositório para o seu computador:

    ```
    
    git clone https://github.com/samsamchi/PS.git
    
    ```

- Navegue até o diretório do projeto:

    ```
    
    cd PS
    
    ```
    
-  Verifique se o Tkinter está instalado:
  
      ```
    
    python -m tkinter
    
    ```

- Se o Tkinter não estiver instalado, você pode precisar instalá-lo usando o gerenciador de pacotes do Python (pip):

    ```
    
    python -m pip install tk
    
    ```

# Caminho do código:

- No código, o projeto utiliza o caminho específico do meu sistema: c:/Users/cicer/Downloads/ps3/ps3. Se você precisar ajustar este caminho para o seu sistema, abra o arquivo main.py ou qualquer outro arquivo de configuração que dependa desse caminho e modifique o caminho para corresponder ao seu ambiente.

- Execução do projeto:

    ```
    
   python3 c:/Users/cicer/Downloads/ps3/ps3/sas.py
    
    ```
- Execução do projeto (com Padrões de Projeto):

    ```
    
   python3 c:/Users/cicer/Downloads/ps3/ps3/sas_ds.py
    
    ```


  


