Calculadora em Python com Tkinter

Este é um projeto de uma calculadora simples desenvolvida em Python utilizando a biblioteca Tkinter para a interface gráfica. A calculadora suporta operações básicas como adição, subtração, multiplicação e divisão.

Funcionalidades
Operações básicas: Adição (+), subtração (-), multiplicação (*) e divisão (/).

Interface gráfica: Interface simples e intuitiva com botões para números e operadores.

Validação de entrada: Verifica se a expressão matemática inserida é válida antes de calcular.

Exibição de resultados: Exibe o resultado formatado ou uma mensagem de erro em caso de expressão inválida.

Como Usar
Pré-requisitos
Python 3.x instalado.

Biblioteca Tkinter (já vem instalada com o Python).

Executando a Calculadora
Clone o repositório ou baixe o arquivo calculadora.py.

Navegue até o diretório onde o arquivo está localizado.

Execute o script Python:

python calculadora.py

Exemplo de Uso
Digite 5 + 3 * 2 na calculadora.

Clique em =.

O resultado exibido será 11 (a calculadora processa as operações sequencialmente).

Estrutura do Código
O código está organizado da seguinte forma:

parse_expression(expression): Converte a string de entrada em uma lista de números e operadores, validando o formato.

calculadora(num1, num2, operador): Executa a operação matemática com base nos números e operador fornecidos.

calcular(): Função chamada quando o botão = é pressionado. Processa a expressão e exibe o resultado ou uma mensagem de erro.

Interface gráfica: Configuração da janela principal, campo de exibição e botões.
