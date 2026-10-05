# Python 02 — Exceções: guia de estudos

Este guia acompanha os exercícios `ex0` a `ex4` do subject **Garden Guardian**. O tema da lista é fazer programas continuarem funcionando quando recebem dados inválidos ou encontram uma falha.

## Ideia principal: exceções

Uma exceção é um aviso que Python gera quando não consegue executar uma operação normalmente. Por exemplo, `int("abc")` não consegue converter o texto para inteiro e gera `ValueError`.

O bloco `try` envolve uma operação que pode falhar. Um bloco `except` informa como tratar um tipo de falha. Quando a exceção é tratada, o programa pode continuar. `raise` gera uma exceção de propósito quando uma regra do programa não é atendida. `finally` executa sua parte sempre, tenha ocorrido uma exceção ou não.

As anotações como `temp_str: str` e `-> int` são *type hints*: documentam os tipos esperados e ajudam ferramentas como mypy a encontrar inconsistências. Elas não convertem valores durante a execução.

## Exercício 0 — `ex0/ft_first_exception.py`

**O que o subject quer ensinar:** converter uma leitura de temperatura e lidar com uma entrada que não pode ser convertida, sem encerrar o programa.

`input_temperature(temp_str: str) -> int` recebe um texto e devolve `int(temp_str)`. Para `"25"`, devolve o inteiro `25`; para `"abc"`, a conversão lança `ValueError`.

`test_temperature()` percorre as entradas `"25"` e `"abc"`. Em cada volta, imprime a entrada, tenta convertê-la e mostra a temperatura. Se surgir `ValueError`, imprime a mensagem da falha. O `try/except` fica dentro do laço para que o erro de uma entrada não impeça o teste seguinte.

`main()` imprime o título, chama os testes e confirma que o programa chegou ao fim. O bloco `if __name__ == "__main__":` chama `main()` quando este arquivo é executado diretamente.

## Exercício 1 — `ex1/ft_raise_exception.py`

**O que o subject quer ensinar:** além de verificar se o texto representa um número, validar uma regra do domínio: plantas aceitam temperaturas de 0 °C a 40 °C, inclusive.

`input_temperature()` converte o texto em inteiro. Se o resultado for maior que 40, `raise ValueError(...)` explica que está quente demais; se for menor que 0, lança uma mensagem indicando que está frio demais. Os limites são válidos porque as condições são `> 40` e `< 0`. Um texto inválido ainda gera o `ValueError` original de `int()`.

`test_temperature()` testa um valor válido, texto inválido e os dois extremos inválidos pedidos (`"100"` e `"-50"`). Um único `except ValueError` captura tanto falhas de conversão quanto as exceções levantadas pelas regras de temperatura.

## Exercício 2 — `ex2/ft_different_errors.py`

**O que o subject quer ensinar:** reconhecer que situações diferentes geram tipos diferentes de exceção e que um mesmo `try` pode ter vários `except`.

`garden_operations(operation_number)` seleciona uma operação pelo número: converter `"abc"` gera `ValueError`; dividir por zero gera `ZeroDivisionError`; abrir um caminho inexistente gera `FileNotFoundError`; concatenar texto e inteiro gera `TypeError`. Qualquer outro número não executa uma operação defeituosa e a função termina normalmente.

`test_error_types()` percorre as operações de 0 a 4. Dentro de um mesmo `try`, há um `except` para cada tipo de erro. Assim, a mensagem identifica o tipo sem usar `type()`, que o subject proíbe. O `# type: ignore[operator]` silencia o diagnóstico estático esperado do mypy, mas não impede o `TypeError` em execução. O subject explicitamente prevê esse diagnóstico: veja a revisão abaixo antes de decidir manter o comentário.

## Exercício 3 — `ex3/ft_custom_errors.py`

**O que o subject quer ensinar:** criar exceções próprias para representar problemas específicos e organizá-las por herança.

`GardenError` herda de `Exception` e representa um problema geral do jardim. `PlantError` e `WaterError` herdam de `GardenError`, então representam problemas mais específicos e também podem ser capturadas como erros gerais do jardim. Cada classe recebe uma mensagem padrão, usada caso nenhuma mensagem seja fornecida.

`test_plant_function()` e `test_water_function()` levantam exemplos desses erros. `test_custom_errors()` primeiro captura cada classe específica e depois captura ambas como `GardenError`. Isso demonstra a relação de herança na prática: capturar a classe base também captura instâncias de suas subclasses.

## Exercício 4 — `ex4/ft_finally_block.py`

**O que o subject quer ensinar:** garantir a limpeza de um recurso mesmo quando uma operação falha.

O exercício define `GardenError` e `PlantError` novamente porque cada arquivo é independente. `water_plant(plant_name: str) -> None` compara o nome com `plant_name.capitalize()`. Se forem diferentes, levanta `PlantError`; se forem iguais, imprime a confirmação de rega.

`test_watering_system(plants: list[str]) -> None` imprime que abriu o sistema, tenta regar cada planta e captura `PlantError`. Quando uma planta inválida aparece, mostra o erro, informa que está encerrando o teste e retorna. O bloco `finally` ainda imprime o fechamento do sistema, inclusive nesse caminho de retorno.

`main()` chama o sistema uma vez com nomes válidos e outra vez com uma planta inválida em minúsculas. A segunda execução demonstra que o fechamento acontece mesmo depois da falha.

## Como ler os tipos e a estrutura

- `str` significa texto; `int`, número inteiro; `list[str]`, lista de textos.
- `-> None` indica que a função não devolve um valor útil com `return`.
- `f"...{variavel}..."` é uma *f-string*: insere o valor da variável no texto.
- `for valor in ...` repete o bloco para cada elemento da sequência.
- `except ValueError as error` captura aquele erro e associa a instância à variável `error`, para que sua mensagem possa ser impressa.
- `super().__init__(message)` encaminha a mensagem para a classe de exceção base, que a disponibiliza em `str(error)`.

## O que revisar para a avaliação

Pratique explicar por que `int("abc")` falha, a diferença entre capturar `ValueError` e `PlantError`, como várias cláusulas `except` podem pertencer ao mesmo `try`, como `raise` aplica uma regra própria, por que uma exceção de uma subclasse também pode ser capturada pela classe base e por que `finally` executa mesmo quando a função retorna dentro do `except`.

Os exemplos deliberadamente provocam erros para ensinar o tratamento de exceções. O objetivo de “não travar” é que o programa demonstre esses casos, capture as falhas esperadas e conclua a execução.


---

# Revisão detalhada dos seus arquivos — 05/10/2026

Esta revisão usa o PDF **Garden Guardian, versão 3.0**, e os cinco arquivos Python enviados. As linhas abaixo correspondem exatamente aos arquivos originais, que não foram alterados. As explicações são pensadas para quem está começando em Python e já teve contato com C.

## 1. Resultado da conferência

