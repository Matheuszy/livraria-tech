class Endereco:
    def __init__(self, rua: str, numero: str, bairro: str, cidade: str, estado: str, cep: str):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __composite_values__(self):
        return (self.rua, self.numero, self.bairro, self.cidade, self.estado, self.cep)

    def __repr__(self):
        return f"Endereco(rua={self.rua}, numero={self.numero}, bairro={self.bairro}, cidade={self.cidade}, estado={self.estado}, cep={self.cep})"
