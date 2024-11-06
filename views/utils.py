import os

def limpa_tela():
    return os.system('clear') or None

def colorir(texto, cor=37, bold=0, end='\n'):
    print(f"\033[{bold};{cor}m{texto}\033[0m", end=end)

def menu(cor):
    limpa_tela()
    t = 24
    colorir('=' * t, cor)
    colorir('MENU'.center(t), cor)
    colorir('=' * t, cor)
    colorir('  1 - Criar senha', cor)
    colorir('  2 - Visualizar senha', cor)
    colorir('  3 - Sair', cor)
    colorir('=' * t, cor)
    print()
    