| Exercício | Execução dos casos pedidos | Flake8 padrão | Mypy estrito | Resultado da leitura do subject |
| --- | --- | --- | --- | --- |
| ex0 | Terminou com código 0 | Sem apontamentos | Sem apontamentos | Cumpre conversão, captura e continuidade |
| ex1 | Terminou com código 0 | Sem apontamentos | Sem apontamentos | Cumpre validação de 0 a 40 inclusive e testes de extremos |
| ex2 | Terminou com código 0 | Sem apontamentos | Sem apontamentos com o comentário atual | Cumpre os quatro erros e vários handlers; revisar a supressão do erro intencional |
| ex3 | Terminou com código 0 | Sem apontamentos | Sem apontamentos | Cumpre herança, mensagens padrão e captura específica/geral |
| ex4 | Terminou com código 0 | Sem apontamentos | Sem apontamentos | Cumpre sucesso, falha, retorno imediato e fechamento no finally |

Ferramentas efetivamente executadas: Python 3.12.14, flake8 7.4.1 e mypy 2.4.0. O mypy foi configurado para a versão de linguagem 3.10. Isso verifica a tipagem nessa configuração; não significa que os programas foram executados em um interpretador 3.10.

Comandos usados para os checkers:

```bash
python3 -m flake8 --isolated upload/*.py
python3 -m mypy --strict --python-version 3.10 --no-incremental upload/*.py
```

O primeiro terminou com código 0 e nenhuma mensagem. O segundo retornou `Success: no issues found in 5 source files`. `--isolated` evita que configurações locais escondam avisos do flake8. `--strict` é uma verificação adicional: o PDF manda usar mypy, mas não exige explicitamente esse modo.

Também executei cada programa e verifiquei: importação sem executar main; limites 0 e 40 aceitos no ex1; -1, 41, abc e 25.5 rejeitados; operações fora de 0–3 retornando normalmente no ex2; mensagens padrão e personalizadas no ex3; interrupção antes de Carrots e um único fechamento no caso inválido do ex4.

### O que são as normas aqui?

O capítulo IV, página impressa 6 do PDF, exige Python 3.10+, flake8, type hints em todas as funções e métodos, uso de mypy, um arquivo por exercício, tratamento de erros e demonstrações de funcionamento normal e de falha.

PEP 8 é um guia de estilo. Flake8 automatiza parte da verificação de estilo, além de outras verificações; passar nele não prova toda recomendação possível da PEP 8. Mypy verifica tipos estaticamente; não testa se a lógica resolve o exercício. Executar os casos e ler o subject completam a análise.

Neste subject não existe proibição de `for`, nem regra de 25 linhas por função ou de 5 funções por arquivo. Essas regras de C/Norminette não devem ser transferidas automaticamente para esta lista Python. O código usa quatro espaços por nível de indentação, nomes de funções em snake_case, classes em PascalCase e separação adequada entre definições. Não foram encontrados problemas de estilo pelo flake8 padrão, incluindo seu limite padrão de 79 caracteres para linhas de código.

Os diretórios pedidos são `ex0/`, `ex1/`, `ex2/`, `ex3/` e `ex4/`. Os nomes enviados estão corretos, mas os anexos não comprovam a organização do seu repositório. Confirme essas pastas antes da entrega e entregue apenas os arquivos pedidos; este guia é material de estudo.

Não foi fornecida uma rubrica interna adicional da 42 SP. Portanto, esta é uma verificação contra o PDF e as ferramentas indicadas, não uma garantia de aprovação nem de regras locais que não aparecem no material.

### Funções autorizadas

| Exercício | Autorizadas no PDF | Uso encontrado |
| --- | --- | --- |
| ex0 | int(), print() | Conversão e impressão |
| ex1 | int(), print() | Conversão, impressão e ValueError |
| ex2 | print(), open(), int() | Essas três; não usa type() |
| ex3 | print() | Impressão e construção das exceções próprias |
| ex4 | print(), str.capitalize() | Impressão, capitalize e construção de PlantError |

`try`, `except`, `finally`, `raise`, `if`, `for` e `return` são construções da linguagem, não chamadas a funções extras. O PDF libera os tipos de exceção necessários. As classes próprias usam `super().__init__()` para inicializar corretamente a mensagem herdada: é o mecanismo usual para cumprir a exigência das exceções com mensagens padrão. Como `super()` não está literalmente na pequena lista do ex3/ex4, essa leitura é uma interpretação coerente com o exercício, não uma confirmação de uma regra interna adicional do campus. Se a avaliação local tiver uma interpretação específica dessa lista, confira-a com o avaliador.

### Ponto principal para revisar: ex2, linha 12

Seu código tem:

```python
"string" + 5  # type: ignore[operator]
```

O comentário manda o mypy ignorar o erro de operador nessa linha. Python ignora o comentário e continua gerando TypeError na execução. Logo, passar no mypy com esse comentário não demonstra que a soma está correta.

Na página impressa 13, o PDF diz que o mypy vai mostrar um erro para esse código defeituoso e que é necessário manter o erro propositalmente. Ele não declara expressamente que comentários de supressão são proibidos, mas a forma mais fiel à demonstração é deixar visível o diagnóstico:

```python
"string" + 5
```

Testei uma cópia temporária sem a supressão. O resultado foi exatamente um erro na linha 12:

```text
error: Unsupported operand types for + ("str" and "int")  [operator]
Found 1 error in 1 file
```

Essa é a exceção prevista pelo próprio subject ao resultado limpo do mypy. A recomendação é remover somente esse comentário e saber justificar o diagnóstico na avaliação. O original foi preservado para você estudar e decidir a mudança.

## 2. Vocabulário para ler qualquer um dos arquivos

- `def` define uma função. O corpo dela só executa quando alguém a chama; definir não é chamar.
- `:` no fim de `def`, `if`, `for`, `try`, `except`, `finally` ou `class` inicia um bloco. A indentação mostra quais linhas pertencem a esse bloco; em Python ela tem significado.
- `=` atribui um valor. `==` compara igualdade. `!=` compara diferença.
- `str` é texto, `int` é inteiro e `list[str]` significa lista cujos elementos esperados são textos.
- `temp_str: str` anota o tipo do parâmetro. `-> int` anota o retorno. As anotações não convertem dados nem bloqueiam automaticamente chamadas erradas em execução.
- `-> None` indica ausência de um resultado útil. Uma função que chega ao fim sem return devolve None; `return` sozinho também devolve None.
- Uma função que lança uma exceção pode não retornar normalmente. `-> int` não promete que uma chamada com entrada inválida vai produzir um inteiro.
- `f"...{valor}..."` insere o valor na mensagem. Não muda o valor original.
- `\n` dentro de uma string imprime uma quebra de linha. Isso é diferente de deixar uma linha vazia no código-fonte.
- `for item in sequencia` percorre diretamente os elementos. Listas usam colchetes; tuplas podem usar parênteses e vírgulas. Nenhuma dessas duas formas precisa de range() nestes arquivos.
- `except ... as error` guarda temporariamente o objeto de exceção em uma variável; o nome pode ser error ou e. O nome da variável não muda o tipo capturado.
- `#!/usr/bin/env python3` é o shebang: ajuda a escolher o interpretador ao executar o arquivo diretamente em sistemas compatíveis. Ao usar `python3 arquivo.py`, o comando já escolheu o interpretador. O shebang não faz parte da lógica do exercício.
- `__name__` vale `"__main__"` quando o arquivo é executado diretamente. Na importação ele recebe o nome do módulo; por isso o guard evita iniciar os testes ao importar.
- Linhas vazias separam visualmente partes do arquivo; não executam ações. Duas linhas vazias entre definições no nível do módulo são parte do estilo usual da PEP 8.

