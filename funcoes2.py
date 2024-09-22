def loginUsuario(perfil):
    print(str.lower(perfil))
    if str.lower(perfil) == 'admin':
        print("Bem-vindo, Administrador")
    else:
        print('Bem-vindo, Usuário')
perfil=input('Entre com seu usuário: ')

loginUsuario(perfil)
