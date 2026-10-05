# Python 03 — Guia de estudos: coleções

Este guia segue o subject **Data Quest: Mastering Python Collections**, versão 3.0, que está em `subjetcs/py03.subject (1).pdf`. Procurei uma régua de correção e instruções `AGENTS.md` no projeto, mas não encontrei nenhum. Por isso, os requisitos abaixo vêm do subject. Não consultei o subject da lista anterior para definir requisitos.

## O tema da lista

O subject apresenta estruturas para organizar dados: listas, tuplas, conjuntos e dicionários. Cada uma serve a um tipo de problema. Listas mantêm uma sequência que pode mudar; tuplas guardam uma sequência que não deve mudar; conjuntos guardam valores únicos sem prometer uma ordem; dicionários associam chaves a valores. A lista também introduz geradores e comprehensions, uma forma compacta de construir coleções.

As instruções comuns pedem Python 3.10 ou posterior, flake8, type hints em todas as funções e métodos e uso de mypy. O subject também orienta a tratar exceções com cuidado e proíbe operações de arquivo. Não há uma lista global de funções autorizadas: cada exercício traz sua própria autorização, transcrita abaixo. O subject diz que os tipos `str`, `int` e `float`, com seus métodos e construtores, são permitidos.

## Exercício 0 — Command Quest

**Arquivo pedido:** `ex0/ft_command_quest.py`<br>
**Autorizado:** `import sys`, `sys.argv`, `len()`, `print()`.

O programa mostra o nome do script, os argumentos recebidos e o total de elementos em `sys.argv`. Essa lista inclui o nome do programa na posição inicial; os parâmetros passados pelo usuário vêm depois. Por isso, sem parâmetros o total ainda é 1. Com `hello world 42`, são três parâmetros e quatro elementos na lista.

O conceito principal é acessar uma lista por índice e entender argumentos de linha de comando. O código usa `split("/")` para exibir apenas a parte final do caminho como nome do programa.

**Relação com exercícios anteriores:** o subject diz que o uso de `sys.argv` é introduzido aqui. A ideia de validar entradas pode lembrar a lista anterior, mas não é um requisito importado dela.

## Exercício 1 — Score Cruncher

**Arquivo pedido:** `ex1/ft_score_analytics.py`<br>
**Autorizado:** `import sys`, `sys.argv`, `len()`, `sum()`, `max()`, `min()`, `print()`.

O programa transforma argumentos de texto em notas inteiras e guarda as válidas em uma lista. Cada conversão é protegida por `try/except ValueError`; parâmetros inválidos são informados e descartados. Se não houver notas válidas, exibe a mensagem de uso e termina. Caso haja, calcula quantidade, soma, média, maior, menor e amplitude (`maior - menor`).

O exemplo com cinco notas deve produzir total 9650, média 1930.0, maior 2300, menor 1500 e amplitude 800. A lista também exige continuar com as notas válidas quando entradas válidas e inválidas aparecem juntas.

O ponto para entender é que uma lista preserva as notas para percorrê-las e calcular estatísticas. A exceção de uma conversão não precisa interromper as conversões seguintes.

## Exercício 2 — Position Tracker

**Arquivo pedido:** `ex2/ft_coordinate_system.py`<br>
**Autorizado:** `import math`, `math.sqrt()`, `input()`, `round()`, `print()`.

`get_player_pos()` pede três coordenadas no formato `x,y,z`. O programa verifica se existem exatamente três partes e tenta converter cada uma em número decimal. Sintaxe errada ou coordenada não numérica gera uma mensagem e uma nova tentativa. Com entrada válida, a função devolve uma tupla de três coordenadas.

O programa imprime a tupla e cada componente, calcula a distância da origem e depois a distância entre as duas posições. Para a origem, aplica a raiz quadrada de `x² + y² + z²`; entre pontos, aplica a mesma fórmula às diferenças de cada coordenada. A saída do exemplo arredonda as distâncias para quatro casas decimais.

O conceito central é a tupla para representar um ponto com três valores relacionados. Depois de criada, a tupla não é alterada; uma nova posição é representada por outra tupla.

## Exercício 3 — Achievement Hunter