## 3. Como a exceção viaja entre funções

No ex0, `main()` chama `test_temperature()`, que chama `input_temperature()`, que chama `int()`. Se `int("abc")` falha, ele não devolve um inteiro: gera ValueError. A exceção sai de input_temperature e chega ao try da função de teste. O except correspondente imprime a mensagem, e o laço continua.

Quando uma linha dentro do try falha, as próximas linhas desse try são puladas. O programa procura o primeiro except compatível. Ele executa apenas esse handler para aquela ocorrência. Se não encontrar um, a exceção sobe para quem chamou a função; se ninguém a tratar, o programa normalmente termina com traceback.

Por isso não é necessário colocar try/except dentro de todas as funções. Algumas funções produzem ou propagam a falha, e a função de demonstração a trata. “Os programas não devem travar” se aplica à demonstração controlada; não significa esconder qualquer erro com `except Exception` em todo lugar.

`raise` produz uma falha; `except` trata uma falha. `finally` faz a limpeza tanto no sucesso quanto na falha. Ele não substitui o except e não torna uma exceção automaticamente tratada.

## 4. Exercício 0 — ft_first_exception.py: linha por linha

A tabela inclui todas as linhas. As linhas vazias são agrupadas por terem a mesma função visual.

| Linha | Código | O que faz |
| --- | --- | --- |
| 1 | `#!/usr/bin/env python3` | Shebang: indica Python 3 para execução direta em um sistema compatível. |
| 2, 3 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 4 | `def input_temperature(temp_str: str) -> int:` | Define input_temperature. temp_str é o texto recebido; o resultado normal esperado é um inteiro. |
| 5 | `return int(temp_str)` | Tenta converter o texto e devolve o inteiro. Com abc, int levanta ValueError e o return não se completa. |
| 6, 7 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 8 | `def test_temperature() -> None:` | Define a função de demonstração sem parâmetros e sem resultado útil. |
| 9 | `for temp_str in ("25", "abc"):` | Percorre uma tupla: primeiro o texto 25, depois abc. temp_str recebe um elemento a cada volta. |
| 10 | `print(f"Input data is '{temp_str}'")` | Mostra o texto recebido. As aspas simples na mensagem apenas ajudam a indicar que é texto. |
| 11 | `try:` | Inicia o bloco onde a conversão pode falhar. |
| 12 | `temperature = input_temperature(temp_str)` | Chama input_temperature e guarda seu retorno em temperature. Na falha, a atribuição não se completa. |
| 13 | `print(f"Temperature is now {temperature}°C")` | Mostra o número e a unidade. Só executa quando a chamada da linha 12 retorna normalmente. |
| 14 | `except ValueError as error:` | Captura ValueError levantado dentro do try, inclusive dentro da função chamada, e o associa a error. |
| 15 | `print(f"Caught input_temperature error: {error}")` | Imprime a mensagem do objeto capturado, sem encerrar o programa. |
| 16, 17 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 18 | `def main() -> None:` | Define main, a função que organiza a execução deste arquivo. |
| 19 | `print("=== Garden Temperature ===")` | Imprime o título da demonstração. |
| 20 | `test_temperature()` | Chama a função de teste: o corpo dela começa a executar aqui. |
| 21 | `print("All tests completed - program didn't crash!")` | Mostra que a chamada de teste terminou e main continuou mesmo após abc. |
| 22, 23 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 24 | `if __name__ == "__main__":` | Verifica se este arquivo foi executado diretamente, em vez de importado. |
| 25 | `main()` | Chama main somente nesse caso. |


**Conceitos do subject:** conversão de string para inteiro; ValueError; propagação de exceções; captura; continuidade após a falha.

**Rastreio:** com 25, a linha 12 recebe o inteiro e a linha 13 imprime sucesso. Com abc, a linha 5 falha; a execução volta ao handler da linha 14; a linha 13 é pulada. Depois o laço acaba e main imprime a confirmação.

**Para a defesa:** explique por que não há except dentro de input_temperature: quem chama é responsável por tratar a falha neste desenho. Capturar ValueError é apropriado para os textos do exercício. Uma chamada fora do contrato, como int(None), pode gerar TypeError; o subject pede uma string, e type hints não garantem isso em execução.

## 5. Exercício 1 — ft_raise_exception.py: linha por linha

A tabela inclui todas as linhas. As linhas vazias são agrupadas por terem a mesma função visual.

| Linha | Código | O que faz |
| --- | --- | --- |
| 1 | `#!/usr/bin/env python3` | Shebang: indica Python 3 para execução direta em um sistema compatível. |
| 2, 3 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 4 | `def input_temperature(temp_str: str) -> int:` | Define a conversão com validação. O parâmetro é texto e o retorno normal é inteiro. |
| 5 | `temp = int(temp_str)` | Converte e guarda o número em temp. abc falha aqui, antes das comparações. |
| 6 | `if temp > 40:` | Pergunta se o número é maior que 40. O próprio 40 não entra no bloco. |
| 7 | `raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")` | Gera ValueError com a mensagem de calor. A execução desta chamada para e a exceção sobe até o handler. |
| 8 | `if temp < 0:` | Se não houve exceção anterior, pergunta se o número é menor que 0. O próprio 0 não entra no bloco. |
| 9 | `raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")` | Gera ValueError com a mensagem de frio. O return da linha 10 não será executado nesta chamada. |
| 10 | `return temp` | Devolve temp apenas depois de converter e passar nas duas validações. |
| 11, 12 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 13 | `def test_temperature() -> None:` | Define a demonstração, sem retorno útil. |
| 14 | `test_cases = ["25", "abc", "100", "-50"]` | Cria uma lista de quatro textos: número válido, texto inválido, calor extremo e frio extremo. |
| 15 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 16 | `for temp_str in test_cases:` | Percorre essa lista. Cada entrada será tratada em sua própria tentativa. |
| 17 | `print(f"Input data is '{temp_str}'")` | Mostra qual entrada está sendo testada. |
| 18 | `try:` | Inicia a tentativa que pode falhar. |
| 19 | `temperature = input_temperature(temp_str)` | Chama a função de validação e guarda o inteiro se ela tiver sucesso. |
| 20 | `print(f"Temperature is now {temperature}°C")` | Imprime a temperatura válida. É pulada se a linha anterior lançar uma exceção. |
| 21 | `except ValueError as error:` | Captura ValueError tanto da conversão int quanto dos raise escritos por você. |
| 22 | `print(f"Caught input_temperature error: {error}")` | Imprime a mensagem correspondente. Depois o laço passa à próxima entrada. |
| 23, 24 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 25 | `def main() -> None:` | Define main como organizadora do programa. |
| 26 | `print("=== Garden Temperature Checker ===")` | Imprime o título. |
| 27 | `test_temperature()` | Executa os quatro testes. |
| 28 | `print("All tests completed - program didn't crash!")` | Confirma que o fluxo chegou ao fim da demonstração. |
| 29, 30 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 31 | `if __name__ == "__main__":` | Protege a execução principal durante importações. |
| 32 | `main()` | Inicia main quando o arquivo é executado diretamente. |


