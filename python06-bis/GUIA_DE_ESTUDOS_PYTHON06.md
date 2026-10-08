# Guia de estudos — Python 06 bis

Este guia é material de estudo pessoal. Para a entrega oficial, copie apenas os arquivos de código pedidos no subject. Execute os comandos abaixo de dentro da pasta `python06`, que funciona como raiz do projeto.

## Exercício 0 — `data_processor.py`

**Objetivo.** Criar uma interface abstrata para processar números, textos e registros de log, com validação antes da ingestão e extração em ordem de chegada.

**Conceitos.** `ABC` impede instanciar a classe base enquanto faltarem métodos abstratos. `validate` e `ingest` são sobrescritos em cada classe concreta. `output` é compartilhado por herança. `Any` na assinatura de `validate` permite examinar uma entrada desconhecida; os tipos de `ingest` mostram o que cada processador aceita.

**Fluxo.** Primeiro, `validate` examina a entrada inteira. `ingest` repete a validação, transforma cada item em texto e o guarda como `(rank, valor)`. `output` remove o item mais antigo. O rank é atribuído quando o item entra e continua crescente após as saídas.

**Decisões.** Números booleanos são rejeitados, apesar de `bool` herdar de `int`. Listas e dicionários vazios são rejeitados porque não identificam um tipo de dado útil. Logs com `log_level` e `log_message` usam o formato `NÍVEL: mensagem`; outros dicionários válidos de `str` para `str` usam `chave=valor`. Uma ingestão inválida gera `ValueError`; `output` sem itens gera `IndexError`. Cada ingestão inválida é recusada por inteiro, sem alterar a fila.

**Teste.** `python3 data_processor.py`. No exemplo, a chamada `numeric.ingest("foo")` é propositalmente incompatível com a anotação; ela demonstra a exceção e é o único erro esperado de mypy.

**Perguntas prováveis.** Por que `DataProcessor` não pode ser instanciado? O que ocorre se uma lista contém um único item inválido? Por que o rank não é recalculado depois de `output`? Por que `bool` exige um cuidado especial?

## Exercício 1 — `data_stream.py`

**Objetivo.** Receber dados de tipos diferentes e encaminhá-los aos processadores registrados, sem conhecer suas implementações internas.

**Conceitos.** Polimorfismo: todos os processadores oferecem `validate` e `ingest`, mas cada um responde segundo seu tipo. O laço `for` com `else` identifica quando ninguém aceitou um elemento.

**Fluxo.** `register_processor` mantém os objetos na ordem de cadastro. `process_stream` examina cada elemento, envia ao primeiro processador cuja validação retorna `True` e mostra um erro se nenhum o aceitar. `print_processors_stats` mostra o total já ingerido e o número ainda pendente. A demonstração imprime os números antes e depois de consumir valores.

**Decisões.** Se dois processadores aceitarem a mesma entrada, o primeiro registrado a recebe. Um item sem processador gera mensagem e não interrompe os itens seguintes. A estatística total é acumulada; a quantidade pendente diminui com `output`.

**Teste.** `python3 data_stream.py`.

**Perguntas prováveis.** Como adicionar um quarto processador sem mudar o roteador? Qual a diferença entre total e pendente? O que acontece quando só um processador está registrado?

## Exercício 2 — `data_pipeline.py`

**Objetivo.** Consumir até `nb` itens de cada processador e entregar os resultados a um exportador compatível.

**Conceitos.** `Protocol` define uma interface estrutural: um plugin não precisa herdar de `ExportPlugin`, só fornecer `process_output` com a assinatura correta. A nova `DataStream` herda o roteamento do exercício 1. CSV e JSON são montados manualmente, sem importar bibliotecas de exportação.

**Fluxo.** `output_pipeline` percorre os processadores em ordem de registro. Para cada um, extrai `min(nb, pendentes)` tuplas `(rank, valor)` e chama o plugin uma vez. O plugin CSV escreve uma linha de campos; o JSON cria um objeto cujas chaves são `item_` seguido do rank.

