# Python04 — Guia de Estudos e Defesa

Material local de revisão baseado no subject **Data Archivist**, versão 3.0. O subject é a referência para a avaliação. Este guia explica a implementação atual; não substitui o enunciado e não é um arquivo solicitado para entrega.

## 1. Objetivo geral da lista

Python04 ensina a abrir arquivos e trabalhar com **file objects**: ler, escrever, fechar e tratar exceções. Também apresenta os três streams padrão (`stdin`, `stdout`, `stderr`) e, no último exercício, context managers com `with`.

| Exercício | Progressão |
|---|---|
| ex0 | `open()` → `read()` → `close()` |
| ex1 | ler → transformar linhas → `write()` |
| ex2 | separar `stdin`, `stdout` e `stderr` |
| ex3 | `with` + `secure_archive()` |

## 2. Regras gerais do subject

- **Python 3.10 ou posterior:** a anotação `str | None`, por exemplo, funciona a partir dessa versão.
- **flake8:** o código deve respeitar o linter.
- **Type hints e mypy:** todas as funções e métodos devem ter anotações; mypy ajuda a verificá-las.
- **Exceções:** as funções devem tratar falhas com cuidado, evitando travamentos inesperados.
- **Entrega:** somente `ex0/ft_ancient_text.py`, `ex1/ft_archive_creation.py`, `ex2/ft_stream_management.py` e `ex3/ft_vault_security.py` são pedidos. Apenas o conteúdo do repositório será avaliado. Este guia não deve entrar na entrega.
- **`with`:** é introduzido no ex3 e não pode ser usado antes dele.
- **Tipos e coleções gerais permitidos:** `str`, `int`, `float`, `list`, `dict`, `set` e `tuple`, com seus métodos e construtores. Cada exercício tem ainda sua lista `Authorized`.
- **Saída:** os exemplos sugerem o formato; mensagens podem variar se mantiverem a estrutura e as informações essenciais.

## 3. EX0 — `ft_ancient_text`

### O que o subject pede

Receber um caminho pela linha de comando, ler e mostrar o conteúdo como `cat`, acrescentar cabeçalho e rodapé e tratar arquivo inexistente ou inacessível.

### Authorized

`import sys`, `sys.argv`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.close()` e `print()`.

### Explicação detalhada do código atual

`sys.argv` guarda os argumentos: posição 0 = nome do script; posição 1 = caminho. `len(sys.argv) != 2` detecta falta ou excesso. Em `_, filename = sys.argv`, `_` recebe o nome do script, que não será usado; `filename` recebe o caminho.

`open(filename, "r")` abre para leitura e devolve um **objeto de arquivo**, não o conteúdo. `typing.IO[str]` anota um arquivo de texto. `file_obj.read()` devolve uma `str` com todo o texto. `close()` libera o recurso. O conteúdo é mostrado entre separadores.

`file_obj` começa em `None` porque `open()` pode falhar antes de devolver um objeto. Seu tipo é `typing.IO[str] | None`. Em `finally`, `if file_obj is not None` impede chamar `close()` quando não há arquivo. `try` contém operações que podem falhar; `except Exception as e` captura a falha em `e` e permite mostrar sua causa; `finally` executa também após falha de leitura. Não se usa `with` porque o subject o proíbe até o ex3.

**Fluxo válido:** conferir argumentos → mostrar cabeçalho → abrir → ler → mostrar → fechar → mostrar mensagem de fechamento → executar `finally`, agora com `file_obj = None`.

**Fluxo com arquivo inexistente:** conferir argumentos → mostrar cabeçalho → `open()` lança exceção → executar `except` → executar `finally`; como `file_obj` ainda é `None`, não há arquivo a fechar.

**Perguntas de defesa:**

- O que `open()` retorna? Um objeto de arquivo, anotável como `typing.IO[str]`.
- O que `read()` retorna? Uma `str` com o conteúdo.
- Por que fechar arquivos? Para liberar o recurso e concluir seu uso.
- Se `open()` falhar, o que acontece? O controle vai ao `except`; não há objeto a fechar.
- Qual a diferença entre `except` e `finally`? O primeiro trata a falha; o segundo executa ao sair da tentativa.
- Por que não usar `with`? Só é autorizado a partir do ex3.

## 4. EX1 — `ft_archive_creation`

### O que o subject pede

Partir do ex0, adicionar `#` ao fim de cada linha, mostrar a transformação, pedir um destino e salvar somente se houver nome. Criar ou substituir o destino.

