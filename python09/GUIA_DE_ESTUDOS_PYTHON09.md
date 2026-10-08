# Guia de estudos — Python09: Cosmic Data

Este guia acompanha os três programas da lista. Para a entrega oficial, copie
somente `ex0/space_station.py`, `ex1/alien_contact.py` e
`ex2/space_crew.py`, cada um em sua pasta. O guia faz parte apenas deste
repositório pessoal de estudos.

## Preparação e verificação

Os comandos abaixo partem da raiz do repositório. Eles criam um ambiente
virtual temporário fora do Git e instalam as ferramentas com `pip`:

```bash
python3 -m venv /tmp/python09_study_venv
/tmp/python09_study_venv/bin/python -m pip install 'pydantic>=2,<3' flake8 mypy
/tmp/python09_study_venv/bin/python -m pip show pydantic
/tmp/python09_study_venv/bin/python python09/ex0/space_station.py
/tmp/python09_study_venv/bin/python python09/ex1/alien_contact.py
/tmp/python09_study_venv/bin/python python09/ex2/space_crew.py
/tmp/python09_study_venv/bin/flake8 python09
/tmp/python09_study_venv/bin/mypy python09
```

Use Python 3.10 ou superior. O ambiente virtual separa as dependências deste
estudo das demais instalações de Python. Os dados das demonstrações foram
criados para os exemplos: os geradores e datasets citados no subject não
estão neste repositório.

## Ex0 — `SpaceStation`

### Objetivo e conceitos

Criar um modelo de dados com limites simples. `SpaceStation` herda de
`BaseModel`, que valida os valores na criação do objeto. `Field` declara os
limites: `min_length` e `max_length` para strings; `ge` (maior ou igual) e
`le` (menor ou igual) para números.

### Como o código funciona

1. `station_id` aceita 3 a 10 caracteres e `name`, 1 a 50.
2. `crew_size` aceita 1 a 20. `power_level` e `oxygen_level` aceitam 0.0 a
   100.0, inclusive.
3. `last_maintenance: datetime` guarda data e hora. `is_operational` vale
   `True` quando omitido. `notes: str | None` aceita texto de até 200
   caracteres ou `None` e, quando omitido, vale `None`.
4. `main()` cria uma estação válida, mostra seus dados e tenta criar outra
   com 21 tripulantes. O `except ValidationError` mostra o campo e a
   mensagem do erro esperado, sem traceback.

`datetime` vem da biblioteca padrão. Pydantic pode converter uma string de
data e hora válida em `datetime`; isso é conversão de tipo, não uma alteração
na declaração do campo. Um valor inválido gera `ValidationError`.

### Testes e perguntas

Teste 1 e 20 tripulantes, depois 0 e 21. Teste 0.0 e 100.0 nos níveis de
energia e oxigênio. O que acontece ao omitir `is_operational`? **Resposta:**
o valor padrão é `True`. `notes` é obrigatório? **Resposta:** não; o valor
padrão é `None`.

## Ex1 — `AlienContact`

### Objetivo e conceitos

Validar campos individuais e regras que dependem da combinação de vários
campos. `ContactType` é um `Enum` com `radio`, `visual`, `physical` e
`telepathic`. Usar o enum limita os tipos de contato aceitos e permite
compará-los por nomes claros.

### Como o código funciona

1. `Field` limita `contact_id` a 5–15 caracteres, `location` a 3–100,
   `signal_strength` a 0.0–10.0, `duration_minutes` a 1–1440 e
   `witness_count` a 1–100.
2. `timestamp` é `datetime`. `message_received` aceita `None` ou uma string
   de até 500 caracteres e vale `None` quando omitido. `is_verified` vale
   `False` quando omitido.
3. `@model_validator(mode="after")` executa depois da validação dos campos.
   O método acessa os valores já convertidos por meio de `self`, lança
   `ValueError` para uma regra violada e retorna `self` quando tudo está
   correto. Ele verifica o prefixo `AC`, a verificação de contato físico,
   as três testemunhas em contato telepático e a mensagem em sinal acima de
   7.0.
4. `main()` apresenta um relato válido e captura o `ValidationError` de um
   relato inválido.

Pydantic pode transformar o texto `"radio"` em `ContactType.RADIO`, assim
como pode converter uma string de data e hora para `datetime`. Se o texto
não corresponder a um membro do enum, a validação falha.

### Testes e perguntas

Teste sinais 7.0 e um pouco acima de 7.0, contato físico verificado e não
verificado e contato telepático com 2 e 3 testemunhas. Quando a regra do
sinal forte se aplica? **Resposta:** somente quando
`signal_strength > 7.0`. Qual exceção externa reúne as falhas de
validação? **Resposta:** `ValidationError`.

## Ex2 — `CrewMember` e `SpaceMission`

### Objetivo e conceitos

Usar modelos aninhados: `SpaceMission.crew` é uma lista de objetos
`CrewMember`. `Rank` é um `Enum` com `cadet`, `officer`, `lieutenant`,
`captain` e `commander`. `launch_date` é `datetime`.

### Como o código funciona

1. `CrewMember` limita ID, nome, idade, especialização e anos de
   experiência. `is_active` vale `True` quando omitido.
2. `SpaceMission` limita ID, nome, destino, duração, orçamento e a lista de
   1 a 12 tripulantes. `mission_status` vale `"planned"` quando omitido.
3. O validador `after` verifica prefixo `M`, presença de captain ou
   commander, experiência suficiente nas missões com mais de 365 dias e
   atividade de todos os tripulantes. Cada violação lança `ValueError`; no
   caminho válido, o método retorna `self`.
4. Para a experiência, o código conta membros com pelo menos 5 anos e
   compara `experienced_count * 2` com o tamanho da tripulação. Isso exige
   2 experientes em uma equipe de 3 e 3 em uma equipe de 5, sem arredondar
   percentuais para baixo.
5. `main()` mostra a missão válida com os membros e captura o erro de uma
   missão sem captain nem commander.

Pydantic valida cada item de `crew` como `CrewMember`, inclusive quando
recebe dicionários. Se a idade do segundo membro for inválida, por exemplo,
o `ValidationError` aponta uma localização como `crew.1.age`: campo `crew`,
índice 1, campo `age`. Se todos os campos individuais forem válidos, então
rodam as regras do validador da missão. Erros dessas regras pertencem ao
modelo como um todo.

### Testes e perguntas

Teste tripulações com 1 e 12 membros, duração 365 e 366 dias, equipes ímpares
e um membro inativo. Uma missão curta precisa de 50% de experientes?
**Resposta:** não; essa regra só vale acima de 365 dias. Um `CrewMember`
inválido passa despercebido dentro de `crew`? **Resposta:** não; Pydantic
valida os modelos aninhados e informa onde está o erro.

## Decisões e leitura do subject

Os limites são inclusivos quando o subject apresenta intervalos como
`1-20`; apenas as regras escritas com `>` usam comparação estrita. Não há
regras adicionais de unicidade de IDs, datas futuras ou formato dos nomes.
As saídas de exemplo do PDF orientam a demonstração, sem exigir texto
idêntico. As restrições de cada exercício vêm desta lista, sem importar
regras de listas anteriores.

No Ex1, o subject exige mensagem recebida para sinal acima de 7.0, mas não
define se uma string vazia ou só com espaços conta como mensagem. Por escolha
de implementação confirmada para este estudo, ambas são rejeitadas. O código
usa `strip()` apenas para conferir se há conteúdo; o texto original é
preservado no modelo.
