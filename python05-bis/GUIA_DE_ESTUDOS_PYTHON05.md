# Guia de estudos — Python05-bis

Este guia acompanha os cinco exercícios do subject versão 1.0. A implementação
usa Python 3.10 ou mais recente, anotações de tipos e os imports autorizados por
exercício. Não usa `eval()`, `exec()` nem alterações em `sys.path`.

## Preparação para executar os exercícios

Execute os programas a partir da pasta `python05-bis`. Para instalar bibliotecas
e ferramentas sem alterar o Python global:

```bash
python3 -m venv /tmp/python05_estudos
source /tmp/python05_estudos/bin/activate
python3 -m pip install -r ex0/requirements.txt -r ex1/requirements.txt
python3 -m pip install flake8 mypy
```

Os exercícios 2–4 compartilham `alchemy/`. Seus imports alcançam somente módulos
criados neste projeto; eles não precisam das bibliotecas dos exercícios 0 e 1.
A `.gitignore` da raiz protege os nomes usuais de ambientes virtuais, `.env` e
caches. `ex1/.gitignore` também contém `.env`, como o subject exige.

## Exercício 0 — The Sealed Laboratory

O subject exige detectar o ambiente virtual, mostrar informações do Python e
dos diretórios de pacotes, orientar a criação de um ambiente e declarar as
mesmas dependências para pip e Poetry. Também exige mostrar versões instaladas
e instruções de instalação quando alguma dependência estiver ausente.

### Arquivos e lógica

- `ex0/construct.py` verifica se o Python atual está em um ambiente virtual.
  Fora dele, mostra como criar e ativar um. Dentro dele, mostra o caminho do
  ambiente e compara os locais de instalação de pacotes do ambiente e do Python
  global.
- `ex0/loading.py` tenta importar `pandas` e `numpy` e mostra as versões
  encontradas. Se alguma biblioteca faltar, explica como instalar as
  dependências com pip ou Poetry sem encerrar com erro.
- `ex0/requirements.txt` e `ex0/pyproject.toml` declaram as mesmas restrições
  de versão para as duas bibliotecas. O primeiro é usado pelo pip; o segundo,
  pelo Poetry.

### Conexões e conceitos

Um **ambiente virtual** tem seu próprio interpretador e diretório de pacotes.
`sys.prefix` aponta para o ambiente em uso; `sys.base_prefix` aponta para a
instalação base do Python. Quando os dois diferem, há um ambiente virtual ativo.
Ele separa pacotes de projetos diferentes, mas não isola arquivos, rede nem
variáveis de ambiente do sistema.

`site.getsitepackages()` mostra diretórios de instalação de pacotes. O programa
usa esse resultado para comparar o ambiente virtual com a instalação base.

Uma **dependência** é uma biblioteca de que o programa precisa. O pip lê as
restrições de `requirements.txt` e escolhe versões ao instalar. O Poetry lê as
restrições de `pyproject.toml` e registra as versões resolvidas em `poetry.lock`
quando se executa `poetry install`. Um lock permite repetir as mesmas versões.
O subject lista quatro arquivos para entregar em `ex0`; `poetry.lock` não faz
parte dessa lista. O teste com Poetry gerou o lock somente na cópia em `/tmp`.

`importlib.import_module()` importa cada biblioteca pelo nome. O programa
captura `ImportError` para tratar bibliotecas ausentes ou com problemas de
importação e continuar a checagem das demais.

### Como executar e testar

Execute a partir da raiz `python05-bis`. Use Python 3.10 ou mais recente.

```bash
# Fora de um ambiente virtual
python3 ex0/construct.py

# Crie um ambiente temporário fora do repositório
python3 -m venv /tmp/python05_lab
source /tmp/python05_lab/bin/activate

# Dentro do ambiente, antes de instalar as dependências
python3 ex0/construct.py
python3 ex0/loading.py

# Instale as dependências e confira as versões
python3 -m pip install -r ex0/requirements.txt
python3 ex0/loading.py

# Volte ao Python global
deactivate
python3 ex0/loading.py
```

