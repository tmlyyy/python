# Python Module 03 — guia de estudos e revisão final

Este é o repositório de estudos. Este guia permanece aqui; apenas `ex0` a `ex6` serão copiadas posteriormente para o repositório oficial. A referência é o subject **Data Quest: Mastering Python Collections**, versão 3.0, e a régua de avaliação fornecida. Todos os exemplos abaixo são executados a partir da pasta `python03`.

As regras comuns pedem Python 3.10+, `flake8`, type hints em todas as funções e métodos, verificação com `mypy`, tratamento cuidadoso de exceções e nenhuma operação de arquivo. Cada exercício tem sua própria lista de funções autorizadas. O subject também permite `str`, `int` e `float`, incluindo construtores e métodos. A estrutura de coleção apresentada em cada exercício pode usar seus métodos associados.

# Ex0 — Command Quest

## O que o subject quer

Ler a linha de comando, mostrar o nome do programa, contar os argumentos do usuário, mostrar cada um e mostrar o total de elementos de `sys.argv`.

## Conceitos que preciso saber

`sys.argv` é uma lista de strings. `sys.argv[0]` contém o caminho usado para chamar o programa; `sys.argv[1:]` é um *slice* com os argumentos do usuário. Índices começam em zero. O shell passa `"Data Quest"` como um único argumento porque as aspas agrupam as duas palavras antes de iniciar o Python. Se o usuário passa três argumentos, `len(sys.argv)` vale quatro, pois inclui o nome do programa.

## Como meu código funciona

Importa `sys`, extrai a parte final de `sys.argv[0]` com `split("/")[-1]` e calcula `len(args) - 1`. Se não houver argumentos, mostra um aviso. Caso contrário, percorre `args[1:]`, imprime cada argumento e incrementa um contador iniciado em 1. Por fim, mostra `len(args)`. Não usa `range()`.

## Trechos importantes do código

```python
for arg in args[1:]:
    print(f"Argument {i}: {arg}")
    i += 1
```

O slice evita imprimir o nome do programa junto dos argumentos. O contador numera apenas os argumentos do usuário.

## O que pode ser perguntado na avaliação

- O que há em `sys.argv[0]`?
- Qual a diferença entre `sys.argv[1:]` e `sys.argv`?
- Como você poderia evitar imprimir o nome do programa de outra maneira?

## Respostas que eu preciso saber dar

`argv[0]` é o caminho/nome usado para chamar o script. O slice começa no primeiro argumento do usuário e cria uma nova lista. Outra solução seria percorrer a lista inteira e ignorar o índice zero; a solução atual usa slicing e contador.

## Testes da régua

```bash
python3 ex0/ft_command_quest.py
python3 ex0/ft_command_quest.py hello world 42
python3 ex0/ft_command_quest.py "Data Quest"
```

Resultados: aviso e total 1; três argumentos e total 4; um argumento `Data Quest` e total 2, respectivamente.

## Edge cases

String vazia, acentos e espaços dentro de aspas são preservados como argumentos; não há conversão numérica.

## Status

**OK.** Usa `import sys`, `sys.argv`, `len()`, `print()` e métodos permitidos de `str`.

# Ex1 — Score Cruncher

## O que o subject quer

Ler pontuações inteiras da linha de comando, guardar as válidas em uma lista, descartar entradas inválidas e calcular quantidade, soma, média, maior, menor e amplitude (*score range*).

## Conceitos que preciso saber

Uma `list` preserva a ordem e aceita novos elementos por `append()`. `int(texto)` converte uma string para inteiro; texto inválido provoca `ValueError`. `try/except` permite informar o erro e continuar com os demais argumentos. `sum()` soma, `min()` acha o menor e `max()` acha o maior. A média é soma dividida pela quantidade; a amplitude é `max - min`.

## Como meu código funciona

Percorre `sys.argv[1:]`, tenta converter cada argumento e acrescenta os válidos à lista. Se a lista ficar vazia, imprime uso e termina. Caso contrário, calcula as estatísticas. A média normal é apresentada como `float`. Se a conversão de uma soma inteira muito grande causar `OverflowError`, o programa apresenta a média exata como parte inteira mais fração, sem estabelecer limite arbitrário para pontuações válidas.

## Trechos importantes do código

