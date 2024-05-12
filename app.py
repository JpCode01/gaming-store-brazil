import json
import os

# Carregar os dados
with open("dados.json") as dados_pc:
    dados_json = json.load(dados_pc)

# Guardar os dados
dados_do_pc = {}
for item in dados_json: 
    modelo_do_pc = item['modelName']
    if modelo_do_pc not in dados_do_pc:
        dados_do_pc[modelo_do_pc] = []
    
    dados_do_pc[modelo_do_pc].append({
        "model": item['modelName'],
        "configurations": item['configurations']
    })

def titulo_do_programa():
    """
    Exibe o título do programa.
    
    Input: Título
    """
    print("""

▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ ▀█▀ ▒█▄░▒█ ▒█▀▀█ 　 ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀ 　 ▒█▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▀▀█ ▀█▀ ▒█░░░ 
▒█░▄▄ ▒█▄▄█ ▒█▒█▒█ ▒█░ ▒█▒█▒█ ▒█░▄▄ 　 ░▀▀▀▄▄ ░▒█░░ ▒█░░▒█ ▒█▄▄▀ ▒█▀▀▀ 　 ▒█▀▀▄ ▒█▄▄▀ ▒█▄▄█ ░▄▄▄▀▀ ▒█░ ▒█░░░ 
▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▄█▄ ▒█░░▀█ ▒█▄▄█ 　 ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▄ 　 ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█▄▄▄█ ▄█▄ ▒█▄▄█
""")
    
    print('━' * 108)

def exibir_opcoes_do_app():
    """
    Exibe as opções disponíveis.

    Input: Opção 1 e 2
    """
    print('1 - Modelos de computadores')
    print('2 - Configurações desse modelo')

def exibir_modelos():
    """
    Exibe os modelos disponíveis no estoque.
    
    """
    configuracoes = []
    modelos = []
    # Percorre os dados para recuperar o nome e as configurações.
    for item in dados_json:
        configuracoes.append(item['configurations'])
        modelos.append(item['modelName'])

    # Exibição dos dados.
    for i in range(0, len(modelos), 1):
        print(f'{modelos[i].ljust(5)} | {configuracoes[i]}')
    
    print('')
    print('━' * 108)
    
def exibir_configuracoes():
    # Varável para entrar na repetição
    verificacao = True
    while verificacao:
        # Input para escolha do modelo.
        escolher_modelo = input('Qual será o modelo? (a/b/c/d) ')
        print('')
        print('━' * 108)
    
        # Cascata condicional para converter a opção para o nome do modelo.
        if escolher_modelo == 'a':
            opcao_convertida = 'Model A'
            break
        elif escolher_modelo == 'b':
            opcao_convertida = 'Model B'
            break
        elif escolher_modelo == 'c':
            opcao_convertida = 'Model C'
            break
        elif escolher_modelo == 'd':
            opcao_convertida = 'Model D'
            break
        else:
            print('\nModelo inválido! Digite novamente.')
            continue
    
    # Cria um dicionário para guardar as informações e percorrer o arquivo JSON.
    modelos_info = {modelo['modelName']: modelo['configurations'] for modelo in dados_json}
    # Condicional para exibição.
    if opcao_convertida in modelos_info:
        configuracoes = modelos_info[opcao_convertida]
        print(f"\nProcessador: | {configuracoes['cpu']}")
        print(f"Placa de vídeo: | {configuracoes['gpu']}")
        print(f"Memória RAM: | {configuracoes['memory']}")
        print(f"Armazenamento: | {configuracoes['storage']}\n")

    print('━' * 108)

def sair_do_programa():
    """
    Limpa o console e exibe a mensagem final.
    """
    os.system('cls')
    mensagem_final()

def mensagem_final():
    """
    Exibe mensgem final.
    """
    print('Para mais informações acesse: \n \n 💬 gamingbrazil@gmail.com')

def escolher_opcao():
    """
    Escolher a opção do programa.

    Input: opcao_escolhida
    """
    opcao_escolhida = int(input('\nEscolha uma opção pelo número: '))
    print('')
    print('━' * 108)
    print('')

    # Verifica a opção
    if opcao_escolhida == 1:
       exibir_modelos() 
    elif opcao_escolhida == 2:
        exibir_configuracoes()
    else:
        print('Opção inválida. Digite novamente')
        escolher_opcao()


# Cria os arquivos JSON
for modelo_do_pc, dados in dados_do_pc.items():
     nome_do_arquivo = f'{modelo_do_pc}.json'
     with open(nome_do_arquivo, 'w') as arquivo_pc:
        json.dump(dados, arquivo_pc,indent=4)

# Programa principal
def main():
    executar = True
    while executar:
        titulo_do_programa()
        exibir_opcoes_do_app()
        escolher_opcao()
        seguir_execucao = input('\nDeseja continuar no programa?(s/n) ')
        seguir_execucao.lower()
        if seguir_execucao == 'n':
            sair_do_programa()
            break
        else:
            os.system('cls')
            continue

if __name__ == '__main__':
    main()