Se usar Poetry, execute os comandos a partir de `ex0/`:

```bash
cd ex0
poetry install
poetry run python loading.py
```

O Poetry precisa estar instalado para esses comandos. Nesta revisão ele foi
instalado num ambiente temporário, e tanto `poetry install` quanto
`poetry run python loading.py` foram executados numa cópia do `ex0` em `/tmp`.
Não há erros intencionais neste exercício.

Verificação de estilo e tipos, a partir da raiz:

```bash
flake8 ex0/construct.py ex0/loading.py
mypy --strict ex0/construct.py ex0/loading.py
```

### Perguntas de avaliação

1. **Como o script detecta um ambiente virtual?** Compara `sys.prefix` e
   `sys.base_prefix`.
2. **O que o ambiente virtual isola?** O interpretador usado e seus pacotes;
   não cria uma barreira para arquivos ou rede.
3. **Por que testar antes e depois da instalação?** Para comprovar que a
   ausência das bibliotecas é tratada e que as versões aparecem após instalar.
4. **Qual é a diferença entre pip e Poetry aqui?** Ambos instalam as
   dependências declaradas; o Poetry também pode gerar um `poetry.lock` com as
   versões exatas resolvidas.
5. **Por que capturar `ImportError`?** Para informar o problema e o comando de
   instalação sem interromper o programa.
6. **Por que não adicionar o ambiente virtual ao repositório?** Ele depende da
   máquina e pode ser recriado a partir das declarações de dependências.

## Exercício 1 — The Oracle

### O que o subject exige

Ler configuração com `python-dotenv`, variáveis de ambiente e um `.env` de
 desenvolvimento. Mostrar uma diferença visível entre desenvolvimento e
produção, tratar configurações ausentes sem falhar e manter `.env` fora do Git.
As cinco variáveis são `MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, `LOG_LEVEL` e
`ZION_ENDPOINT`. Os imports autorizados são `os`, `sys` e `python-dotenv`, além
 de operações com arquivos.

### Arquivos e conexões

- `ex1/oracle.py`: carrega `.env`, lê as variáveis, escolhe valores padrão e
  imprime a situação da configuração.
- `ex1/requirements.txt`: declara `python-dotenv` para instalação com pip.
- `ex1/.env.example`: modelo com configurações locais e `API_KEY` vazia.
- `ex1/.gitignore`: impede que o `.env` local apareça entre os arquivos a enviar.

A biblioteca se instala como `python-dotenv`, mas é importada como `dotenv`.
`oracle.py` procura `.env` ao lado do próprio arquivo, usando `__file__` e
`os.path`. Isso funciona mesmo quando o diretório de execução é outro.

### Lógica e conceitos

`load_dotenv(env_path, override=False)` adiciona valores do arquivo ao ambiente
sem substituir variáveis que já existam no processo. Depois, `os.getenv()` lê
 esses valores. Uma variável vazia é tratada como configuração ausente; o programa
avisa e usa um valor padrão quando houver.

O subject deixa livre a demonstração da diferença entre os modos. Nesta
implementação:

| Configuração ausente | Desenvolvimento | Produção |
| --- | --- | --- |
| `DATABASE_URL` | `sqlite:///laboratory.db` | Sem valor padrão |
| `LOG_LEVEL` | `DEBUG` | `INFO` |
| `ZION_ENDPOINT` | `http://localhost:8000` | Sem valor padrão |
| `API_KEY` | Ausente, com aviso | Ausente, com aviso |

`MATRIX_MODE` ausente usa `development`. Um modo desconhecido também resulta em
 desenvolvimento, com aviso. O programa não abre conexões: “Configured” significa
que existe um valor, sem comprovar que um serviço está disponível. Chaves de API
 e URLs fornecidas pelo ambiente não são impressas, pois URLs também podem conter
credenciais.

A lógica usa dicionários para reunir a configuração, condicionais para os modos
 e uma lista dos campos ausentes para mostrar os avisos.