```python
try:
    val = int(arg)
    valid_scores.append(val)
except ValueError:
    print(f"Invalid parameter: '{arg}'")
```

```python
whole = total_score // total_players
remainder = total_score % total_players
```

A primeira parte isola entradas inválidas. A segunda permite representar a média de inteiros que não cabem em `float`; por exemplo, `10 + 1/2` significa 10,5.

## O que pode ser perguntado na avaliação

- Por que guardar os scores em uma lista?
- Por que tratar `ValueError` dentro do laço?
- Como são calculadas a média e a amplitude?

## Respostas que eu preciso saber dar

A lista conserva todas as pontuações válidas para estatísticas. O tratamento dentro do laço descarta só a entrada ruim. Média é `sum(scores) / len(scores)`; amplitude é `max(scores) - min(scores)`.

## Testes da régua

```bash
python3 ex1/ft_score_analytics.py 1500 2300 1800 2100 1950
python3 ex1/ft_score_analytics.py 100 250 180 90 300
python3 ex1/ft_score_analytics.py 100 abc 200
python3 ex1/ft_score_analytics.py
python3 ex1/ft_score_analytics.py ab ac
```

Resultados: primeiro caso soma 9650 e média 1930.0; caso da régua soma 920 e média 184.0; `abc` é descartado; entradas sem score válido mostram uso.

## Edge cases

`-10 0 10` produz soma 0 e amplitude 20. Uma pontuação de 400 dígitos já causou `OverflowError`; agora termina sem traceback. Scores inteiros negativos são aceitos, pois o subject não fixa limite inferior.

Em versões de Python que limitam a conversão de inteiros gigantes para texto, um resultado derivado acima desse limite recebe a mensagem `Numeric result exceeds Python's display limit` em vez de traceback. Nesse caso extremo, a impressão das estatísticas pode terminar antes do fim; o limite pertence ao interpretador, não à validação dos scores.

## Status

**OK.** Usa `import sys`, `sys.argv`, `len()`, `sum()`, `max()`, `min()`, `print()`, `list.append()` e construtores permitidos `int()`/`float()`.

# Ex2 — Position Tracker

## O que o subject quer

Pedir duas posições 3D, cada uma como `x,y,z`; repetir a pergunta em caso de entrada inválida; mostrar a primeira tupla e cada coordenada; calcular a distância à origem e entre os dois pontos.

## Conceitos que preciso saber

Uma `tuple` guarda uma sequência de valores e é imutável: seus elementos não são trocados depois da criação. Uma `list` seria mutável. Podemos acessar uma tupla por índice (`pos[0]`) ou desempacotá-la (`x, y, z = pos`). O código desempacota as três strings lidas e acessa as coordenadas da tupla por índice. `float()` converte números decimais. `input()` lê uma linha. `math.sqrt()` calcula raiz quadrada. A distância Euclidiana é `sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)`.

## Como meu código funciona

`get_player_pos()` divide a linha nas vírgulas e tenta desempacotar exatamente três partes; `ValueError` indica sintaxe errada. Cada parte é convertida com `float()` e produz mensagem específica se for inválida. `nan` e infinitos são rejeitados; uma posição válida retorna `tuple[float, float, float]`. `main()` chama a função duas vezes, imprime a primeira posição e calcula as distâncias com `math.sqrt()`. Se stdin terminar, imprime aviso e encerra sem traceback. Se a distância exceder a faixa representável, imprime aviso e encerra.

## Trechos importantes do código

```python
try:
    x_str, y_str, z_str = line.split(",")
except ValueError:
    print("Invalid syntax")
    continue
```

O desempacotamento exige exatamente três campos sem usar `len()`, que não é autorizado neste exercício.

## O que pode ser perguntado na avaliação

- Por que usar tupla para posição?
- O que acontece quando há duas ou quatro coordenadas?
- Qual a diferença entre um erro de conversão e EOF?

## Respostas que eu preciso saber dar

Uma posição tem três componentes fixos; a tupla expressa isso. Quantidade errada de campos falha no desempacotamento e pede nova entrada. `ValueError` indica texto ou formato inválido; `EOFError` indica que não há mais entrada disponível.

## Testes da régua

```bash
python3 ex2/ft_coordinate_system.py
```

