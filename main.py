import tkinter as tk

def parse_expression(expression):
    """Converte a string de entrada em uma lista de números e operadores."""
    tokens = []
    current_number = ''
    for char in expression:
        if char in '+-*/':
            if not current_number:  # Operador sem número antes
                return None
            try:
                num = float(current_number)
            except ValueError:
                return None
            tokens.append(num)
            tokens.append(char)
            current_number = ''
        elif char.isdigit() or char == '.':
            current_number += char
        else:  # Caractere inválido
            return None
    
    # Adiciona o último número
    if current_number:
        try:
            num = float(current_number)
        except ValueError:
            return None
        tokens.append(num)
    
    # Valida formato: número seguido por pares operador-número
    if not tokens or len(tokens) % 2 == 0:
        return None
    return tokens

def calculadora(num1, num2, operador):
    """Executa a operação matemática e retorna o resultado."""
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2 if num2 != 0 else None
    return None

def calcular():
    """Função chamada quando o botão '=' é pressionado."""
    expressao = display.get().replace('=', '').strip()  # Remove o '=' final
    
    tokens = parse_expression(expressao)
    if not tokens:
        display.delete(0, tk.END)
        display.insert(0, "Erro!")
        return
    
    resultado = tokens[0]
    
    # Processa cada operação sequencialmente
    for i in range(1, len(tokens), 2):
        if i + 1 >= len(tokens):
            display.delete(0, tk.END)
            display.insert(0, "Erro!")
            return
        
        operador = tokens[i]
        num = tokens[i + 1]
        
        resultado = calculadora(resultado, num, operador)
        if resultado is None:
            break
    
    # Exibe o resultado ou mensagem de erro
    display.delete(0, tk.END)
    if resultado is not None:
        display.insert(0, f"{resultado:.10g}")  # Formatação inteligente
    else:
        display.insert(0, "Erro!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora")

display = tk.Entry(
    root,
    width=25,
    font=("Arial", 16),
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
for botao in botoes:
    if botao == '=':
        comando = calcular
    else:
        comando = lambda b=botao: display.insert(tk.END, b)
    
    tk.Button(
        root,
        text=botao,
        width=5,
        height=2,
        font=("Arial", 14),
        command=comando
    ).grid(row=row, column=col, padx=2, pady=2)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()     