from televisor import Televisor, ControleRemoto

televisor = Televisor(False, 1, 0)
controle_remoto = ControleRemoto()

controle_remoto.associar_televisor(televisor)

controle_remoto.ligar_televisor()
controle_remoto.exibir_status_televisor()

controle_remoto.mudar_canal(7)
controle_remoto.aumentar_volume()
controle_remoto.aumentar_volume()

controle_remoto.exibir_status_televisor()

controle_remoto.diminuir_volume()
controle_remoto.exibir_status_televisor()

controle_remoto.desligar_televisor()
controle_remoto.exibir_status_televisor()