### Como executar e testar

Com `python-dotenv` instalado, execute primeiro sem criar `.env`:

```bash
python3 ex1/oracle.py
MATRIX_MODE=production python3 ex1/oracle.py
```

Para testar o arquivo de desenvolvimento:

```bash
cp ex1/.env.example ex1/.env
# Edite ex1/.env e preencha API_KEY somente nesse arquivo local.
python3 ex1/oracle.py
```

O exemplo tem chave vazia de propósito: o aviso de `API_KEY` deve continuar até
você preenchê-la. Para testar a precedência com um valor fictício:

```bash
MATRIX_MODE=production API_KEY=valor_ficticio LOG_LEVEL=WARNING \
  python3 ex1/oracle.py
API_KEY= python3 ex1/oracle.py
MATRIX_MODE=desconhecido python3 ex1/oracle.py
git check-ignore -v ex1/.env
```

Sem variáveis e sem `.env`, aparecem os padrões de desenvolvimento e avisos dos
cinco campos. Em produção sem configuração, banco, chave e endpoint ficam
marcados como ausentes. Com todas as variáveis preenchidas, não há avisos de
campos ausentes. Não há erros intencionais neste exercício.

### Perguntas de avaliação

1. **Quem vence: `.env` ou variável do processo?** A variável do processo,
   porque `override=False` impede sua substituição.
2. **`.env` e `.env.example` têm o mesmo papel?** O primeiro guarda valores
   locais; o segundo documenta as variáveis e pode ir ao Git sem segredos.
3. **O que `.gitignore` protege?** Impede a inclusão normal de arquivos ainda
   não rastreados. Não remove segredos de commits anteriores nem impede `git add
   -f`.
4. **Variáveis de ambiente são totalmente seguras?** Não. Podem aparecer em
   diagnósticos, logs ou processos com acesso suficiente. Evitar constantes no
   código reduz a exposição no repositório, mas ainda é preciso protegê-las.
5. **O programa testa uma conexão real?** Não; o exercício trata de configuração.
6. **Por que não escrever um parser próprio de `.env`?** O subject exige usar
   `python-dotenv`, que já interpreta esse formato.

## Exercício 2 — The Alembic

### O que o subject exige

Criar dois módulos chamados `elements.py`: um na raiz com fogo e água, outro
em `alchemy/` com terra e ar. Expor somente `create_air` como função da interface
`alchemy`. Demonstrar os imports com dois programas, incluindo uma tentativa
que deve falhar ao chamar `alchemy.create_earth()`.

### Arquivos e conexões

| Arquivo | Papel |
| --- | --- |
| `elements.py` | Define `create_fire()` e `create_water()` |
| `alchemy/elements.py` | Define `create_earth()` e `create_air()` |
| `alchemy/__init__.py` | Importa `create_air` para a interface do pacote |
| `ft_alembic_0.py` | Usa `import elements` e chama `elements.create_fire()` |
| `ft_alembic_1.py` | Usa `import alchemy`, chama ar e tenta chamar terra |

As quatro funções não recebem argumentos e retornam `str`. Os retornos exatos
são `Fire element created`, `Water element created`, `Earth element created` e
`Air element created`.

### Lógica e conceitos

Um módulo é um arquivo Python. Um pacote organiza módulos e tem uma interface
inicializada por `__init__.py`. `import elements` acessa o módulo da raiz;
`import alchemy` executa a inicialização do pacote e disponibiliza seus atributos.

`alchemy/__init__.py` importa `create_air`, mas não importa `create_earth` para
esse nível. A função de terra continua disponível em `alchemy.elements`; ela
não ficou privada. `__all__ = ["create_air"]` documenta a exportação, controla
`from alchemy import *` e permite que flake8 e mypy reconheçam o export. Quem faz
`alchemy.create_air` existir é o import, não a lista `__all__` sozinha.

### Como executar, testar e reconhecer o erro intencional

```bash
python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 -c "from alchemy.elements import create_earth; print(create_earth())"
```