### Authorized

`import sys`, `sys.argv`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.write()`, `io.close()`, `print()` e `input()`.

### O que mudou em relação ao ex0

Depois de ler e fechar a origem, o código transforma o texto e usa `input()` para pedir o destino. A origem é aberta com `"r"`; o destino, com `"w"`.

`content.splitlines()` produz uma lista de linhas sem os separadores. A list comprehension `[line + "#" for line in lines]` cria outra lista com um `#` adicionado a cada linha. `"\n".join(transformed_lines)` une as linhas transformadas. Se a origem terminava em `\n`, o código acrescenta uma quebra final; se não terminava, o destino também não termina. Arquivo vazio continua vazio. Linha vazia vira `#`. Linha que já terminava em `#` recebe outro e vira, por exemplo, `a##`.

A leitura em modo texto e `splitlines()` normalizam CRLF e `\r` para `\n`; os bytes originais dessas quebras não são preservados. O subject exige o `#` em cada linha, mas não exige preservar os bytes das quebras.

`input()` devolve a resposta sem o Enter final. Se a resposta for vazia, não há gravação. O código também trata uma resposta só de espaços como vazia por meio de `strip()`. Se houver nome, `open(new_filename, "w")` cria o arquivo se necessário ou **trunca o arquivo existente no momento da abertura**. `write(new_content)` envia o texto e `close()` conclui a operação. `try`/`except` tratam erro de leitura ou escrita; `finally` fecha um objeto que permaneça aberto. A falha pode acontecer ao abrir, escrever ou fechar.

**`"r"` versus `"w"`:** `"r"` exige um arquivo existente e lê; `"w"` escreve, cria um destino ausente e apaga o conteúdo anterior de um destino existente.

**Perguntas de defesa:**

- O que `splitlines()` faz? Separa o texto em linhas sem os separadores.
- O que a list comprehension cria? Uma lista nova com `#` acrescentado em cada linha.
- O que `join()` faz? Une essas linhas com `\n`.
- Por que conferir newline final? Para manter sua presença ou ausência.
- O que acontece com arquivo vazio? O conteúdo transformado permanece vazio.
- O que `"w"` faz com arquivo existente? Trunca e substitui seu conteúdo.
- Se o destino não puder ser aberto? O erro é tratado e nada é salvo ali.

## 5. EX2 — `ft_stream_management`

### O que o subject pede e Authorized