**Conceitos do subject:** validação de formato versus validação de domínio; limites inclusivos; raise; mensagem útil; reaproveitamento da captura de ValueError.

| Entrada | Conversão | Validação de intervalo | Resultado |
| --- | --- | --- | --- |
| 25 | 25 | Aceita | Devolve 25 |
| abc | Falha | Não é executada | ValueError de int |
| 100 | 100 | Maior que 40 | ValueError de calor |
| -50 | -50 | Menor que 0 | ValueError de frio |
| 0 | 0 | Aceita | Devolve 0 |
| 40 | 40 | Aceita | Devolve 40 |

**Para a defesa:** um número pode ter formato válido e ser inválido para a planta. O intervalo inclui 0 e 40 porque você usou < e >, e não <= e >=. Dois if funcionam aqui: depois de raise, a chamada não continua para o segundo if. Não é obrigatório trocar por elif.

Testar 0 e 40 na demonstração é uma melhoria opcional; esses limites já foram verificados na revisão. int não aceita o texto 25.5 como inteiro: ele gera ValueError, coerente com a exigência de retorno inteiro.

## 6. Exercício 2 — ft_different_errors.py: linha por linha

A tabela inclui todas as linhas. As linhas vazias são agrupadas por terem a mesma função visual.

| Linha | Código | O que faz |
| --- | --- | --- |
| 1 | `#!/usr/bin/env python3` | Shebang: indica Python 3 para execução direta em um sistema compatível. |
| 2, 3 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 4 | `def garden_operations(operation_number: int) -> None:` | Define a função que escolhe uma operação por um inteiro. Ela não devolve resultado útil. |
| 5 | `if operation_number == 0:` | Seleciona a operação zero. |
| 6 | `int("abc")` | Tenta converter abc para inteiro e gera ValueError. O erro é proposital. |
| 7 | `elif operation_number == 1:` | Se não escolheu zero, verifica se a operação é um. elif significa uma alternativa na mesma seleção. |
| 8 | `1 / 0` | Tenta dividir 1 por 0 e gera ZeroDivisionError. Não é necessário guardar o resultado para a operação falhar. |
| 9 | `elif operation_number == 2:` | Seleciona a operação dois. |
| 10 | `open("/non/existent/file", "r")` | Tenta abrir o caminho inexistente em modo de leitura r. Como a abertura falha, não há arquivo aberto para fechar. |
| 11 | `elif operation_number == 3:` | Seleciona a operação três. |
| 12 | `"string" + 5  # type: ignore[operator]` | Tenta concatenar string com o inteiro 5: gera TypeError. O comentário silencia apenas o diagnóstico operator do mypy; não corrige a operação. |
| 13, 14 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 15 | `def test_error_types() -> None:` | Define a função que testa os tipos de erro. |
| 16 | `for op in (0, 1, 2, 3, 4):` | Percorre as operações 0, 1, 2, 3 e 4. A última demonstra funcionamento sem erro. |
| 17 | `print(f"Testing operation {op}...")` | Imprime o número da tentativa atual. |
| 18 | `try:` | Inicia um único try com quatro alternativas de captura abaixo. |
| 19 | `garden_operations(op)` | Chama garden_operations. A exceção daquela operação sai da função e chega aos handlers deste try. |
| 20 | `print("Operation completed successfully")` | Imprime sucesso apenas quando a chamada termina normalmente, como na operação 4. |
| 21 | `except ValueError as error:` | Captura falha de valor inválido. |
| 22 | `print(f"Caught ValueError: {error}")` | Imprime seu tipo e a mensagem original. |
| 23 | `except ZeroDivisionError as error:` | Captura divisão por zero, se esse foi o erro que ocorreu. |
| 24 | `print(f"Caught ZeroDivisionError: {error}")` | Imprime a mensagem de divisão por zero. |
| 25 | `except FileNotFoundError as error:` | Captura falha de arquivo inexistente. |
| 26 | `print(f"Caught FileNotFoundError: {error}")` | Imprime a mensagem do sistema sobre o caminho. |
| 27 | `except TypeError as error:` | Captura operação entre tipos incompatíveis. |
| 28 | `print(f"Caught TypeError: {error}")` | Imprime a mensagem do TypeError. Depois deste handler, o laço segue para a próxima operação. |
| 29, 30 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 31 | `def main() -> None:` | Define main. |
| 32 | `print("=== Garden Error Types Demo ===")` | Imprime o título. |
| 33 | `test_error_types()` | Executa as cinco operações da demonstração. |
| 34 | `print("All error types tested successfully!")` | Imprime a confirmação final após os erros terem sido tratados. |
| 35, 36 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 37 | `if __name__ == "__main__":` | Verifica execução direta do arquivo. |
| 38 | `main()` | Chama main nesse caso. |


**Conceitos do subject:** categorias de exceção; escolha de handlers; operação normal; múltiplas capturas associadas ao mesmo try; erro estático versus erro em execução.

Seu try com quatro except já mostra como capturar diferentes tipos com um único try. O PDF não exige explicitamente escrever uma tupla de exceções. Para estudar outra forma, também existe:

```python
try:
    garden_operations(0)
except (ValueError, TypeError) as error:
    print(f"Caught input error: {error}")
```

Esse handler compartilha o mesmo tratamento entre dois tipos. Com os quatro handlers do seu arquivo, as mensagens podem ser específicas. Nenhuma das formas precisa usar type(). Um único disparo de erro executa apenas um handler compatível, não todos.

Com operation_number igual a 4, -1 ou 99, nenhuma condição é atendida. A função chega ao fim e retorna None implicitamente, cumprindo o retorno sem código defeituoso. A mensagem de sucesso aparece porque nenhuma exceção ocorreu.

O caminho /non/existent/file foi confirmado inexistente neste ambiente. A demonstração depende de ele continuar inexistente. Como open falha, nenhum objeto de arquivo é obtido; não é preciso fechá-lo nesse caminho de falha. Isso não significa que arquivos abertos com sucesso nunca precisem ser fechados.

**Para a defesa:** ValueError é um valor inadequado para uma operação, como abc para int; TypeError é uma incompatibilidade de tipos, como somar str e int. str(5) produziria texto, mas “consertar” a soma eliminaria justamente a falha que este exercício manda demonstrar.

## 7. Exercício 3 — ft_custom_errors.py: linha por linha

A tabela inclui todas as linhas. As linhas vazias são agrupadas por terem a mesma função visual.