**Arquivo pedido:** `ex3/ft_achievement_tracker.py`<br>
**Autorizado:** `len()`, `print()`, `import random`, `random.*`, `set()`, `set.union()`, `set.intersection()`, `set.difference()`.

`gen_player_achievements()` escolhe aleatoriamente uma quantidade de conquistas de uma lista fixa, seleciona essa quantidade e devolve um conjunto. O programa cria conjuntos para pelo menos quatro jogadores.

O conjunto elimina duplicatas. `union` reúne as conquistas que aparecem em qualquer jogador; `intersection` encontra as presentes em todos; `difference` identifica o que só um jogador tem e o que falta para cada um alcançar todas as conquistas presentes no grupo. A ordem de exibição dos conjuntos pode mudar, pois conjuntos não representam uma ordem fixa. Um conjunto vazio aparece como `set()`; `{}` representa um dicionário vazio.

O código atual usa 14 conquistas e sorteia entre 5 e 10 para cada jogador. O subject sugere ajustar esses números para que os conjuntos pedidos provavelmente não fiquem vazios, mas não define um tamanho obrigatório nem uma probabilidade-alvo. Como os resultados são aleatórios, conjuntos de interseção ou de conquistas exclusivas ainda podem aparecer vazios; o próprio exemplo do subject mostra `set()` para jogadores sem conquistas exclusivas. Vale entender por que isso acontece e como os tamanhos escolhidos influenciam o resultado.

## Exercício 4 — Inventory Master

**Arquivo pedido:** `ex4/ft_inventory_system.py`<br>
**Autorizado:** `import sys`, `sys.argv`, `len()`, `print()`, `sum()`, `list()`, `round()`, `dict.keys()`, `dict.values()`, `dict.update()`.

Cada parâmetro deve ter o formato `nome:quantidade`. O programa separa nome e quantidade, converte a quantidade para inteiro e armazena os dados em um dicionário. Parâmetros malformados, quantidades inválidas e nomes repetidos são descartados com uma mensagem.

O programa exibe o dicionário, a lista de nomes, a quantidade total e a porcentagem de cada item. Também encontra o item mais e menos abundante; em caso de empate, deve escolher o primeiro passado na linha de comando. Por fim, adiciona `magic_item` e exibe o inventário atualizado.

O conceito é usar o nome como chave e a quantidade como valor. No Python 3.10, dicionários mantêm a ordem em que as chaves foram inseridas; percorrê-las nessa ordem permite preservar o primeiro item em empates. Se o inventário estiver vazio, não há item para comparar nem total pelo qual dividir; o código deve evitar essas operações e ainda atualizar o próprio dicionário com o novo item.

## Exercício 5 — Stream Wizard

**Arquivo pedido:** `ex5/ft_data_stream.py`<br>
**Autorizado:** `next()`, `range()`, `len()`, `print()`, `import typing`, `typing.Generator`, `import random`, `random.*`.

`gen_event()` é um gerador infinito: em cada pedido, escolhe um jogador e uma ação aleatórios e produz uma tupla. `yield` entrega um evento sem precisar construir uma lista infinita na memória. O programa consome e imprime mil eventos com `next()`.

Depois, monta uma lista com dez eventos. `consume_event()` escolhe um elemento aleatório, remove-o daquela lista e o entrega com `yield`, até a lista ficar vazia. O `for` percorre diretamente esse gerador e imprime o evento e o que restou.

O importante é distinguir um gerador, que produz valores sob demanda, de uma lista, que mantém seus valores disponíveis na memória. Como os eventos são aleatórios, as linhas concretas variam entre execuções; o comportamento verificável é a quantidade de eventos e o esvaziamento da lista.

## Exercício 6 — Data Alchemist

**Arquivo pedido:** `ex6/ft_data_alchemist.py`<br>
**Autorizado:** `import random`, `random.*`, `print()`, `len()`, `sum()`, `round()`.

O programa parte de nomes com capitalização mista. Uma list comprehension produz uma nova lista com todos capitalizados; outra seleciona somente os nomes que já estavam capitalizados na lista inicial. Depois, uma dict comprehension associa cada nome a uma pontuação aleatória. O programa calcula a média e usa outra dict comprehension para criar um dicionário apenas com pontuações acima dela.