Manter as operações do ex1, enviar erros de exceções ao fluxo de erro com prefixo claro e obter o destino sem `input()`. Authorized: `import sys`, `sys.argv`, `sys.stdin`, `sys.stdout`, `sys.stderr`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.readline()`, `io.write()`, `io.flush()`, `io.close()` e `print()`.

### Três streams diferentes

| Stream | Papel | Exemplo |
|---|---|---|
| `sys.stdin` | Entrada padrão | Texto digitado ou enviado por pipe |
| `sys.stdout` | Saída normal | Cabeçalho, conteúdo, pergunta, confirmação |
| `sys.stderr` | Saída de erro | Exceção ao abrir ou salvar |

`sys.stdout.write("Enter ...")` escreve o prompt sem acrescentar automaticamente uma quebra de linha. `sys.stdout.flush()` força a saída pendente antes da espera; sem ele, o prompt pode ficar em buffer. `sys.stdin.readline()` lê uma linha e normalmente **mantém `\n`**; ao encontrar EOF, devolve `""`. `rstrip("\r\n")` remove quebras finais `\r` e `\n` do nome. `sys.stderr.write(...)` envia a mensagem ao canal de erro de fato.

`input()` também recebe texto, mas normalmente remove o Enter e pode mostrar o prompt. Ele era autorizado no ex1; no ex2 o subject exige entrada sem esse built-in. Aqui escrever o prompt e ler a resposta são duas operações separadas. Imprimir `[STDERR]` com `print()` comum **não** muda o canal: por padrão, `print()` escreve em stdout. O código usa `sys.stderr.write()` para os erros. Após falha de gravação, `Data not saved.` é uma informação normal em stdout; a causa da exceção vai para stderr.

Exemplos de terminal, executados a partir de `ex2` com uma origem existente:

```bash
python3 ft_stream_management.py origem.txt > stdout.txt
python3 ft_stream_management.py origem.txt 2> stderr.txt
python3 ft_stream_management.py origem.txt > stdout.txt 2> stderr.txt
```

`1` é stdout (`>` equivale a `1>`); `2` é stderr (`2>`). Para provar a separação, use uma origem inexistente e confira que o cabeçalho foi para `stdout.txt`, enquanto o erro foi para `stderr.txt`. Uma linha enviada ao programa por pipe entra via `sys.stdin`.

**Perguntas de defesa:**

- Qual diferença entre stdout e stderr? São canais distintos para saída normal e erros.
- Por que `[STDERR]` sozinho não basta? É apenas texto; a operação de escrita define o canal.
- Como provar o canal? Redirecionar `> stdout.txt 2> stderr.txt` e examinar os arquivos.
- Para que serve `flush()`? Para mostrar a pergunta antes de esperar entrada.
- Qual diferença entre `input()` e `readline()`? `readline()` lê diretamente do stream, normalmente mantém newline e devolve `""` em EOF.
- Por que remover `\r\n`? São terminadores da linha recebida, não parte do nome desejado.

## 6. EX3 — `ft_vault_security`

### O que o subject pede e Authorized

Criar `secure_archive()` para ler ou escrever arquivos, devolver `(bool, str)` com status e texto e usar `with` para gerenciar o arquivo. Authorized: `open()`, `read()`, `write()` e `print()`; os tipos padrão das regras gerais continuam permitidos.

### Assinatura da função

```python
def secure_archive(
    filename: str,
    action: str = "read",
    content: str | None = None,
) -> tuple[bool, str]:
```

`filename` é obrigatório. `action` é opcional e vale `"read"` por padrão. `content` também é opcional: `str | None` significa texto ou ausência de texto. O retorno `tuple[bool, str]` tem um booleano e uma string. Leitura válida retorna `(True, conteúdo)`; escrita válida retorna `(True, confirmação)`; falha retorna `(False, mensagem)`.

Com `action == "read"`, o código abre em `"r"`, lê e retorna os dados. Com `action == "write"`, abre em `"w"`, grava o conteúdo informado ou `""` se for `None`, e confirma. Ação inválida retorna `(False, "Unsupported action: ...")` sem abrir arquivo.

`with open(filename, "r") as f:` abre o arquivo e entra em um bloco gerenciado. O objeto retornado por `open()` funciona como **context manager**: ao sair do bloco, fecha o arquivo, mesmo se `read()` ou `write()` falhar. O erro ainda chega ao `except`, que o transforma em mensagem. Nos exercícios anteriores, o fechamento é feito manualmente com `try`/`finally`; o subject só introduz e autoriza `with` no ex3.

```python
arquivo = open(nome, "r")
try:
    dados = arquivo.read()
finally:
    arquivo.close()

with open(nome, "r") as arquivo:
    dados = arquivo.read()
