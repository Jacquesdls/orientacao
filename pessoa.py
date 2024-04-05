class Pessoa:
    "Isto é uma nova classe chamada Pessoa"
    
    idade = 15
    
    def saudacao(self):
        print("Olá pessoas!!!")
        
print(Pessoa.idade)

objPessoa = Pessoa()
objPessoa.saudacao()
print(objPessoa.idade)
