# Sprint 4 Dynamic Programming

## codigo explicado
files:
- main.py
- utils.py
- funcs/
  + check.py
  + dp.py
  + edit.py
  + register.py
  + search.py

### main.py
    funciona como menu para o user selecionar a opcao desejada

### utils.py
    onde foram definidas funcoes helper para observar e 
    comparar o tempo de execucao + 
    memoria utilizadas pelos algoritimos top down e bottom up

### funcs/

#### check.py
    funcao para listar items iterativamente
- display de todos os items presentes no estoque
#### dp.py
    funcoes top down e bottom up para comparar o valor total dos items em estoque
- funcao para calcular o valor total do inventario
- funcao para calcular o item de maior valor dentro do inventario
#### edit.py
    funcao que permite o user editar items existentes no estoque
- o user escolhe qual o item **existente** ele deseja editar
- caso encontrado, recebe um menu para selecionar qual informacao gostaria de editar
#### register.py
    funcao para o user registrar items novos
- uso de dicionarios para armazenamento dos items e organizacao
- os dicionarios sao armazenados dentro de uma lista
#### search.py
    funcao para localizar um item especifico em estoque
## integrantes
- Joao Victor Oliveira dos Santos rm557948
- Matheus Alcantara Estevao rm558193
- Pedro Pereira dos Santos rm552047
- Nicolle Pellegrino Jelinski rm558610
- Eric Segawa Montagner rm558224
