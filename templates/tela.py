import __init__
from models.password import Password
from views.utils import menu, colorir
from views.password_views import FernetHasher


if __name__ == '__main__':

    menu(32)
    action = input('Informe a opção: ')
    match action:
        case '1':
            if len(Password.get()) == 0:
                key, path = FernetHasher.create_key(archive=True)
                colorir('\nSua chave foi criada, salve-a com cuidado caso a perca nao poderá recuperar suas senhas.')
                colorir('Chave:', 33, end=' ')
                colorir(f'{key.decode('utf-8')}', 36)
                if path:
                    colorir('\nChave salva no arquivo, lembre-se de remover o arquivo após o transferir de local', 33)
                    colorir('Caminho:', 33, end=' ')
                    colorir(f'{path}', 36)
            else: 
                key = input('\nDigite sua chave usada para criptografia, use sempre a mesma chave: ')

            domain = input('Domínio: ')
            #TODO: verificar se o domínio existe, em caso positivo alterar ao invés de adicionar
            password = input('Digite a senha: ')

            try:
                fernet = FernetHasher(key)
            except ValueError as e:
                print('\nToken inválido !\n')
                exit()

            p1 = Password(domain=domain, password=fernet.encrypt(password).decode('utf-8'))
            p1.save()

        case '2':
            domain = input('\nDomínio: ')
            key = input('Chave: ')

            try:
                fernet = FernetHasher(key)
            except ValueError as e:
                colorir('\nToken inválido !\n', 33)
                exit()

            data = Password.get()
            password = ''
            for i in data:
                if domain in i['domain']:
                    password = fernet.decrypt(i['password'])
                    break
                    
            if password:
                colorir('\nSua senha:', 33, end=' ')
                colorir(f'{password}\n', 36)
            else:
                colorir('\nNenhuma senha encontrada para esse domínio.\n', 33)

        case '3':
            colorir('\nSistema Finalizado!\n', 36)
            exit()                    
        case _:
            colorir('\nOpção inválida!\n', 33)
