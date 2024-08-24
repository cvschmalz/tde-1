# Aluna: Christine von Schmalz

##################
# ENUNCIADO
# Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
# linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
# operações que serão realizadas entre dois conjuntos de dados.
# O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
# em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
# operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
# seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
# operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
# terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
# das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
# 4
# U
# 3, 5, 67, 7
# 1, 2, 3, 4
# I
# 1, 2, 3, 4, 5
# 4, 5
# D
# 1, A, C, 34
# A, C, D, 23
# C
# 3, 4, 5, 5, A, B, R
# 1, B, C, D, 1
# Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
# produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
# {𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
# A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
# dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
# a informação e a formatação mostrada a seguir:
# União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
# Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
# um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
# de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
# minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
# No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
# pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
# implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
# Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
# contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
# diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no
# ambiente repl.it quanto no ambiente Github.
# Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,
# no mínimo um arquivo de testes criado pelo próprio professor.
#############


# Read file as a list and remove every \n
file = open("operacoes.txt")
content_raw = file.readlines()  # Turns each line of the file into a separate string and adds them to a list
content = []
for item in content_raw:
    content.append(item.replace("\n", ""))  # Removes every \n

opNo = int(content[0])  # Defines how many operations will be done
opType = 0  # Defines operation type
counter = 1


# Function for turning lists into properly formatted strings
def format_list(list0):
    string = str(list0)
    string = string.replace("[", "{")
    string = string.replace("]", "}")
    string = string.replace("'", "")
    return string


# Function for removing empty strings from lists
def remove_empty(list0):
    for i in list0:
        if i == "":
            list0.remove(i)
    return list0


# Loop that goes through every line of the content file
while counter < 3 * opNo + 1:

    result = []  # For storing the result of each operation
    pair = []  # For storing ordered pairs
    opType = content[counter]  # Catches operation type from the appropriate line
    list1 = content[counter + 1].rsplit(", ")  # Catches each set, turns them into lists divided by the commas
    list2 = content[counter + 2].rsplit(", ")
    list1 = remove_empty(list1)  # Remove any empty strings
    list2 = remove_empty(list2)

    if opType == "U":  # Union
        for i in list1:
            result.append(i)  # Adds all elements from the first set to the result
        for i in list2:
            if result.count(i) == 0:
                result.append(i)   # Adds elements from the second set if they're not repeated

        # Format all sets to nice strings
        list1 = format_list(list1)
        list2 = format_list(list2)
        result = format_list(result)

        print("União: conjunto 1 {0}, conjunto 2 {1}. Resultado: {2}".format(list1, list2, result))

    elif opType == "I":  # Intersection
        for i in list1:
            for j in list2:
                if i == j:
                    result.append(i)  # Only adds elements that are in both sets to the result

        # Format all sets to nice strings
        list1 = format_list(list1)
        list2 = format_list(list2)
        result = format_list(result)

        print("Interseção: conjunto 1 {0}, conjunto 2 {1}. Resultado: {2}".format(list1, list2, result))

    elif opType == "D":  # Difference
        for i in list1:
            result.append(i)  # Adds all elements from the first set to the result
        for i in list2:
            if result.count(i) > 0:
                result.remove(i)  # Removes all elements that appear in the second set

        # Format all sets to nice strings
        list1 = format_list(list1)
        list2 = format_list(list2)
        result = format_list(result)

        print("Diferença: conjunto 1 {0}, conjunto 2 {1}. Resultado: {2}".format(list1, list2, result))

    elif opType == "C":  # Cartesian product
        if len(list1) != 0 and len(list2) != 0:  # Only goes through if neither of the sets are empty
            for i in list1:
                for j in list2:
                    pair = [i, j]  # Creates a pair out of every possible combination
                    if result.count(pair) == 0:
                        result.append(pair)  # Only adds a pair to the result if it isn't already present
        else:
            result = []  # If either set is empty, the result is also empty

        # Format all sets to nice strings
        list1 = format_list(list1)
        list2 = format_list(list2)
        result = format_list(result)

        print("Produto Cartesiano: conjunto 1 {0}, conjunto 2 {1}. Resultado: {2}".format(list1, list2, result))

    # Increase loop counter by 3 to skip 3 lines ahead
    counter += 3