| Linha | Código | O que faz |
| --- | --- | --- |
| 1 | `#!/usr/bin/env python3` | Shebang: indica Python 3 para execução direta em um sistema compatível. |
| 2, 3 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 4 | `class GardenError(Exception):` | Cria GardenError como subclasse de Exception. Instâncias dessa classe podem ser levantadas com raise. |
| 5 | `def __init__(self, message: str = "Unknown garden error") -> None:` | Define o inicializador. self é a instância criada; message é texto opcional, com valor padrão. O inicializador não devolve resultado útil. |
| 6 | `super().__init__(message)` | Chama o inicializador da classe pai, Exception, e entrega a mensagem para o mecanismo normal de exceções. |
| 7, 8 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 9 | `class PlantError(GardenError):` | Cria PlantError como subclasse de GardenError: um erro de planta também é um erro de jardim. |
| 10 | `def __init__(self, message: str = "Unknown plant error") -> None:` | Define seu inicializador com uma mensagem padrão específica para plantas. |
| 11 | `super().__init__(message)` | Passa a mensagem para GardenError.__init__, que a encaminha a Exception.__init__. Não chama a si mesmo. |
| 12, 13 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 14 | `class WaterError(GardenError):` | Cria WaterError como outra subclasse de GardenError. WaterError e PlantError são classes irmãs. |
| 15 | `def __init__(self, message: str = "Unknown water error") -> None:` | Define seu inicializador com a mensagem padrão de água. |
| 16 | `super().__init__(message)` | Encaminha a mensagem ao inicializador da classe pai. |
| 17, 18 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 19 | `def test_plant_function() -> None:` | Define uma função de exemplo que vai falhar com um problema de planta. |
| 20 | `raise PlantError("The tomato plant is wilting!")` | Cria uma PlantError com mensagem personalizada e a levanta. Nenhum retorno normal acontece nessa chamada. |
| 21, 22 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 23 | `def test_water_function() -> None:` | Define outra função de exemplo, para problemas de água. |
| 24 | `raise WaterError("Not enough water in the tank!")` | Levanta WaterError com uma mensagem personalizada. |
| 25, 26 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 27 | `def test_custom_errors() -> None:` | Define a função que demonstra capturas específicas e gerais. |
| 28 | `print("Testing PlantError...")` | Anuncia o teste de PlantError. |
| 29 | `try:` | Inicia o primeiro try. |
| 30 | `test_plant_function()` | Chama a função que levanta PlantError. |
| 31 | `except PlantError as e:` | Captura esse tipo específico e guarda o objeto em e. |
| 32 | `print(f"Caught PlantError: {e}")` | Imprime a mensagem do objeto de erro. |
| 33 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 34 | `print("\nTesting WaterError...")` | Imprime uma quebra de linha e anuncia WaterError. |
| 35 | `try:` | Inicia um novo try, independente do primeiro. |
| 36 | `test_water_function()` | Chama a função que levanta WaterError. |
| 37 | `except WaterError as e:` | Captura o erro de água especificamente. |
| 38 | `print(f"Caught WaterError: {e}")` | Imprime a mensagem do erro de água. |
| 39 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 40 | `print("\nTesting catching all garden errors...")` | Anuncia que agora vai capturar pela classe geral GardenError. |
| 41 | `try:` | Inicia a tentativa de planta com captura geral. |
| 42 | `test_plant_function()` | Levanta PlantError por meio da função chamada. |
| 43 | `except GardenError as e:` | Captura GardenError; como PlantError herda dela, esse handler também aceita a falha de planta. |
| 44 | `print(f"Caught GardenError: {e}")` | Mostra a mensagem da PlantError capturada pelo handler geral. O objeto não foi convertido em GardenError. |
| 45 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 46 | `try:` | Inicia uma tentativa separada para água. |
| 47 | `test_water_function()` | Levanta WaterError por meio da função chamada. |
| 48 | `except GardenError as e:` | Captura a classe base; ela também aceita a subclasse WaterError. |
| 49 | `print(f"Caught GardenError: {e}")` | Mostra a mensagem do erro de água capturado pela classe geral. |
| 50, 51 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 52 | `def main() -> None:` | Define main. |
| 53 | `print("=== Custom Garden Errors Demo ===")` | Imprime o título. |
| 54 | `test_custom_errors()` | Executa todas as demonstrações de captura. |
| 55 | `print("All custom error types work correctly!")` | Imprime a confirmação final. |
| 56, 57 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 58 | `if __name__ == "__main__":` | Verifica execução direta. |
| 59 | `main()` | Inicia main somente na execução direta. |


**Conceitos do subject:** classes; instâncias; herança; exceções próprias; inicializador; self; super; argumento padrão; captura específica e pela classe base.

Uma classe descreve um tipo. PlantError é a classe; PlantError("mensagem") cria um objeto desse tipo. raise lança esse objeto. self, dentro do método, representa a instância que está sendo inicializada; você não precisa passá-lo explicitamente ao criar o objeto.

__init__ inicializa o objeto; tecnicamente ele não é o método que aloca/cria a instância. super permite chamar a implementação herdada sem escrever diretamente o nome da classe pai. Aqui a cadeia de inicialização termina em Exception, que guarda a mensagem nos argumentos da exceção; ao imprimir o objeto, a mensagem aparece.

| Construção | Mensagem resultante |
| --- | --- |
| GardenError() | Unknown garden error |
| PlantError() | Unknown plant error |
| WaterError() | Unknown water error |
| PlantError("The tomato plant is wilting!") | The tomato plant is wilting! |

Essas mensagens padrão foram testadas, embora a demonstração principal só use mensagens personalizadas. Usar o padrão é uma melhoria opcional para tornar a exigência mais visível durante a defesa.

GardenError captura PlantError e WaterError porque são subclasses dela. PlantError não captura WaterError, pois nenhuma herda da outra. Capturar pela classe base não muda o tipo original do objeto.

Se houver um handler específico e outro geral para o mesmo try, coloque o específico primeiro. Caso GardenError venha antes de PlantError, ele já captura o erro de planta e o handler mais específico não será escolhido.

**Para a defesa:** crie erros próprios quando o chamador precisa distinguir uma regra do seu domínio de falhas genéricas. Aqui “problema com planta” e “problema com água” são categorias compreensíveis; não é preciso inventar novas classes para qualquer ValueError comum.

## 8. Exercício 4 — ft_finally_block.py: linha por linha

A tabela inclui todas as linhas. As linhas vazias são agrupadas por terem a mesma função visual.

