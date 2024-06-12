nome = input('Digite o nome da Aluna: ')
idade = int(input('Digite a idade da aluna: '))
altura = float(input('Digite a altura da aluna: '))
hobbies = input('Digite os hobbies da aluna separados por virgula: ')
hobbies1 = hobbies.split(',') #transforma hobbies em uma lista
endereco_rua = input('Digite o nome da rua da aluna: ')
endereco_numero = int(input('Digite o numero da casa da aluna: '))
endereco_cidade = input('Digite a cidade da aluna: ')
endereco = (endereco_rua, endereco_numero, endereco_cidade) #cria uma tupla
email = input('Digite o email da aluna: ')
telefone = input('Digite o telefone da aluna: ')
contato = {'email': email, 'telefone': telefone} # quando usa colchetes ria um dicionario

print('\nOlá, segue informações sobre a aluna:')
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Hobbies:', hobbies1)
print('Endereço:', endereco)
print('Contato', contato)