Na primeira execução, digite `hello world`, `1.0 , 2.5, 3.0`, `4,abc,5`, `4,5,6`: os erros são informados e as distâncias finais são 4.0311 e 4.9244. Em outra execução, digite `0,0,0` e `3,4,0`: distâncias 0.0000 e 5.0000.

## Edge cases

EOF na primeira ou segunda leitura encerra com aviso. `nan` e `inf` são rejeitados. `1e308,0,0` ou distância que resulta em infinito numérico recebe aviso de distância grande, sem traceback. Uma coordenada finita pode ser grande demais para a fórmula com `float`; o programa encerra de forma controlada em vez de apresentar um resultado incorreto.

## Status

**OK.** Usa `import math`, `math.sqrt()`, `input()`, `print()` e métodos/construtores permitidos de `str` e `float`. Não usa `len()`.

# Ex3 — Achievement Hunter

## O que o subject quer

Sortear conquistas de um catálogo fixo para pelo menos quatro jogadores. Mostrar o conjunto de todas as conquistas sorteadas, as comuns a todos, as exclusivas de cada jogador e as que faltam para completar o catálogo.

## Conceitos que preciso saber

`set` guarda valores únicos: não há duplicatas nem ordem garantida. `union()` reúne elementos de qualquer conjunto. `intersection()` retém os elementos de todos. `difference()` mostra os elementos do primeiro conjunto ausentes do segundo. `set()` cria conjunto vazio; `{}` cria dicionário vazio porque essa sintaxe foi reservada para dicionários.

## Como meu código funciona

`gen_player_achievements()` sorteia uma quantidade entre 5 e 10, amostra o catálogo e devolve um `set`. `main()` gera quatro jogadores. Calcula união, interseção e exclusivos com operações de conjuntos. Para faltantes, cria `all_possible = set(ACHIEVEMENTS)` e subtrai o conjunto de cada jogador. Assim, uma conquista que ninguém recebeu ainda aparece entre as faltantes.

## Trechos importantes do código

```python
all_distinct = set.union(alice, bob, charlie, dylan)
all_possible = set(ACHIEVEMENTS)
print(f"Alice is missing: {set.difference(all_possible, alice)}")
```

A união descreve o que surgiu entre os jogadores. O catálogo descreve tudo o que pode ser conquistado; só ele serve de base para calcular o que falta.

## O que pode ser perguntado na avaliação

- Qual a diferença entre união e interseção?
- Como encontrar conquistas exclusivas?
- Por que faltantes usam o catálogo inteiro?

## Respostas que eu preciso saber dar

União é “ao menos um jogador”; interseção é “todos”. Exclusivas de Alice são `alice - (bob ∪ charlie ∪ dylan)`. Para completar todas, Alice precisa de `catálogo - alice`, inclusive itens ainda não sorteados para ninguém.

## Testes da régua

```bash
python3 ex3/ft_achievement_tracker.py
python3 ex3/ft_achievement_tracker.py
python3 ex3/ft_achievement_tracker.py
```

As três execuções produzem conjuntos aleatórios. Um teste controlado em memória, com os quatro jogadores recebendo as mesmas cinco conquistas, confirmou as nove restantes como faltantes para cada um.

## Edge cases

Interseção ou exclusivos podem ser `set()`: a aleatoriedade não garante conjuntos não vazios. A ordem textual de um set pode variar; compare seus elementos, não sua apresentação.

## Status

**OK.** Usa `import random`, `random.randint()`, `random.sample()`, `set()`, `set.union()`, `set.intersection()`, `set.difference()` e `print()`.

# Ex4 — Inventory Master

## O que o subject quer

Ler parâmetros `item:quantity`, descartar inválidos e repetidos, armazenar quantidades inteiras em um dicionário, mostrar inventário, nomes, total, porcentagens, maior e menor quantidade e adicionar um item realmente novo.

## Conceitos que preciso saber

`dict` associa uma chave a um valor: aqui, `nome -> quantidade`. `inventory[item]` lê pela chave; `item in inventory` testa se já existe. `keys()` fornece os nomes, `values()` fornece as quantidades e `update()` adiciona ou atualiza entradas. A ordem de inserção é preservada: se a busca por maior/menor só troca o candidato com desigualdade estrita, o primeiro item vence empates. Porcentagem é `quantidade / total * 100`.

## Como meu código funciona