```

O exemplo de `main()` usa `ancient_fragment.txt`, que não é um arquivo pedido para entrega. Sem ele no diretório de execução, a demonstração de leitura válida e escrita seguinte é pulada. A função pode ser testada diretamente com outro arquivo.

**Perguntas de defesa:**

- O que é context manager? Um objeto que define ações ao entrar e sair de um bloco `with`.
- Quem fecha o arquivo? O context manager do objeto aberto.
- Fecha mesmo se `read()` falhar? Sim, ao sair do bloco.
- O que significa `tuple[bool, str]`? Indicador de sucesso e texto associado.
- O que grava com `content=None`? Uma string vazia.
- E uma ação inválida? Retorna falha sem abrir arquivo.

## 7. Exceções

`try` contém operações que podem falhar. Sem erro, o fluxo segue e `except` não executa. Com erro, o restante do `try` é pulado e o `except` compatível executa. `finally` executa depois de ambos os caminhos, inclusive quando há `return`; aqui ajuda a fechar arquivos abertos.

`FileNotFoundError` é um exemplo de falha ao abrir um caminho inexistente. `PermissionError` indica falta de permissão. O código atual não captura cada classe separadamente: usa **`except Exception as e`**, que captura essas e outras exceções comuns. `e` é o objeto de exceção. `str(e)` produz o texto usado no retorno de ex3; nos outros scripts, a f-string também mostra a mensagem de `e`.

## 8. File object

`open()` **não** retorna o conteúdo. Ele devolve um objeto que representa a conexão aberta com o arquivo. Depois, `file.read()` retorna o texto como `str`; `file.write(texto)` o envia para gravação. `typing.IO[str]` anota um objeto de arquivo em modo texto. Ele precisa ser fechado: explicitamente com `close()` nos ex0–ex2 ou automaticamente pelo `with` no ex3.

## 9. Modos de abertura

| Modo | Finalidade | Precisa existir? | Cria? | Sobrescreve? |
|---|---|---|---|---|
| `"r"` | Ler | Sim | Não | Não |
| `"w"` | Escrever | Não | Sim, se não existir | Sim, trunca ao abrir |

Estes são os modos usados nos exercícios. A tabela não apresenta recursos adicionais autorizados.

## 10. Type hints do projeto

| Anotação | Significado |
|---|---|
| `str` | Texto: caminho, conteúdo ou mensagem |
| `None` | Ausência de valor |
| `str | None` | Texto ou ausência de texto |
| `typing.IO[str]` | Objeto de arquivo de texto |
| `typing.IO[str] | None` | Objeto de arquivo ou ausência de objeto |
| `tuple[bool, str]` | Status booleano e texto |
| `list[str]` | Lista de linhas em texto |

Type hints documentam expectativas e permitem a mypy encontrar incompatibilidades sem executar o programa. `typing.Optional` foi removido dos ex0–ex2 porque as listas `Authorized` citam `typing.IO`, mas não `typing.Optional`. `typing.IO[str] | None` mantém o significado em Python 3.10+.

## 11. flake8 x mypy

**flake8** verifica estilo e problemas estáticos, como certas violações de formatação. **mypy** verifica coerência das anotações de tipos. Passar em um não implica passar no outro. Nenhum substitui testes funcionais: código bem formatado e tipado ainda pode salvar dados errados.

## 12. Casos de teste importantes

- **EX0:** [ ] sem argumento; [ ] argumentos demais; [ ] arquivo normal; [ ] vazio; [ ] inexistente; [ ] sem permissão; [ ] newline final; [ ] sem newline final; [ ] fechamento após falha.
- **EX1:** [ ] casos de leitura do ex0; [ ] não salvar com nome vazio; [ ] salvar conteúdo vazio; [ ] novo arquivo; [ ] sobrescrever; [ ] origem vazia; [ ] várias linhas; [ ] linha vazia; [ ] erro de escrita; [ ] conferir bytes salvos.
- **EX2:** [ ] casos anteriores; [ ] `stdin`; [ ] `stdout`; [ ] `stderr`; [ ] redirecionamento separado; [ ] EOF; [ ] ausência de `input()`.
- **EX3:** [ ] leitura válida; [ ] inexistente; [ ] sem permissão; [ ] escrita; [ ] sobrescrita; [ ] `None`; [ ] string vazia; [ ] ação inválida; [ ] fechamento em sucesso e falha.

Para testar permissão, use um arquivo temporário e retire as permissões durante o teste; restaure-as ao fim. A possibilidade de testar depende do ambiente. Para erro de gravação, use um destino temporário inválido, nunca um arquivo importante.

## 13. Possíveis pegadinhas da avaliação

- Dizer que `open()` retorna string: retorna um file object.
- Esquecer `close()` nos ex0–ex2 ou não saber explicar `finally`.
- Achar que escrever `[STDERR]` com `print()` transforma a saída em stderr.
- Confundir `stdin` (entrada), `stdout` (saída normal) e `stderr` (erros).
- Usar `input()` no ex2 ou `with` antes do ex3.
- Não saber que `"w"` cria ou trunca o destino ao abrir.
- Não saber explicar os dois itens de `tuple[bool, str]`.
- Achar que `with` esconde erros: ele fecha o recurso, mas a exceção ainda precisa ser tratada.
- Tratar os exemplos de mensagem como texto obrigatório; o subject exige a informação essencial.

## 14. Perguntas de peer evaluation

### ex0

1. **Quantos itens deve haver em `sys.argv`?** Dois: script e caminho.
2. **Por que conferir `len(sys.argv)`?** Para rejeitar quantidade errada de argumentos.
3. **O que significa `_` no desempacotamento?** Recebe o nome do script, que não será usado.
4. **O que `open(..., "r")` devolve?** Um objeto de arquivo de texto.
5. **O que `read()` devolve?** Uma `str` com o conteúdo.
6. **Por que `file_obj` começa em `None`?** `open()` pode falhar antes de criar o objeto.
7. **Quando `finally` executa?** Ao sair da tentativa, com ou sem erro.
8. **Por que não há `with`?** Só é autorizado a partir do ex3.

### ex1

9. **O que `splitlines()` faz?** Divide texto em linhas sem separadores.
10. **O que a list comprehension constrói?** Outra lista com `#` em cada linha.
11. **O que `join()` faz?** Une as linhas transformadas com `\n`.
12. **E se não houver newline final?** O destino também não terá.
13. **E se houver linha vazia?** Ela recebe `#`.
14. **E se uma linha já terminar em `#`?** Recebe mais um `#`.
15. **O que `input()` devolve?** Texto digitado sem o Enter final.
16. **O que `"w"` faz com destino existente?** Trunca e substitui o conteúdo.

