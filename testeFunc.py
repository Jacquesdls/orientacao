"""
Criação de objetos e chamados dos métodos:    
"""

from Funcionario import func

funcionario = func("antonio", "tonhao@gmail.com")

print(funcionario)

funcionario.cadastro_hora('Jan', 280)
funcionario.cadastro_hora('Feb', 230)
funcionario.cadastro_salario_hora('Jan', 250)
funcionario.cadastro_salario_hora('Jan', 250)
print(funcionario.calcula_salario('Jan'))

print(funcionario.calcula_salario('Feb'))



