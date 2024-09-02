# ORE Programming Language

Instruções ao utilizar o compilador para ser executado da maneira correta
- utilize o vscode
- tenha a extensão python extension pack
- rode em modo debug cada arquivo na ordem ore_basic.py -> format.py -> shell.py
- depois para executar só rodar em modo debug o shell.py

### Manual de execução para arquivos no shell.py
| run("path até o arquivo ou o arquivo.ore") |
|--- |

### Operadores Matemáticos da Linguagem
 
| Operador | Função |
|--- |--- |
| + | adição | 
| - | subtração |
| / | divisão |
| * | multiplicação |
| ^ | potenciação |


### Operadores Lógicos da Linguagem

| Operador | Função |
|--- |--- |
| and | e | 
| or | ou |
| != | diferente |
| == | igual |
| > | maior que |
| < | manor que |
| >= | maior ou igual que |
| <= | manor ou igual que |
| to | para |
| step | passo | 
| then | então |
| return | retornar |
| continue | continuar | 
| not | não | 
| end | fim |

### Tipos Primitivos da Linguagem

| Tipo | Função |
|--- |--- |
| string | define letras e números | 
| int | números inteiros ex: 17 |
| float | números reais quebrados ex: 2.1 |
| boolean | true ou false, 0 ou 1 |

### Atribuição de Variaveis

Desta forma você cria e atribui uma variavel

| var | nome da variavel | = | expr |
|--- |--- |--- |--- |

### Comandos de Comparação

| if | variavel == 10 | then | expr |
|--- |--- |--- |--- |

| if | variavel == 10 | then | expr | else | expr
|--- |--- |--- |--- |--- |--- |

### Laços de Repetição

#### no arquivo

| for | i = 0 | to | num or list | then | expr | end |
|--- |--- |--- |--- |--- |--- |--- |

| while | i < num ou list | then | expr | end |
|--- |--- |--- |--- |--- |

#### na shell

| for | i = 0 | to | num or list | then | expr | 
|--- |--- |--- |--- |--- |--- |

| while | i < num ou list | then | expr |
|--- |--- |--- |--- |

### Funções

#### no arquivo

| func | nome da func(parametros) | expr | end |
|--- |--- |--- |--- |

#### na shell

| func | nome da func(parametros) | -> |expr | 
|--- |--- |--- |--- |


### Funções Built In

| NULL | vazio |
|--- |--- |

| FALSE | retorna falso |
|--- |--- |

| TRUE | retorna verdadeira |
|--- |--- |

| math_pi | retorna pi |
|--- |--- |

| math_e | retorna euler |
|--- |--- |

| impout | printa um valor |
|--- |--- |

| input | le uma string digitada pelo usuario |
|--- |--- |

| input_int | le um interiro digitado pelo usuario |
|--- |--- |

| cls | limpa terminal |
|--- |--- |

| clear | limpa terminal |
|--- |--- |

| is_num | retorna true ou false se o valor entre aspas é número |
|--- |--- |

| is_str | retorna true ou false se o valor entre aspas é letras |
|--- |--- |

| is_list | retorna true ou false se o valor entre aspas é lista |
|--- |--- |

| is_func | retorna true ou false se o valor entre aspas é função |
|--- |--- |

| append | adiciona a lista |
|--- |--- |

| pop | remove da lista |
|--- |--- |

| extend | adiciona varios valores a lista |
|--- |--- |

| len | le a lista |
|--- |--- |

