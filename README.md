# 4sem-sprint3-dp
Sprint 3 Dynamic Programming

## estruturas utilizadas
    lista (pilha e fila)
    dicionarios

## funcoes utilizadas e complexidade
    queuea() O(1)
    consulta() O(n)
    searcha() case 1: O(n), case 2: O(log n)
    sorta() avg: O(n log n), worst: O(n**2)

## codigo explicado
files:
- main.py
- funcs.py
- utils.py

### main
funciona como menu para o user selecionar a opcao desejada

### utils
onde foram definidas funcoes helper, nao sao as principais porem ajudam

### funcs
onde a maior parte do codigo fica. as 4 funcoes principais sao as demonstradas na section de complexidade.

###### queuea (fila)
funcao para adicionar items, o user digita nome, quantidade e validade do item, se tudo estiver de acordo, o item entra no estoque

###### consulta (pilha)
funcao para checar quais os items no estoque, funciona como pilha porque mostra os ultimos items da fila primeiro

###### searcha (sequencial e binaria)
funcao para procurar por items, sequencial caso o user queira procurar por nome, binaria caso seja por quantidade

###### sorta
funcao de sort, o algoritimo utilizado foi o quicksort

## integrantes
Joao Victor Oliveira dos Santos rm557948
Matheus Alcantara Estevao rm558193
Pedro Pereira dos Santos rm552047
Nicolle Pellegrino Jelinski
Eric Segawa Montagner rm558224
