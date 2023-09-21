from usuarioredesocial import UsuarioRedeSocial
from perfilusuario import PerfilUsuario

usuario = UsuarioRedeSocial("Lucas", 18)
perfil_usuario = PerfilUsuario(usuario)

amigo1 = UsuarioRedeSocial("Talison", 19)
amigo2 = UsuarioRedeSocial("Jonathan", 16)
perfil_usuario.UsuarioRedeSocial.adicionar_amigo(amigo1)
perfil_usuario.UsuarioRedeSocial.adicionar_amigo(amigo2)
perfil_usuario.UsuarioRedeSocial.atualizar_nome("Evangelista")
perfil_usuario.UsuarioRedeSocial.atualizar_idade(19)

perfil_usuario.definir_descricao("Olá, eu sou Dev Front-end.")
perfil_usuario.adicionar_interesse("Programação")
perfil_usuario.adicionar_interesse("Web")
perfil_usuario.adicionar_interesse("Tecnologia")

print(f"Nome do usuário: {perfil_usuario.UsuarioRedeSocial.obter_nome()}")
print(f"Idade do usuário: {perfil_usuario.UsuarioRedeSocial.obter_idade()} anos")
print(f"Descrição do usuário: {perfil_usuario.obter_descricao()}")
print(f"Interesses do usuário: {perfil_usuario.listar_interesses()}")