O primeiro programa cria fogo. O segundo cria ar e termina com `AttributeError`
ao chamar `alchemy.create_earth()`. O terceiro comprova que terra existe no
submódulo. O mypy também deve apontar a ausência do atributo em
`ft_alembic_1.py`; o subject pede esse erro expressamente. Ele não foi escondido
com `type: ignore`.

### Perguntas de avaliação

1. **Por que existem dois `elements.py` sem conflito?** Eles têm nomes de
   import diferentes: `elements` e `alchemy.elements`.
2. **Por que ar funciona e terra falha via `alchemy`?** Apenas ar foi importado
   para os atributos da interface do pacote.
3. **`__all__` torna terra privada?** Não. É possível importá-la do submódulo.
4. **Por que deixar o mypy acusar um erro?** A chamada errada é uma demonstração
   exigida pelo exercício, não um defeito a esconder.

## Exercício 3 — Distillation and Transmutation

### O que o subject exige

Reutilizar os quatro elementos para criar duas poções e uma receita em um
subpacote. `recipes.py` precisa de pelo menos um import absoluto e um relativo.
O programa de destilação deve usar `from ... import ...`; o de transmutação,
`import ...` para alcançar o módulo da receita.

### Arquivos e conexões

- `alchemy/potions.py`: define `healing_potion()` e `strength_potion()`,
  reutilizando funções dos dois módulos de elementos.
- `alchemy/transmutation/__init__.py`: inicializa o subpacote; não precisa
  reexportar a receita.
- `alchemy/transmutation/recipes.py`: define `lead_to_gold()`, usando ar, a
  poção de força e fogo.
- `ft_distillation_0.py`: importa as duas funções de poção diretamente do módulo
  e exibe seus resultados.
- `ft_transmutation_0.py`: importa `alchemy.transmutation.recipes` e chama a
  receita pelo caminho completo.

### Lógica e conceitos

`healing_potion()` combina os resultados de terra e ar. `strength_potion()`
combina fogo e água. Ambas retornam texto, sem imprimir dentro da função:

```text
Healing potion brewed with 'Earth element created' and 'Air element created'
Strength potion brewed with 'Fire element created' and 'Water element created'
```

`lead_to_gold()` encaixa ar, a poção de força e fogo no texto da receita. As
aspas simples dentro da poção são preservadas, inclusive quando a poção aparece
 dentro de outras aspas no resultado da receita.

Um import absoluto começa pelo nome completo acessível ao interpretador, como
`from elements import create_fire`. Um import relativo começa com pontos e usa
 o pacote atual como referência. Em `recipes.py`, `from ..elements import
create_air` sobe de `alchemy.transmutation` para `alchemy`; `from ..potions
import strength_potion` alcança a poção no mesmo nível.

Os programas na raiz dão acesso aos módulos do projeto pelo mecanismo normal
 de execução do Python. Não é necessário alterar `sys.path`.

### Como executar e testar

```bash
python3 ft_distillation_0.py
python3 ft_transmutation_0.py
```

A destilação deve mostrar as duas poções. A transmutação deve mostrar a receita
com os resultados completos das funções utilizadas. Não há erros intencionais.
Não execute `recipes.py` como arquivo solto: seus imports relativos dependem do
contexto do pacote, estabelecido pelo programa da raiz.

### Perguntas de avaliação

1. **O que significa `..` no import?** Sobe um nível na hierarquia de pacotes;
   não é uma operação comum sobre o diretório de trabalho.
2. **Quando escolher um import absoluto?** Quando o caminho completo ajuda a
   identificar a origem do módulo, especialmente fora do pacote atual.
3. **Quando escolher um import relativo?** Quando os módulos pertencem ao mesmo
   pacote e a relação entre eles é o que interessa expressar.
4. **Por que retornar texto em vez de imprimir nas funções?** O retorno pode
   ser combinado por outras funções e testado diretamente.
5. **Por que a receita usa a função da poção?** Para reutilizar a composição já
   definida, em vez de repetir a implementação.