### ex2

17. **O que é `stdin`?** Entrada padrão.
18. **O que é `stdout`?** Saída normal.
19. **O que é `stderr`?** Saída de erro.
20. **Por que `[STDERR]` impresso não basta?** Prefixo é texto; o canal depende da escrita.
21. **Como testar a separação?** Usar `> stdout.txt 2> stderr.txt`.
22. **Para que serve `flush()`?** Para mostrar o prompt antes de ler.
23. **O que `readline()` normalmente preserva?** A quebra `\n`.
24. **O que `readline()` retorna em EOF?** Uma string vazia.
25. **Por que `input()` não é usado?** O ex2 exige entrada sem esse built-in.

### ex3

26. **Qual ação é padrão?** `"read"`.
27. **Quais parâmetros são opcionais?** `action` e `content`.
28. **O que é `str | None`?** Uma string ou ausência de valor.
29. **O que significa `tuple[bool, str]`?** Status e texto associado.
30. **O que `with` faz ao sair?** Aciona o fechamento do arquivo.
31. **Ele fecha se `read()` falhar?** Sim.
32. **O que acontece com ação inválida?** Retorna falha sem abrir arquivo.
33. **O que grava quando `content=None`?** Uma string vazia.

### conceitos gerais

34. **Qual diferença entre `except` e `finally`?** Um trata exceção; o outro executa ao sair.
35. **O que é `Exception as e`?** Captura uma exceção comum na variável `e`.
36. **Para que serve `str(e)`?** Para obter o texto da falha.
37. **Qual diferença entre flake8 e mypy?** Um verifica estilo; outro verifica tipos.
38. **Por que testar efeitos reais?** Uma mensagem de sucesso não prova que os bytes foram salvos.
39. **O que o subject manda entregar?** Somente os quatro scripts pedidos.

## 15. Resumo de última hora

`open()` → file object; `read()` → `str`; `write()` → grava; `close()` → fecha; `"r"` → lê arquivo existente; `"w"` → escreve, cria ou trunca; `stdin` → entrada; `stdout` → saída normal; `stderr` → erros; `flush()` → força saída pendente; `with` → context manager no ex3; `try` → tenta; `except` → trata; `finally` → executa ao sair. Nos ex0–ex2, fechar manualmente. No ex3, `secure_archive()` devolve `(bool, str)`.

## 16. Status final da implementação

Validação executada após a troca das anotações, neste ambiente:

| Verificação | Resultado |
|---|---|
| `python3 --version` | Python 3.13.1; atende ao mínimo 3.10 |
| `python3 -m py_compile` nos quatro scripts | PASS |
| `flake8` nos quatro scripts | PASS, sem saída de erros |
| `mypy` nos quatro scripts | PASS: `Success: no issues found in 4 source files` |
| `Authorized` e `typing.Optional` | PASS: chamadas e imports revistos por exercício; `typing.Optional` ausente |
| Regra de `with` | PASS: nenhum nos ex0–ex2; dois blocos no ex3 |
| Testes funcionais | PASS: 52/52 verificações da bateria principal e 12/12 casos complementares, incluindo criação, bytes gravados, sobrescrita, falhas, EOF e fechamento |
| stdout/stderr do ex2 | PASS: saídas redirecionadas para arquivos separados e inspecionadas |
| `secure_archive()` | PASS: chamada direta para leitura, escrita, sobrescrita, conteúdo vazio, `None`, ação inválida e erros |

**Pendência de entrega:** o guia continua rastreado no Git, embora o subject peça apenas os quatro scripts. Ele deve sair do versionamento mantendo a cópia local; nenhuma alteração no índice foi autorizada nesta etapa. Os testes usaram arquivos temporários, sem acrescentar arquivos aos diretórios dos exercícios.

**Observação:** arquivos de origem com CRLF ou `\r` são normalizados para `\n` pelos ex1–ex2. Não há exigência explícita de preservar esses bytes no subject. A execução de demonstração do ex3 depende de `ancient_fragment.txt`, ausente na pasta; as chamadas diretas de `secure_archive()` foram testadas com arquivos temporários.
