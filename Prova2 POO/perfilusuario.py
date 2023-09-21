class PerfilUsuario:
    def __init__(self, UsuarioRedeSocial):
        self.UsuarioRedeSocial = UsuarioRedeSocial
        self.descricao = ""
        self.interesses = []
    
    def definir_descricao(self, descricao):
        self.descricao = descricao
    
    def adicionar_interesse(self, interesse):
        self.interesses.append(interesse)
    
    def obter_descricao(self):
        return self.descricao
    
    def listar_interesses(self):
        return self.interesses