| Linha | Código | O que faz |
| --- | --- | --- |
| 1 | `#!/usr/bin/env python3` | Shebang: indica Python 3 para execução direta em um sistema compatível. |
| 2, 3 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 4 | `class GardenError(Exception):` | Define a classe base de erros de jardim neste arquivo, herdando de Exception. |
| 5 | `def __init__(self, message: str = "Unknown garden error") -> None:` | Define o inicializador com self, mensagem opcional e retorno None. |
| 6 | `super().__init__(message)` | Inicializa a parte herdada da exceção com a mensagem recebida. |
| 7, 8 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 9 | `class PlantError(GardenError):` | Define PlantError como subclasse de GardenError neste arquivo. |
| 10 | `def __init__(self, message: str = "Unknown plant error") -> None:` | Define a mensagem padrão específica para plantas. |
| 11 | `super().__init__(message)` | Encaminha a mensagem ao inicializador da classe base. |
| 12, 13 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 14 | `def water_plant(plant_name: str) -> None:` | Define a função que recebe o nome de uma planta como texto e não devolve resultado útil. |
| 15 | `if plant_name != plant_name.capitalize():` | Compara o nome original com uma nova string produzida por capitalize. Não altera plant_name. Se forem diferentes, o nome falha na regra. |
| 16 | `raise PlantError(f"Invalid plant name to water: '{plant_name}'")` | Levanta PlantError com o nome inválido entre aspas. A linha seguinte será pulada nesta chamada. |
| 17 | `print(f"Watering {plant_name}: [OK]")` | Imprime a confirmação de rega somente se a validação passou. |
| 18, 19 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 20 | `def test_watering_system(plants: list[str]) -> None:` | Define o teste que recebe uma lista de nomes de plantas. list[str] anota o tipo esperado dos elementos. |
| 21 | `print("Opening watering system")` | Simula a abertura do sistema por uma mensagem; não abre um recurso real. |
| 22 | `try:` | Inicia a tentativa de regar a lista inteira. |
| 23 | `for plant in plants:` | Percorre os nomes recebidos. O laço inteiro está dentro do try. |
| 24 | `water_plant(plant)` | Chama water_plant para o nome atual. Se falhar, abandona o laço e vai ao except. |
| 25 | `except PlantError as e:` | Captura PlantError levantada dentro da chamada e a associa a e. |
| 26 | `print(f"Caught PlantError: {e}")` | Imprime a falha da planta. |
| 27 | `print(".. ending tests and returning to main")` | Informa que o teste está terminando e voltará para main. |
| 28 | `return` | Solicita saída desta função, devolvendo None. Antes de sair, o finally ainda precisa executar. |
| 29 | `finally:` | Inicia o bloco de limpeza, que executa no sucesso e na falha, inclusive antes do return pendente. |
| 30 | `print("Closing watering system")` | Simula o fechamento do sistema. O fechamento acontece uma vez por chamada de teste. |
| 31, 32 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 33 | `def main() -> None:` | Define main. |
| 34 | `print("=== Garden Watering System ===")` | Imprime o título. |
| 35 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 36 | `print("\nTesting valid plants...")` | Imprime uma quebra de linha e anuncia a lista válida. |
| 37 | `valid_plants = ["Tomato", "Lettuce", "Carrots"]` | Cria a lista de três nomes que coincidem com o resultado de capitalize. |
| 38 | `test_watering_system(valid_plants)` | Executa a primeira chamada de teste: as três plantas são regadas e o sistema é fechado. |
| 39 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 40 | `print("\nTesting invalid plants...")` | Anuncia a lista que contém um nome inválido. |
| 41 | `invalid_plants = ["Tomato", "lettuce", "Carrots"]` | Cria uma lista em que lettuce falha na regra. Carrots vem depois dela para demonstrar a interrupção. |
| 42 | `test_watering_system(invalid_plants)` | Executa a segunda chamada: rega Tomato, falha em lettuce, fecha o sistema e retorna. Carrots não é regada. |
| 43 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 44 | `print("Cleanup always happens, even with errors!")` | Imprime a confirmação após o retorno da segunda chamada. return na função de teste não encerrou main. |
| 45, 46 | Linha vazia | Separa visualmente os blocos; não executa nenhuma instrução. |
| 47 | `if __name__ == "__main__":` | Verifica se o arquivo está sendo executado diretamente. |
| 48 | `main()` | Chama main nesse caso. |


**Conceitos do subject:** limpeza de recursos; try/except/finally; propagação; interrupção de sequência; retorno; regra de capitalização.

capitalize devolve uma nova string com o primeiro caractere capitalizado e o restante em minúsculas. Não transforma apenas a primeira letra mantendo todo o restante igual. Por isso Tomato passa, lettuce falha e TOMATO também falha: o resultado de capitalize para TOMATO é Tomato.

| Nome | Resultado de capitalize | Comparação do seu código |
| --- | --- | --- |
| Tomato | Tomato | Aceita |
| lettuce | Lettuce | PlantError |
| TOMATO | Tomato | PlantError |
| String vazia | String vazia | Aceita |
| 123 | 123 | Aceita |

Os dois últimos casos são uma limitação da regra por igualdade: não provam que existe um nome de planta com inicial maiúscula. O subject usa nomes de plantas e autoriza capitalize; não estabelece validação adicional para vazios ou números. Registre essa limitação e não acrescente funções fora da lista sem necessidade.

**Caso válido:** abre → rega Tomato → rega Lettuce → rega Carrots → finally fecha → retorna normalmente.

**Caso inválido:** abre → rega Tomato → lettuce gera PlantError → sai do laço → except imprime o erro → return fica pendente → finally fecha → retorno para main → main imprime a mensagem final. Carrots é pulada. O try está fora do laço justamente para interromper o conjunto no primeiro erro. No ex0, ele está dentro do laço para tratar cada entrada e continuar.

return termina somente test_watering_system, não o programa inteiro. finally executa antes de concretizar esse retorno. Evite colocar return no finally: isso pode substituir retornos anteriores e até suprimir uma exceção, escondendo a falha.

“Sempre” descreve o fluxo normal do Python, incluindo exceções e retornos; não é promessa de executar limpeza se o processo for morto à força ou a máquina desligar. Aqui abrir e fechar são apenas prints. Em um sistema real, a mesma estrutura poderia liberar um arquivo, conexão ou dispositivo.

As classes GardenError e PlantError foram definidas novamente para este arquivo ser independente. Isso mantém a mesma hierarquia e comportamento, mas as classes definidas em dois módulos são objetos diferentes: uma PlantError criada no ex3 não é automaticamente a PlantError do ex4. Para os testes autônomos deste subject, isso não provoca um problema. O enunciado pede usar sua PlantError anterior; a redefinição reproduz sua implementação, mas não representa importação da mesma classe. Confirme eventual exigência de compartilhamento se houver rubrica adicional; o PDF não lista aqui um arquivo extra a entregar.

## 9. Perguntas para praticar antes da avaliação

Tente responder em voz alta antes de consultar a resposta curta.

| Pergunta | Resposta que você precisa conseguir explicar |
| --- | --- |
| Por que int("abc") falha? | O texto não representa um inteiro válido; a conversão levanta ValueError. |
| O que acontece com as linhas depois da falha dentro do try? | São puladas nessa tentativa; o fluxo busca um handler compatível. |
| Por que o ex0 continua após abc? | O ValueError é tratado no teste; ele não fica sem handler. |
| O que raise faz que print não faz? | Interrompe o fluxo normal e gera uma exceção; print só exibe uma mensagem. |
| Por que 40 e 0 são válidos no ex1? | As rejeições usam > 40 e < 0, deixando os limites incluídos. |
| Quantos except rodam para uma única exceção? | Só o primeiro compatível. |
| Qual a diferença entre vários except e uma tupla no except? | Vários permitem tratamentos separados; a tupla compartilha um handler. |
| Type hints convertem ou impedem automaticamente entradas erradas? | Não; são anotações usadas pelo verificador estático e pelo leitor. |
| Por que mypy pode reclamar de um programa que trata TypeError? | A operação é estaticamente incompatível, mesmo que a falha de execução seja capturada. |
| O que type: ignore muda em execução? | Nada; só silencia um diagnóstico do checker. |
| Por que GardenError captura WaterError? | WaterError é uma subclasse dela. |
| Para que servem self e super? | self representa a instância; super permite chamar a implementação herdada. |
| Quando a mensagem padrão é usada? | Quando você não fornece o argumento message. |
| Por que Carrots não é regada depois de lettuce? | A exceção sai do laço; o handler solicita retorno imediato da função. |
| Por que o finally roda apesar do return? | Python executa o bloco de limpeza antes de concluir a saída da função. |
| finally trata a exceção? | Não por si só; ele executa a limpeza. except faz a captura. |
| Por que main não roda ao importar? | O guard __name__ não é verdadeiro para uma importação normal. |