Uma comprehension constrói uma coleção a partir de uma expressão e, se necessário, de um filtro. A forma compacta deve continuar legível. O subject diz que cada comprehension deve ficar em uma linha, exceto quando passar do limite de linha.

## O que saber demonstrar na avaliação

O subject diz que podem pedir para explicar escolhas de estruturas de dados, demonstrar operações de coleções ou estender os sistemas. Treine explicar:

- por que `sys.argv` contém o nome do script junto dos parâmetros;
- por que o programa guarda as notas válidas em uma lista e ignora as inválidas;
- como uma tupla representa as três coordenadas e como funciona a fórmula da distância;
- diferença entre união, interseção e diferença de conjuntos;
- como um dicionário liga cada item a uma quantidade e como desempatar pela ordem original;
- como `yield` e `next()` produzem eventos sob demanda;
- como uma list ou dict comprehension transforma e filtra dados.

## Perguntas de revisão

**Por que `len(sys.argv)` é 1 quando não há parâmetros?**<br>
Porque a lista ainda contém o nome do programa.

**O que acontece com uma nota que não pode ser convertida para inteiro?**<br>
A conversão gera `ValueError`; o programa informa o parâmetro e continua com as outras notas.

**Por que coordenadas são uma tupla?**<br>
Porque formam um conjunto fixo de três valores para representar um ponto.

**Qual a diferença entre `union` e `intersection`?**<br>
`union` junta elementos presentes em pelo menos um conjunto; `intersection` mantém os elementos presentes em todos os conjuntos indicados.

**Por que um set remove duplicatas?**<br>
Conjuntos armazenam valores únicos.

**Como o dicionário escolhe o primeiro item em caso de empate?**<br>
Percorrendo as chaves na ordem de inserção e atualizando o resultado só quando encontra quantidade estritamente maior ou menor.

**O que `yield` faz?**<br>
Entrega um valor do gerador e pausa sua execução até o próximo pedido.

**O que significa o `if` dentro de uma comprehension?**<br>
É um filtro: só os elementos que satisfazem a condição entram na nova coleção.

## Checklist final

| Exercício | Requisito do subject | Situação atual |
|---|---|---|
| 0 | Exibir nome, argumentos e total, com e sem argumentos | Atendido; exemplos executados |
| 1 | Converter notas, descartar inválidas e calcular estatísticas | Atendido; exemplos e mistura de entradas verificados |
| 2 | Repetir até obter três floats válidos e calcular distâncias | Atendido; exemplos de entrada executados |
| 3 | Quatro jogadores e união, interseção e diferenças de sets | Atendido; resultado varia. O subject sugere ajustar as quantidades para reduzir sets vazios, sem definir valores obrigatórios |
| 4 | Analisar inventário, desempatar pela ordem de entrada e adicionar item | Atendido após correção; exemplos e inventário vazio verificados |
| 5 | Gerar mil eventos, montar dez e consumir até esvaziar lista | Atendido estruturalmente; contagens verificadas |
| 6 | Duas list comprehensions e dict comprehensions de pontuação | Atendido estruturalmente; conteúdo aleatório varia |

O subject requer Python 3.10+, flake8 e type hints conferidos por mypy. Comandos executados neste workspace:

```bash
python3 --version
python3 -m flake8 --isolated --jobs=1 python03
python3 -m mypy --strict --cache-dir=/tmp/python03-mypy python03
python3 -m compileall -q python03
```

Para executar os scripts, use os caminhos do projeto. Exemplos:

```bash
python3 python03/ex0/ft_command_quest.py hello world 42
python3 python03/ex1/ft_score_analytics.py 1500 2300 1800 2100 1950
python3 python03/ex2/ft_coordinate_system.py
python3 python03/ex3/ft_achievement_tracker.py
python3 python03/ex4/ft_inventory_system.py sword:1 potion:5 shield:2
python3 python03/ex5/ft_data_stream.py
python3 python03/ex6/ft_data_alchemist.py
```

Para exercício 2, digite entradas inválidas e depois válidas para conferir que ele tenta novamente. Os exercícios 3, 5 e 6 usam aleatoriedade, então as saídas detalhadas mudam em cada execução. Não há régua de correção separada disponível neste projeto; os requisitos conferidos neste guia são os descritos no subject.