## Exercício 4 — Avoid the Explosion

### O que o subject exige

Criar dois pares de módulos com dependência mútua. O par claro precisa funcionar;
 o escuro precisa falhar de verdade por causa de imports mútuos no topo. O
spellbook fornece a lista de ingredientes e registra ou rejeita o feitiço usando
 o resultado do validador.

O validador aceita texto que contenha pelo menos um ingrediente permitido, sem
 distinguir maiúsculas de minúsculas. Terra, ar, fogo e água são os ingredientes
claros em inglês; os escuros são `bats`, `frogs`, `arsenic` e `eyeball`.

A instrução específica pede que as funções de ingredientes retornem `list[str]`.
Essa exigência específica prevalece sobre a orientação geral de retornar
strings nos exercícios 2–4. As funções de validação e registro retornam `str`.

### Arquivos e conexões

| Arquivo | Papel |
| --- | --- |
| `alchemy/grimoire/__init__.py` | Expõe `light_spell_record` pela interface do pacote |
| `light_spellbook.py` | Define `light_spell_allowed_ingredients()` e `light_spell_record(spell_name: str, ingredients: str)` |
| `light_validator.py` | Define `validate_ingredients(ingredients: str)` e consulta os ingredientes do spellbook |
| `dark_spellbook.py` | Define `dark_spell_allowed_ingredients()` e `dark_spell_record(spell_name: str, ingredients: str)`; importa o validador no topo |
| `dark_validator.py` | Define `dark_validate_ingredients(ingredients: str)`; importa a lista do spellbook no topo |
| `ft_kaboom_0.py` | Acessa o pacote grimoire e registra um feitiço claro |
| `ft_kaboom_1.py` | Tenta importar diretamente o spellbook escuro e registrar um feitiço |

Os cinco primeiros arquivos ficam em `alchemy/grimoire/`; os dois programas
ficam na raiz. A inicialização de grimoire não importa os módulos escuros,
permitindo que o exemplo claro funcione de forma independente.

### Lógica e conceitos

No par claro, o import de `validate_ingredients` fica **dentro** de
`light_spell_record()`. Ao inicializar o spellbook, o Python consegue definir
suas funções sem carregar imediatamente o validador. Quando o registro é
chamado, o spellbook já está pronto, e o validador pode importar a função de
ingredientes dele.

O validador usa `.lower()` e `any()` para verificar se há pelo menos um nome
permitido no texto. Por exemplo, `EARTH` e `copper and Earth` são válidos;
`wind`, texto vazio e `bats` são inválidos para magia clara.

O registro verifica o sufixo ` - VALID` do resultado. Buscar somente a palavra
`VALID` seria errado, pois `INVALID` também contém essa sequência. Os resultados
seguem o formato:

```text
Spell recorded: Fantasy (Earth, wind and fire - VALID)
Spell rejected: Test (copper - INVALID)
```

No par escuro, `dark_spellbook` tenta importar `dark_validate_ingredients` antes
 de definir sua própria função de ingredientes. O validador tenta importar essa
função do spellbook ainda incompleto. O Python encontra um módulo parcialmente
inicializado e levanta `ImportError`. A falha ocorre antes de registrar o
feitiço, e não foi simulada com um `raise` artificial.

### Como executar, testar e reconhecer o erro intencional

```bash
python3 ft_kaboom_0.py
python3 ft_kaboom_1.py
python3 -c "from alchemy.grimoire import light_spell_record; print(light_spell_record('Test', 'EARTH'))"
python3 -c "from alchemy.grimoire import light_spell_record; print(light_spell_record('Test', 'copper'))"
```

`ft_kaboom_0.py` registra o feitiço claro. `ft_kaboom_1.py` deve terminar com
`ImportError`, mencionando módulo parcialmente inicializado e import circular.
Essa falha é intencional. Importar primeiro o validador escuro também deve
falhar. O mypy consegue resolver os símbolos estaticamente e não precisa
apontar esse ciclo: o problema é a ordem de execução dos imports.

