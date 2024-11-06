# Gerenciador de Senhas

> Projeto desenvolvido na [4days-4projects](https://pythonando.com.br "Pythonando").

## Objetivo

    Gerenciar senhas, criptografando as mesmas, de diversos serviços em apenas um lugar.

## Sumário

- <a href='#pré-requesitos'>Pré-requisitos</a>
- <a href='#funcionalidades'>Funcionalidades</a>
- <a href='#como-executar-o-projeto'>Como executar o projeto</a>

### Pré-requisitos

    Python.

### Funcionalidades

- Gerar chave mestra
- Gerar e salvar senha criptografada

### Como executar o projeto

```bash
# Clone o projeto
git clone https://github.com/gm-costa/gerenciador_senha.git

# A partir daqui vou usar o comando 'python3', pois uso linux, quem for 
# usar no windows, pode substituir por 'python' ou somente 'py'

# Crie o ambiente virtual
python3 -m venv venv

# Ative o ambiente
    # No Linux
        source venv/bin/activate
    # No Windows
        venv\Scripts\Activate

# Instale as bibliotecas
pip install -r requirements.txt

# Execute o projeto
python3 templates/tela.py
```

---