Se não há argumentos, mostra uso. O laço separa cada parâmetro em dois campos, rejeita formato ruim, nome vazio e chave repetida, converte a quantidade com `int()` e guarda o item. Mostra o dicionário e `list(inventory.keys())`; soma `inventory.values()`. Evita divisão por zero. Para números comuns, mostra porcentagem com uma casa decimal. Se o resultado ultrapassar a faixa de `float`, mostra a porcentagem exata como fração. Depois percorre os itens para encontrar maior e menor, e escolhe um nome novo (`magic_item`, acrescentando `_new` se necessário) antes de chamar `update()`.

## Trechos importantes do código

```python
if item_name in inventory:
    print(f"Redundant item '{item_name}' - discarding")
    continue
```

```python
new_item = "magic_item"
while new_item in inventory:
    new_item += "_new"
inventory.update({new_item: 1})
```

O teste de pertencimento evita duplicatas da entrada. O segundo trecho preserva um `magic_item` recebido do usuário e garante uma chave nova na atualização final.

## O que pode ser perguntado na avaliação

- Por que usar um dicionário?
- Como `keys()`, `values()` e `update()` entram no código?
- Por que o primeiro item vence um empate?

## Respostas que eu preciso saber dar

O nome identifica a quantidade correspondente; acesso por chave é direto. `keys()` gera a lista de nomes, `values()` fornece números para `sum()`, e `update()` adiciona o item final. A ordem de inserção é preservada e a comparação usa apenas `>` ou `<`, nunca `>=` ou `<=`.

## Testes da régua

```bash
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2 armor:3
python3 ex4/ft_inventory_system.py
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
```

Resultados: primeiro total 11 e `potion` como mais abundante; sem argumentos, mensagem de uso; no terceiro, duplicata e formatos ruins são descartados, com total 12.

## Edge cases

`magic_item:7` é preservado e `magic_item_new:1` é adicionado. `a:2 b:2` escolhe `a` nos dois extremos. `a:0 b:0` mostra 0.0% sem divisão por zero. Uma soma pequena de inteiros enormes de sinais opostos usa uma fração exata para porcentagem, evitando overflow de `float`. Quantidades negativas são aceitas porque o subject pede conversão para `int` e não define mínimo; isso pode produzir percentuais negativos. Se o total for zero, o código exibe 0.0% por convenção, pois a porcentagem matemática é indefinida.

Se um cálculo produzir um inteiro maior que o limite de conversão para texto do interpretador, o programa informa `Numeric result exceeds Python's display limit` sem traceback; a saída do inventário pode ficar parcial nesse extremo.

## Status

**OK.** Usa `import sys`, `sys.argv`, `len()`, `print()`, `sum()`, `list()`, `dict.keys()`, `dict.values()`, `dict.update()` e construtores/métodos permitidos de `str`, `int` e `float`.

# Ex5 — Stream Wizard

## O que o subject quer

Gerar e imprimir mil eventos sob demanda, criar uma lista separada com dez eventos e consumi-la aleatoriamente até ficar vazia usando outro gerador.

## Conceitos que preciso saber

Um *generator* calcula o próximo valor quando pedido: isso é *lazy evaluation* ou geração sob demanda. `yield` entrega um valor e pausa a função; `return` encerra a função e devolve um resultado. `next(generator)` retoma até o próximo `yield`. Um gerador infinito pode produzir eventos sem guardar uma lista infinita. Uma lista mantém todos os elementos em memória, o que custa espaço proporcional à quantidade de eventos. `typing.Generator[tuple[str, str], None, None]` diz: produz tuplas de duas strings; não recebe valores pelo método `send`; não retorna valor especial ao terminar.

## Como meu código funciona

`gen_event()` fica em `while True`, escolhe jogador e ação com `random.choice()` e produz a tupla com `yield`. `main()` chama `next()` mil vezes e imprime cada evento imediatamente, sem lista de mil elementos. Depois constrói uma lista com dez eventos. `consume_event()` escolhe um item dessa lista, remove-o e o produz; o `for` o consome diretamente até a lista esvaziar.

## Trechos importantes do código

```python
while True:
    player = random.choice(PLAYERS)
    action = random.choice(ACTIONS)
    yield (player, action)
```

```python
for event in consume_event(ten_events):
    print(f"Got event from list: {event}")
```

