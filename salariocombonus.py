nome = input()
salario = float(input())
vendas = float(input())
comissao = 0.15 * vendas 
salario_final = comissao + salario 
print("TOTAL = R$ %.2F"%salario_final)