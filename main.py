"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    num_1 = float(input('Digite um número: '))
    num_2 = float(input('Digite outro número: '))
    if (num_1 >= num_2):
      maior = num_1
    else:
      maior = num_2
    print(f'{maior}')

if __name__ == '__main__':
    main()
