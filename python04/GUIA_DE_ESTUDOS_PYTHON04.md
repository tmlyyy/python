# Python 04 — Guia de estudos: arquivos e streams

Este guia segue o subject **Data Archivist: Digital Preservation in the Cyber Archives**, versão 3.0, em `subjetcs/py04.subject (1).pdf`. Procurei uma régua de correção e instruções `AGENTS.md` no projeto e não encontrei. Os requisitos descritos aqui vêm do subject da lista 04.

## Regras comuns do subject

O projeto deve usar Python 3.10 ou posterior, respeitar flake8 e incluir type hints em todas as funções e métodos, conferidos com mypy. As funções devem lidar com exceções com cuidado. O subject permite os tipos e coleções padrão `str`, `int`, `float`, `list`, `dict`, `set` e `tuple`, com seus métodos e construtores.

Há uma regra de ordem: o `with` é introduzido no exercício 3 e não deve ser usado antes dele. As saídas dos exemplos servem de formato sugerido; o subject permite personalizar mensagens desde que a estrutura e as informações essenciais permaneçam. Os arquivos a entregar são os quatro scripts abaixo; o subject não pede arquivos de dados adicionais.

## Conceitos principais

`open()` abre um arquivo e devolve um objeto de arquivo, não o texto diretamente. O método `read()` lê seu conteúdo como texto. Depois de usar o arquivo, é necessário fechá-lo com `close()` nos três primeiros exercícios. No exercício 3, `with` fecha o arquivo automaticamente quando o bloco termina, inclusive quando ocorre uma exceção.

Arquivos podem ser abertos para leitura (`"r"`) ou escrita (`"w"`). O modo `"w"` cria o arquivo se necessário e substitui o conteúdo anterior se ele já existir. `write()` envia texto ao arquivo. Já `sys.stdin`, `sys.stdout` e `sys.stderr` são streams: entrada padrão, saída normal e saída de erro.

## Exercício 0 — Ancient Text Recovery

**Arquivo pedido:** `ex0/ft_ancient_text.py`<br>
**Autorizado:** `import sys`, `sys.argv`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.close()`, `print()`.

O programa recebe o nome do arquivo pela linha de comando, tenta abri-lo para leitura e exibe seu conteúdo como o comando `cat`, com cabeçalho e separadores. Se a quantidade de argumentos não for a esperada, exibe o formato de uso. Se a abertura ou a leitura falhar, mostra uma mensagem com a causa. Depois de uma leitura bem-sucedida, mostra que fechou o arquivo.

Este exercício ensina a relação entre `sys.argv`, a chamada de `open()` e o objeto retornado. Ele também apresenta o fechamento explícito de um recurso e o tratamento de falhas como arquivo inexistente ou sem permissão.

## Exercício 1 — Archive Creation

**Arquivo pedido:** `ex1/ft_archive_creation.py`<br>
**Autorizado:** `import sys`, `sys.argv`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.write()`, `io.close()`, `print()`, `input()`.

O exercício parte da leitura do anterior. Depois de exibir o texto, acrescenta `#` ao fim de cada linha, mostra a transformação e pergunta o nome do arquivo de destino. Uma resposta vazia significa que não deve salvar. Com um nome, abre o destino em modo `"w"`, grava o novo conteúdo e informa o resultado. Esse modo cria ou substitui o arquivo.

O código preserva linhas vazias, acrescentando `#` a elas também. Essa é a interpretação de “no fim de cada linha”; o exemplo do subject não inclui linhas vazias no conteúdo de origem.

Como o `with` ainda não pode ser usado, o arquivo é fechado explicitamente. Os blocos `finally` garantem uma tentativa de fechamento também nos caminhos de erro.

## Exercício 2 — Stream Management