## 10. Como repetir a verificação no seu repositório

Com as pastas do subject organizadas, execute:

```bash
python3 --version
python3 -m flake8 ex0/ ex1/ ex2/ ex3/ ex4/
python3 -m mypy --strict --python-version 3.10 ex0/ ex1/ ex2/ ex3/ ex4/
python3 ex0/ft_first_exception.py
python3 ex1/ft_raise_exception.py
python3 ex2/ft_different_errors.py
python3 ex3/ft_custom_errors.py
python3 ex4/ft_finally_block.py
```

Se as ferramentas não estiverem instaladas, use um ambiente virtual para instalá-las:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install flake8 mypy
```

Não é necessário entregar esse ambiente. Se você remover a supressão no ex2, espere o único diagnóstico operator intencional. Qualquer diagnóstico adicional precisa ser investigado; não ignore o arquivo inteiro para fazer o comando passar.

Melhorias opcionais de demonstração: incluir 0 e 40 no ex1; mostrar uma construção sem mensagem para cada exceção do ex3; adicionar separação visual nas saídas. Os exemplos do PDF têm algumas linhas vazias a mais, mas o texto fornecido não exige comparação de saída byte a byte. As mensagens essenciais e os fluxos estão presentes.

Recomendação principal: estude a linha 12 do ex2 sem a supressão para ver o diagnóstico esperado. Não identifiquei outra correção obrigatória nos casos especificados pelo PDF. Leve os pontos de interpretação sobre super e reutilização de PlantError para a revisão com um colega se houver orientações locais adicionais. O próprio capítulo de IA recomenda revisão por pares e compreensão do conteúdo usado.

## 11. Fontes usadas

- Subject enviado: Garden Guardian, versão 3.0; páginas impressas 6–18 para regras e exercícios.
- Cinco arquivos Python enviados nesta conversa, preservados sem alterações.
- Guia original enviado, mantido no início e complementado com esta revisão.
- Documentação oficial do mypy sobre supressão por código: https://mypy.readthedocs.io/en/stable/error_codes.html
- Documentação oficial do flake8 sobre opções: https://flake8.pycqa.org/en/stable/user/options.html
- Documentação oficial do flake8 sobre seleção de avisos e configurações padrão: https://flake8.pycqa.org/en/latest/user/violations.html

Os resultados dos comandos são evidência desta execução e dessas versões de ferramentas. A leitura do subject é o que fundamenta a comparação de requisitos.

---

# Checklist da régua de correção da 42 — Python Module 02

Esta seção foi acrescentada após comparar o guia e os arquivos com a régua **Scale for Project Python Module 02 Edit**, recebida em 05/10/2026. A régua é usada na avaliação oral: ela verifica o repositório, cada exercício e se você consegue explicar/reproduzir o comportamento. Marcar um item abaixo significa estar preparada para mostrar evidência dele durante a avaliação; não é uma nota ou aprovação antecipada.

## Antes de começar a avaliação

A régua instrui o avaliador a:

- Avaliar apenas o trabalho que está no seu repositório Git e conferir que o repositório pertence à pessoa certa.
- Verificar que a estrutura corresponde ao subject, sem aliases maliciosos e sem editar arquivos durante a defesa.
- Confirmar a versão Python 3.10 ou superior, Flake8 sem avisos ou erros, um arquivo independente por exercício e type hints em todos os parâmetros e retornos de funções e métodos.
- Verificar que não há exceções sem tratamento capazes de encerrar o programa inesperadamente.

**Sua preparação:** confira se o conteúdo que quer entregar foi commitado e está no repositório correto; organize os cinco arquivos nas pastas `ex0/` a `ex4/`; execute os cinco scripts a partir da estrutura que vai entregar. A cópia de arquivos desta conversa, por si só, não comprova o conteúdo do Git remoto. A régua também pede evitar alteração de arquivos durante a defesa: se surgir um problema, explique-o e discuta-o, sem editar o trabalho no meio da avaliação.

O requisito de estilo da régua é específico: **flake8 sem avisos ou erros**. O mypy continua no subject como verificação de tipos, mas não aparece na checklist geral da régua com a mesma redação de “sem avisos ou erros”. Há uma ressalva intencional para o diagnóstico mypy do erro de tipos do ex2, explicada abaixo.

## Conferência por exercício

### Exercício 0 — `ft_first_exception.py`

A régua espera que você mostre e explique:

- `input_temperature(temp_str)` existe e funciona.
- Ela retorna a temperatura quando a entrada pode ser convertida.
- `test_temperature()` exercita uma entrada válida e outra inválida.
- O `try/except` trata `Exception` ou `ValueError` quando a conversão de `abc` falha.
- A mensagem de erro aparece e o programa continua.
- Você sabe explicar por que `int("abc")` gera erro e por que o programa não encerra.

**Seu código:** atende esses itens. O `except ValueError` é uma captura mais específica que `Exception` e combina com a falha de `int("abc")`.

### Exercício 1 — `ft_raise_exception.py`

A régua espera que você mostre e explique:

- A função do ex0 foi atualizada para validar os limites mínimo e máximo.
- Valores dentro de 0 a 40, inclusive, são devolvidos.
- Valores acima ou abaixo do intervalo geram exceção.
- Os testes incluem entrada válida, inválida e extremos fora da faixa.
- A falha é capturada, explicada e não interrompe os outros testes.

**Seu código:** atende os casos da régua: `25`, `abc`, `100` e `-50`. Os limites exatos `0` e `40` não aparecem na saída principal, mas a implementação os aceita e foram verificados separadamente. Para mostrar tudo diretamente durante a defesa, você pode adicionar `"0"` e `"40"` à lista de testes antes da entrega; são casos de limite recomendáveis, ainda que a régua ilustrada não os nomeie explicitamente.

### Exercício 2 — `ft_different_errors.py`

A régua espera que você mostre e explique:

- `garden_operations()` cria cenários que geram ValueError, ZeroDivisionError, FileNotFoundError e TypeError.
- `test_error_types()` usa **um único bloco try com múltiplas cláusulas except**, uma para cada tipo.
- Cada falha é capturada e a execução continua para a próxima operação.
- Você consegue explicar por que existem diferentes tipos de exceções.
- Você entende por que o mypy avisa sobre a soma entre texto e inteiro, mesmo que a operação esteja propositalmente no exercício.

**Seu código:** atende a estrutura de handlers e os casos. A régua diz explicitamente que o erro mypy nessa linha é intencional. Na cópia analisada, `# type: ignore[operator]` silencia exatamente esse aviso. Para demonstrar a situação tal como descrita pela régua e pelo subject, remova esse comentário antes de submeter; então o mypy deve apontar o erro de operador nessa linha. O aviso esperado não é uma falha de flake8. Os demais quatro arquivos passaram no mypy estrito sem erros; na cópia do ex2 sem a supressão, o único aviso foi `operator` na soma proposital.