O primeiro gerador só produz quando `next()` é chamado. O segundo `for` pede valores até `consume_event()` terminar.

## O que pode ser perguntado na avaliação

- Por que um gerador economiza memória?
- O que muda entre `yield` e `return`?
- O que acontece quando a lista de `consume_event()` fica vazia?

## Respostas que eu preciso saber dar

O evento é criado e usado um de cada vez; não há lista de mil eventos. `yield` pausa e permite retomar, enquanto `return` termina. Quando a lista fica vazia, o gerador termina e o `for` para naturalmente.

## Testes da régua

```bash
python3 ex5/ft_data_stream.py
```

Foram confirmadas exatamente mil linhas `Event`, dez linhas `Got event from list` e lista final `[]`. Duas execuções produziram eventos diferentes.

## Edge cases

Um teste em memória confirmou que `consume_event([])` termina imediatamente, uma lista unitária é esvaziada e eventos duplicados são todos consumidos. O gerador de eventos é infinito; não execute um `for` sem limite sobre ele.

## Status

**OK.** Usa `import typing`, `typing.Generator`, `import random`, `random.choice()`, `next()`, `range()` e `print()`. A lógica deste exercício não precisou de alteração.

# Ex6 — Data Alchemist

## O que o subject quer

Usar duas *list comprehensions* para transformar e filtrar nomes, uma *dict comprehension* para criar pontuações aleatórias e outra para manter pontuações acima da média.

## Conceitos que preciso saber

Uma comprehension combina expressão e laço em uma linha lógica. `[p.capitalize() for p in players]` transforma cada nome. `[p for p in players if condição]` filtra. `{nome: valor for nome in nomes}` constrói um dicionário; um `if` final filtra chaves/valores. Um laço tradicional pode fazer a mesma coisa em várias linhas com `append()` ou atribuição, mas a comprehension deixa a transformação simples próxima do resultado.

## Como meu código funciona

Cria a lista mista de nomes. A primeira comprehension capitaliza todos; a segunda mantém os que já correspondiam a `capitalize()` no início. A terceira associa cada nome capitalizado a um número aleatório entre 1 e 1000. Soma os scores, divide pela quantidade de chaves e mostra a média com duas casas. A quarta comprehension seleciona apenas `score > média`.

## Trechos importantes do código

```python
capitalized_players = [p.capitalize() for p in players]
```

```python
high_scores: dict[str, int] = {
    name: score_dict[name]
    for name in score_dict
    if score_dict[name] > avg_score
}
```

A primeira expressão transforma; o `if` da segunda construção filtra. A segunda aparece em várias linhas porque uma linha única ultrapassaria o limite de estilo.

## O que pode ser perguntado na avaliação

- Qual a diferença entre transformação e filtro?
- Por que o filtro usa `>` em vez de `>=`?
- O que acontece com dois nomes que ficam iguais após `capitalize()`?

## Respostas que eu preciso saber dar

Transformação muda cada valor; filtro escolhe quais entram. O subject pede scores *acima* da média, então igualdade fica fora. Chaves iguais num dicionário representam uma única entrada; na lista atual, os nomes resultantes são distintos.

## Testes da régua

```bash
python3 ex6/ft_data_alchemist.py
python3 ex6/ft_data_alchemist.py
```

As pontuações variaram. Em 100 execuções, a média e o filtro estritamente acima dela foram conferidos. Listas alternativas foram testadas em memória, sem alterar o arquivo.

## Edge cases

Uma lista vazia produz média 0.00 sem divisão por zero. Uma lista com um nome produz filtro vazio. Nomes que colidem após `capitalize()` compartilham uma chave no dicionário. O código atual trabalha com a lista fixa do subject.

## Status

**OK.** Usa `import random`, `random.randint()`, `print()`, `len()`, `sum()` e os construtores/métodos gerais `float()` e `str.capitalize()`. A lógica deste exercício não precisou de alteração.

# Diferença entre as principais estruturas