### Perguntas de avaliação

1. **O que é uma dependência circular?** Dois módulos dependem um do outro,
   diretamente ou por uma cadeia de imports.
2. **Toda dependência circular falha?** Não. A falha depende de quais símbolos
   são pedidos e do momento em que cada módulo precisa deles.
3. **Por que o import local resolve o exemplo claro?** Ele adia a busca pelo
   validador até que as funções do spellbook já existam.
4. **Que alternativas existem?** Extrair dados compartilhados para um terceiro
   módulo ou importar o módulo e acessar seus atributos só depois da
   inicialização. A escolha depende da organização do código.
5. **Por que não corrigir o par escuro?** O subject exige demonstrar a falha
   causada pelo desenho ingênuo dos imports.
6. **Uma lista de ingredientes é uma exceção ao retorno de strings?** Sim, o
   exercício exige explicitamente uma lista nessas duas funções.

## Revisão, testes executados e limites

A revisão de 08/10/2026 usou Python **3.13.1**. Todos os nove programas de
entrada foram executados. Os testes auxiliares e ambientes ficaram em `/tmp`.

| Parte | Resultado observado |
| --- | --- |
| `ex0/construct.py` | Distinguiu Python global de um ambiente virtual novo e mostrou os caminhos |
| `ex0/loading.py` sem bibliotecas | Informou pandas e numpy ausentes, com comandos pip e Poetry; saída 0 |
| `ex0/loading.py` com apenas numpy | Informou pandas ausente e a versão de numpy, mantendo as instruções de instalação; saída 0 |
| `ex0/loading.py` após pip | Mostrou pandas 2.3.3 e numpy 2.5.3; saída 0 |
| Poetry 2.5.1 | `poetry check`, `poetry install` e execução de `loading.py` passaram numa cópia temporária; mesmas versões do pip |
| `ex1/oracle.py` | 12 verificações passaram, incluindo configuração ausente, arquivo `.env`, precedência, produção, valores vazios e ocultação de segredos fictícios |
| Exercícios 2–4 | 35 verificações passaram, incluindo os seis programas, retornos exatos, ingredientes válidos e inválidos e as duas falhas exigidas |
| `flake8 .` | Saída 0, sem problemas |
| mypy sobre `.` | 20 arquivos analisados; somente o erro intencional de atributo em `ft_alembic_1.py` |
| Estrutura, imports e tipos | Árvore conferida, imports autorizados, funções anotadas e sintaxe aceita pela análise com alvo Python 3.10 |
| Git | `.env`, nomes usuais de ambientes e caches reconhecidos por `git check-ignore`; nenhum desses arquivos foi criado no projeto |

Para repetir a análise estática com as dependências e ferramentas instaladas
no ambiente ativado:

```bash
flake8 .
mypy .
mypy --strict --python-version 3.10 .
```

O resultado esperado do mypy é **um erro**, no acesso intencional a
`alchemy.create_earth()`. Na revisão, foi indicado também `--python-executable`
para o interpretador temporário com as dependências e `--cache-dir` para um
 diretório em `/tmp`, pois a ferramenta foi chamada de fora desse ambiente.

As instalações pip e Poetry precisaram de execução autorizada fora do sandbox
para acessar a rede. O `poetry check` aceitou o `pyproject.toml` existente, mas
emitiu avisos de depreciação sobre metadados em `[tool.poetry]`. Esses avisos não
impediram a instalação; o `ex0` foi preservado.

**Limites da validação:** não houve execução em um interpretador Python 3.10 nem
no Windows. A compatibilidade de sintaxe e tipos com Python 3.10 foi verificada,
mas não substitui um teste de execução nessa versão. Não há conexões reais com
bancos ou serviços para testar: o oracle somente consulta configurações. Não
restaram dúvidas sobre os requisitos que impedissem a implementação.

Os arquivos do projeto não foram commitados nem enviados por push. Antes da
avaliação, pratique criar um ambiente novo e explique os imports e as duas
falhas intencionais sem depender deste guia.