**Arquivo pedido:** `ex2/ft_stream_management.py`<br>
**Autorizado:** `import sys`, `sys.argv`, `sys.stdin`, `sys.stdout`, `sys.stderr`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.readline()`, `io.write()`, `io.flush()`, `io.close()`, `print()`.

O exercício mantém a leitura e a transformação anteriores. A diferença central é o uso dos três streams padrão: mensagens de erro são enviadas a `sys.stderr` com o prefixo `[STDERR]`; o nome do arquivo de destino é solicitado escrevendo em `sys.stdout`; e a resposta é obtida com `sys.stdin.readline()` em vez de `input()`.

`flush()` força a exibição do prompt antes da leitura. `readline()` devolve também a quebra de linha digitada, que é removida antes de usar o nome como caminho. Se houver falha ao ler ou gravar, a mensagem vai para o stream de erro; o programa informa quando os dados não foram salvos.

## Exercício 3 — Vault Security

**Arquivo pedido:** `ex3/ft_vault_security.py`<br>
**Autorizado:** `open()`, `read()`, `write()`, `print()`.

O subject pede uma função `secure_archive()` que recebe obrigatoriamente um nome de arquivo, uma ação opcional (`read` ou `write`) e conteúdo opcional. Ela devolve uma tupla `(bool, str)`: o booleano indica sucesso e o texto contém o conteúdo lido, uma confirmação de gravação ou a mensagem de erro.

Aqui aparece o `with`. Para leitura, o bloco abre o arquivo, lê o conteúdo e fecha automaticamente. Para escrita, abre com `"w"`, grava e fecha automaticamente. Uma exceção é capturada e devolvida como `(False, mensagem)`. A ação padrão é leitura; uma ação desconhecida devolve uma falha explicativa.

Este é o primeiro exercício em que a estrutura do código será revisada para verificar o uso de `with`. A lista anterior introduziu tratamento de exceções; aqui a mesma ideia protege operações com arquivos. Tuplas, estudadas na lista 03, permitem devolver o indicador de sucesso e a mensagem juntos.

O exemplo de `main()` usa `ancient_fragment.txt` no diretório de execução. Esse arquivo de exemplo não está na pasta `python04`; para ver o caminho de sucesso, crie um arquivo temporário com esse nome ou teste a função diretamente. O programa agora não grava uma mensagem de erro como se fosse o conteúdo recuperado.

## Checklist por exercício

| Exercício | O que o subject pede | Situação conferida |
|---|---|---|
| 0 | Receber caminho, exibir conteúdo, tratar falhas e fechar arquivo | Atendido; testei arquivo válido, caminho ausente e uso sem argumento |
| 1 | Acrescentar `#` às linhas, exibir transformação, permitir não salvar ou gravar/substituir destino | Atendido; testei saída vazia, gravação e preservação de linha vazia |
| 2 | Enviar erros a stderr e ler resposta com streams, sem `input()` | Atendido; testei erro de leitura, cancelamento e erro de gravação |
| 3 | Implementar `secure_archive()` com tupla de resultado e `with` para ler/gravar | Atendido; testei sucesso, arquivo ausente, permissão negada e ação inválida |

O exemplo do subject usa `/etc/master.passwd` para demonstrar permissão negada. Esse caminho não existe neste ambiente Linux, então ele produz “arquivo inexistente” aqui. Para testar permissão negada sem alterar arquivos do sistema, usei `/proc/1/mem` em um diretório temporário.

## O que conseguir explicar na avaliação

O subject diz que podem pedir para demonstrar operações de arquivo, tratamento de erros e o funcionamento de `with`. Pratique explicar:

- que `open()` devolve um objeto de arquivo, enquanto `read()` devolve seu conteúdo;
- a diferença entre abrir com `"r"` e com `"w"`;
- por que fechar o arquivo é necessário nos exercícios 0–2;
- como `finally` ajuda a fechar um arquivo mesmo se uma operação falhar;
- a diferença entre `sys.stdin`, `sys.stdout` e `sys.stderr`;
- como `readline()` recebe uma linha e por que o nome precisa perder a quebra de linha;
- como `with` fecha o arquivo automaticamente ao sair do bloco;
- por que `secure_archive()` devolve uma tupla com status e mensagem.

## Perguntas de revisão

**O que `open()` retorna?**<br>
Um objeto de arquivo, que oferece métodos como `read()`, `write()` e `close()`.

**O que o modo `"w"` faz se o destino já existir?**<br>
Abre para escrita e substitui o conteúdo existente.

**Qual a diferença entre stdout e stderr?**<br>
São streams diferentes: stdout recebe a saída normal; stderr recebe mensagens de erro.

**Por que o exercício 2 não usa `input()`?**<br>
O requisito é ler usando `sys.stdin`; o prompt é enviado por `sys.stdout`.

**O que acontece quando a execução sai de um bloco `with open(...)`?**<br>
O arquivo é fechado automaticamente.

**Qual informação volta de `secure_archive()`?**<br>
Uma tupla com sucesso ou falha e o conteúdo, confirmação ou mensagem de erro.

## Verificações e comandos

O ambiente usado nesta revisão tem Python 3.14.4, acima do mínimo exigido. Flake8 e mypy estão instalados. Estes são os comandos executados:

```bash
python3 --version
python3 -m flake8 --isolated --jobs=1 python04
python3 -m mypy --strict --cache-dir=/tmp/python04-mypy python04
python3 -m compileall -q python04
```

Para executar os exemplos:

```bash
python3 python04/ex0/ft_ancient_text.py ancient_fragment.txt
python3 python04/ex1/ft_archive_creation.py ancient_fragment.txt
python3 python04/ex2/ft_stream_management.py ancient_fragment.txt
python3 python04/ex3/ft_vault_security.py
```

Os testes desta revisão foram feitos em diretórios temporários para não deixar arquivos de saída na pasta do projeto. Não há régua separada no workspace; por isso, o checklist usa os requisitos e exemplos do subject.