| Estrutura | Sintaxe | Ordenação | Mutabilidade | Duplicatas | Acesso | Uso típico |
|---|---|---|---|---|---|---|
| `list` | `[1, 2]` | Ordem de inserção | Mutável | Permite | Índice, slice | Sequência de scores ou eventos |
| `tuple` | `(1, 2)` | Ordem de posição | Imutável | Permite | Índice, unpacking | Coordenadas fixas |
| `set` | `{1, 2}` ou `set()` vazio | Sem ordem garantida | Mutável | Elimina | Pertencimento e operações de conjunto; sem índice | Conquistas únicas |
| `dict` | `{'a': 1}` ou `{}` vazio | Ordem de inserção | Mutável | Chaves únicas; valores podem repetir | Chave, `keys()`, `values()` | Nome associado à quantidade ou score |

# Perguntas gerais que podem cair na avaliação

- **List vs tuple?** A lista pode mudar; a tupla não. Ambas mantêm posições e aceitam duplicatas.
- **List vs set?** A lista mantém ordem e duplicatas; o set guarda apenas valores únicos, sem índice.
- **Set vs dict?** Set contém elementos; dict associa chaves únicas a valores. `{}` é dict vazio; `set()` é set vazio.
- **Mutable vs immutable?** Mutável pode mudar depois de criado; imutável não muda seu conteúdo.
- **Ordered vs unordered?** List, tuple e dict preservam uma ordem definida; set não promete ordem de iteração.
- **Quando usar valores únicos?** Use set quando duplicatas não fazem sentido, como conquistas de um jogador.
- **O que é chave/valor?** No inventário, a chave é o nome e o valor é a quantidade.
- **Generator vs list?** Generator produz sob demanda; list já armazena todos os elementos.
- **Yield vs return?** `yield` entrega e pausa; `return` termina a chamada/gerador.
- **O que faz `next()`?** Pede o próximo valor de um iterador/gerador.
- **O que é comprehension?** Sintaxe compacta para construir coleção transformando ou filtrando uma fonte.
- **O que são type hints?** Anotações que descrevem tipos esperados; não fazem validação automática em tempo de execução.
- **O que faz mypy?** Verifica estaticamente a coerência dos type hints.
- **O que faz flake8?** Aponta problemas de estilo e alguns erros simples de código.
- **Para que serve `try/except`?** Permite tratar erros esperados e continuar ou encerrar de modo controlado.
- **O que é `ValueError`?** Erro quando um valor tem formato/conteúdo inadequado, como `int('abc')`.
- **Como chegam argumentos de linha de comando?** Como strings em `sys.argv`; `argv[0]` identifica o programa.

# Revisão de 10 minutos antes da defesa

1. **Ex0:** `argv[0]` é o programa; `argv[1:]` são os argumentos; `len(argv)` inclui o programa.
2. **Ex1:** converta com `int()` em `try/except`; guarde válidos em lista; média = soma/quantidade; amplitude = máximo−mínimo.
3. **Ex2:** leia três floats, represente como tupla; `sqrt` da soma dos quadrados dá a distância; trate erro e EOF.
4. **Ex3:** set elimina duplicatas; união = qualquer jogador, interseção = todos, diferença = exclusivos ou faltantes; faltantes usam o catálogo inteiro.
5. **Ex4:** dict liga item a quantidade; descarte duplicatas; `keys`, `values`, `update`; empate mantém o primeiro; evite dividir por zero.
6. **Ex5:** `yield` produz sob demanda; `next()` pede um evento; mil eventos são impressos sem guardar mil tuplas; a lista de dez termina vazia.
7. **Ex6:** comprehension transforma ou filtra; o dict de scores usa nomes capitalizados; high scores têm `score > média`.

# Validação e cópia

Revisão de 6 de outubro de 2026: os sete arquivos têm os nomes exigidos e cada pasta `ex0`–`ex6` contém apenas seu `.py`. Não há testes, logs, caches ou arquivos auxiliares nessas pastas. Python 3.13.1, `flake8 .`, `mypy .` e `mypy --strict .` passaram; os casos da régua e extremos descritos acima terminaram sem traceback. Todas as funções têm type hints. O guia fica neste repositório de estudos.

Para a entrega oficial, copie **somente** `ex0/ft_command_quest.py`, `ex1/ft_score_analytics.py`, `ex2/ft_coordinate_system.py`, `ex3/ft_achievement_tracker.py`, `ex4/ft_inventory_system.py`, `ex5/ft_data_stream.py` e `ex6/ft_data_alchemist.py`, preservando as pastas. Não copie este guia.
