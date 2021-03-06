# AULA 01: VARIÁVEIS, PRINT() E INPUT()

Os três aspectos mais comuns de um programa de computador, seja qual for a linguagem em que ele foi escrito, são:

1- **variáveis**

2- **saída de dados**

3- **entrada de dados**

## Variáveis

Variável é um espaço da memória do computador que armazena um dado. Em Python, uma variável é definida a partir de um *nome* e um *valor*. Usa-se o símbolo = para atribuir/armazenar/definir o valor de uma variável. Por exemplo:

```python
a = 4
b = 3
c = 5
```

No exemplo acima, definimos três variáveis: ```a```, ```b```, ```c```. Cada uma foi criada/inicializada com os valores 4, 3, 5, respectivamente. Aquilo do lado esquerdo do símbolo = é o nome da variável; aquilo do lado direito, o valor.

Existem algumas regras para definir nomes de variáveis. Eles podem ser curtos (como ```x```, ```y```, ```a``` ou ```b```) ou um nome mais descritivo (idade, nome, volume_total). As regras de nomeação de uma variável no Python são:

- Uma variável DEVE começar com uma letra or com o caractére sublinhado (_)
- Uma variável NÃO PODE começar com um número
- Uma variável pode conter APENAS caractéres alfanuméricos e sublinhados (A-Z, a-z, 0-9, _)
- Variáveis são sensíveis à capitalização (```idade```, ```Idade``` e ```IDADE``` são tratadas como três variáveis diferentes)

## A função de saída mais comum: print()

Função é um comando especial. Uma função é definida por um nome seguido por um abre e fecha parênteses. Dentro dos parênteses colocamos dados que serão usados pela função (chamamos esses dados de **parâmetros** ou **argumentos da função**). Uma função pode ou não retornar valores (também chamados de resultados). Python possui várias funções já inclusas, além de permitir que o programador crie as suas próprias funções. Veremos como construir uma função em tempo oportuno, além de uma lista de funções super legais disponíveis. Por enquanto, apresentaremos duas funções importantes e super úteis em diversos programas escritos em Python. A primeira delas é a print().

A função print() exibe uma mensagem na tela. Seu uso é bem simples: basta chamá-la em seu programa com algum texto, variável ou valor dentro dos parênteses. Ao ser executada, print() vai exibir o dado na saída padrão (chamada de console ou terminal).

```python
print("Olá, Mundo!")
#>>Olá, Mundo!
```

Note que no exemplo acima, as aspas do texto "Olá, Mundo!" não aparecem no resultado. Elas servem como delimitadores de textos. Mais detalhes sobre textos quando falarmos de tipos de dados.

Também é possível mostrar o conteúdo de variáveis:

```python
num1 = 5
num2 = 10
print(num1)
#>>5
print(num2)
#>>10
```

## A função de entrada mais comum: input()

Enquanto a função print() exibe dados, ou seja, é um função de saída, a função input() é usada para capturar dados, ou seja, é uma função de entrada. Assim como a print(), você também pode passar uma mensagem como argumento (dentro dos parênteses) para facilitar a iteração entre o programa e o usuário. Agora, diferente da print(), a input() é uma função que retorna um resultado. Isso quer dizer que você pode armazenar esse resultado em uma variável, através do operador =.

```python
idade = input("Quantos anos você tem? ")
#>>Quantos anos você tem? 28
print(idade)
#>>28
```
## EXERCÍCIOS 01: Variáveis, entrada e saída

Na primeira aula, vimos o conceito de variável, como mostrar dados na tela usando a função print() e como ler dados do teclado usando a função input(). Consolidar esses três conceitos são essenciais para os próximos passos e para construir programas mais sofisticados!

**1.1:** O seu primeiro programa deve conter os seguintes passos:

> - Crie uma variável chamada x e atribua o valor 100 a ela
>
> - Crie uma variável chamada y e atribua o valor 200 a ela
>
> - Mostre os conteúdos de x e depois y usando a função print()
>
> - Crie uma variável chamada z e atribua a ela um valor entrada via input()
>
> - Mostre o conteúdo de z usando print()

**1.2:** Escreva um programa que guarda uma lista de compras. Você deve registrar pelo menos 3 alimentos, 2 produtos de limpeza e 4 avulsos. Use uma variável para cada item da lista. Perguntas: qual critério você usou para nomear as variáveis? O MU reclamou de algum nome que você escolheu? Se sim, como você corrigiu?

**1.3:** Você foi contratado como programador em grande conglomerado capitalista (banco). Sua primeira função é criar um programa que lê três informações dos clientes (nome, idade, senha de cartão de crédito) e depois mostra esses valores de volta. É um programa muito útil e seguro. Escreva esse programa e compartilhe com seus amigos (menos a senha, claro, use uma senha falsa como teste).
