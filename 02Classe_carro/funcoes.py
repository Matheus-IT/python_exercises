def resumo_carro(c):
    print('-'*30)
    print(f' - Modelo {c.modelo}')
    print(f' - Cor do carro {c.cor}')
    print(f' - Vidros eletricos {c.vidros_eletricos}')
    print(f' - Travas eletricas {c.travas_eletricas}')
    print(f' - Quantidade de lugares {c.qtd_lugares}')
    print(f' - Gps {c.gps}')
    try:
        print(f' - Camera de re {c.camera_de_re}')
    except:
        pass #Do nothing
    try:
        print(f' - Wi-fi {c.wifi}')
    except:
        pass
    print('-'*30)