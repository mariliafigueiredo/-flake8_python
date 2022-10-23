class filanormal:
    codigo:int = 0            #código inicia em 0
    fila = []
    clientesatendidos = []
    senhatual:str = ""

    def gerasenhaatual(self)->None:
        self.senhaatual = f'NM{self.codigo}'

    def resetafila(self)->None:        # vai verificar o valor do código, caso seja maior do que 100, vai igualar a 0
        if self.codigo >= 100:         # o límite do código é 100
            self.codigo = 0

        else:
            self.codigo += 1

    def atualizafila(self)->None:
        self.resetafila()                      # metodo reseta fila vai fazer a verificação do código
        self.gerasenhaatual()                  # vai chamar gerasenhaatual que vai pegar o código e adicionar um sufixo a ele como "NM" indicando que é fila normal
        self.fila.append(self.senhaatual)      # vai pegar senha atual e inserir dentro do array fila e com isso vou saber do primeiro ao último cliente que chegou na agência

    def chamacliente(self, caixa:int)->str:
        cliente_atual:str = self.fila.pop(0)                 #vai pegar o primeiro item do array
        self.clientesatendidos.append(cliente_atual)    #tirei o cliente da fila e coloquei na lista de clientes atendidos
        return(f'cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')