Na defesa, explique que `"string" + 5` é incompatível em execução e levanta TypeError; capturá-lo permite continuar. O mypy faz análise estática e detecta a incompatibilidade antes de rodar. Não esconda o aviso fingindo que a operação é válida. A régua pede a demonstração e o entendimento desse contraste.

### Exercício 3 — `ft_custom_errors.py`

A régua espera que você mostre e explique:

- `GardenError` herda de `Exception`.
- `PlantError` e `WaterError` herdam de `GardenError`.
- As classes são simples e têm mensagens padrão.
- Você levanta e captura cada erro específico.
- Capturar `GardenError` também captura seus erros filhos.
- **Você consegue provocar um `PlantError` sem fornecer mensagem e mostrar a mensagem padrão.** A régua pede que o avaliador peça para você demonstrar isso sem modificar as três classes.

**Seu código:** as três classes já têm valores padrão corretos, mas `test_custom_errors()` só levanta erros com uma mensagem explícita. Portanto, a mensagem padrão existe, porém o programa atual não a mostra. Para cumprir a demonstração prática da régua no arquivo submetido, acrescente um caso de teste sem argumento, por exemplo:

```python
def test_default_plant_error() -> None:
    try:
        raise PlantError()
    except PlantError as error:
        print(f"Caught default PlantError: {error}")
```

Chame essa função em `test_custom_errors()` ou demonstre o mesmo trecho ao vivo, sem alterar as classes durante a defesa. Uma demonstração permanente no arquivo é mais fácil de repetir. Você deve explicar que `message` recebe seu valor padrão porque a chamada não forneceu argumento, e `super().__init__(message)` leva esse texto à classe Exception. Faça o mesmo tipo de demonstração para WaterError se quiser comprovar os dois padrões; a régua pede expressamente o teste padrão de PlantError e diz que cada classe deve ter seu padrão.

A régua recomenda que a estrutura de testes siga o padrão do ex2, mas esclarece que isso não é obrigatório. Sua estrutura com funções que levantam erros e handlers separados é válida.

### Exercício 4 — `ft_finally_block.py`

A régua espera que você mostre e explique:

- `water_plant(plant_name)` existe.
- A condição usa a comparação do nome com `capitalize()`.
- Nome que não corresponde à forma capitalizada gera PlantError; um nome aceito mostra sucesso.
- O sistema imprime a abertura antes de começar a rega.
- Existe `try/except/finally` e a falha é tratada.
- Ao encontrar um nome inválido, o teste para e retorna ao corpo principal do arquivo.
- O `finally` sempre imprime o fechamento, mesmo no caso de erro.
- Há cenários normais e com erro.
- Você consegue explicar por que limpeza ainda ocorre após erro e dar exemplos de recursos reais que precisam ser fechados.

**Seu código:** atende esses pontos. `Tomato` é válido; `lettuce` levanta PlantError. A chamada inválida retorna antes de regar `Carrots`, mas o fechamento acontece antes de o controle voltar ao `main()`.

Exemplos de recursos reais para citar: arquivo aberto, conexão com banco, socket ou outro recurso do sistema. Explique que neste exercício a abertura e o fechamento são representados por `print`; o princípio do `finally` é garantir a limpeza ao sair do `try`, tanto por sucesso quanto por exceção/retorno.

## Situação dos seus arquivos frente à régua

| Item da régua | Situação observada | Próxima ação |
| --- | --- | --- |
| Python 3.10+ | Código usa sintaxe `list[str]`, válida em 3.10+; teste realizado com Python 3.12.14 | Na entrega, confirme o interpretador da escola/ambiente |
| Flake8 sem erros ou avisos | Os cinco arquivos passaram no Flake8 7.4.1, configuração isolada | Manter assim ao reorganizar/copiar para o repositório |
| Type hints em funções e métodos | Todos os parâmetros e retornos têm type hints | Preservar as anotações |
| Mypy | Os cinco passaram em `--strict` com a supressão de ex2; sem ela há o erro intencional pedido | Remover `type: ignore` e explicar o aviso de ex2 |
| Um arquivo por exercício | Os nomes dos cinco arquivos estão corretos | Colocá-los nas pastas `ex0` a `ex4` do repositório |
| Captura e continuidade | Execuções demonstrativas terminaram normalmente | Executar cada arquivo no clone final |
| Mensagens padrão do ex3 | As classes têm defaults, mas o teste atual sempre passa mensagem explícita | Incluir/demonstrar `PlantError()` sem argumento |
| Repositório correto e estrutura | Não verificável apenas pelos anexos locais | Conferir o clone/Git e os diretórios antes da avaliação |

### Comandos de conferência antes de entregar

Rode na raiz do projeto, substituindo a forma do comando do mypy se a sua versão ou configuração local exigir:

```bash
python3 --version
python3 -m flake8 ex0/ ex1/ ex2/ ex3/ ex4/
python3 -m mypy --strict --python-version 3.10 ex0/ ex1/ ex2/ ex3/ ex4/
python3 ex0/ft_first_exception.py
python3 ex1/ft_raise_exception.py
python3 ex2/ft_different_errors.py
python3 ex3/ft_custom_errors.py
python3 ex4/ft_finally_block.py
```

Se você removeu a supressão como recomendado, espere o mypy relatar apenas o TypeError intencional do ex2. Confirme que o Flake8 não relata warnings/errors e que cada script mostra tanto o fluxo esperado quanto os casos inválidos. Na avaliação, esteja pronta para explicar o fluxo sem depender apenas de ler a tela.

### Roteiro curto de defesa

1. Mostre o clone/repositório correto e localize `ex0` até `ex4`.
2. Execute cada arquivo e identifique uma entrada válida e uma falha esperada.
3. No ex2, explique cada tipo de exceção e a mensagem do mypy para a soma intencional.
4. No ex3, provoque `PlantError()` sem mensagem e explique o default; depois mostre que `except GardenError` captura PlantError e WaterError.
5. No ex4, mostre que a lista para na planta inválida e que `finally` imprime fechamento antes do retorno.
6. Explique o que fez, sem editar o repositório durante a avaliação.

## Referência da régua

Arquivo enviado nesta conversa: **Regua-02-Python.pdf**, “Scale for Project Python Module 02 Edit”, três páginas, versão impressa em 05/10/2026. Esta checklist resume os critérios da régua para estudo; durante a avaliação, siga as instruções oficiais e as perguntas do avaliador.