**Decisões.** `nb` negativo gera `ValueError`; zero não consome valores. CSV coloca aspas em campos com vírgula, aspas ou quebra de linha, dobrando aspas internas. JSON escapa aspas, barras invertidas e caracteres de controle. Se o processador está vazio, o CSV imprime uma linha vazia e o JSON imprime `{}`. Os plugins escrevem em stdout, como nos exemplos.

**Teste.** `python3 data_pipeline.py`. Para estudar os escapes, experimente campos com `,`, `"`, `\n` e `\t`.

**Perguntas prováveis.** Por que um plugin funciona sem herdar de `ExportPlugin`? Qual é a diferença entre `Protocol` e `ABC`? Por que usar `min(nb, pendentes)`? Por que CSV exige aspas em certos campos?

## Exercício 3 — `ex3/`, `battle.py`, `capacitor.py`

**Objetivo.** Criar famílias de criaturas por fábricas abstratas e oferecer transformação apenas às criaturas que possuem essa capacidade.

**Conceitos.** `Creature` é uma classe abstrata com `attack` e o método herdado `describe`. `TransformCapability` é outra classe abstrata e não herda de `Creature`. `Shiftling` e `Morphagon` combinam as duas por herança múltipla. `CreatureFactory` define a criação de base e evolução; as duas fábricas escolhem as classes concretas.

**Fluxo.** `battle.py` recebe fábricas, cria criaturas por seus métodos comuns e chama `describe`/`attack`. `capacitor.py` usa a fábrica de transformação, verifica a capacidade com `isinstance`, transforma, ataca novamente e reverte.

**Decisões.** Os métodos de ação retornam mensagens; os roteiros cuidam da impressão. Cada instância transformável inicia com `transformed = False`. O `__init__.py` de `ex3` publica somente as fábricas; `Creature` e a capacidade são importáveis de `ex3.creatures` para quem precisa dos tipos, sem publicar criaturas concretas na interface do pacote.

**Teste.** `python3 battle.py` e `python3 capacitor.py`.

**Perguntas prováveis.** Por que a capacidade não herda de `Creature`? Como a fábrica oculta a classe concreta de quem a usa? Onde o estado transformado é guardado? Por que `battle.py` pode lidar com as duas famílias sem testar seus nomes?

## Exercício 4 — `ex4/`, `tournament.py`

**Objetivo.** Variar a ação de combate por estratégia e organizar confrontos entre todos os pares de oponentes.

**Conceitos.** `BattleStrategy` obriga `is_valid` e `act`. `NormalStrategy` ataca qualquer `Creature`. `AggressiveStrategy` verifica `TransformCapability` com `isinstance` e executa transformação, ataque e reversão. `InvalidStrategyError` representa uma incompatibilidade específica.

**Fluxo.** Cada oponente é `(fábrica, estratégia)`. O laço externo escolhe o primeiro participante; o interno começa no índice seguinte. Assim, cada par não ordenado luta exatamente uma vez. Para cada confronto, são criadas criaturas base novas e chamadas as estratégias correspondentes. A exceção encerra o torneio; o roteiro principal a captura para mostrar o caso de erro.

**Decisões.** A validade é checada no momento de `act`, de modo que a demonstração de erro executa a primeira estratégia antes de encontrar a segunda inválida. `try/finally` garante a reversão após um ataque agressivo, inclusive se o ataque levantar exceção. As estratégias verificam tipos/capacidades, nunca a família concreta.

**Teste.** `python3 tournament.py`. Com três participantes, o total de confrontos deve ser `3 × 2 / 2 = 3`.

**Perguntas prováveis.** Como o `isinstance` permite uma nova família transformável? Quantas lutas há para `n` oponentes? O que muda ao trocar a estratégia de um oponente? Como a exceção interrompe o torneio?

## Verificações gerais

Execute os seis roteiros: `python3 data_processor.py`, `python3 data_stream.py`, `python3 data_pipeline.py`, `python3 battle.py`, `python3 capacitor.py` e `python3 tournament.py`.

Verifique estilo com `flake8 .`. Verifique tipos com `mypy --strict .`. O exemplo de ingestão inválida em `data_processor.py` produz intencionalmente um erro de argumento em mypy. Os demais erros devem ser investigados e corrigidos.
