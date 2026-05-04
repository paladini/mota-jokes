# mota-jokes

Uma biblioteca Python para honrar uma tradição importante: as piadas ruins do Mota.

O pacote é instalado como `mota-jokes`, mas o import fica como `mota`. A ideia é simples: transformar o folclore interno de um amigo que insiste em manter o meme vivo numa API Python publicável, testável e completamente desnecessária.

Ele tem dois módulos de primeira classe:

- `mota.jokes`: acervo e motor de piadas ruins.
- `mota.php`: utilidades PHP emocionalmente duvidosas.

```python
from mota import jokes, php

print(jokes.tell("direito"))
print(php.composer_install("mota/bom-senso"))
```

## Instalação

```bash
python -m pip install mota-jokes
```

Para desenvolvimento local:

```bash
python -m pip install -e .
```

## Linha de comando

Depois de instalar:

```bash
python -m mota
python -m mota jokes direito
python -m mota jokes --search python
python -m mota php
python -m mota php framework
python -m mota php composer mota/bom-senso
```

Se o diretório de scripts do Python estiver no `PATH`, o comando `mota` também fica disponível diretamente:

```bash
mota jokes direito
```

## Uso em Python

```python
from mota import jokes, php

print(jokes.random())
print(jokes.explain("direito"))
print(php.echo())
```

## API rápida

```python
jokes.all()
jokes.random()
jokes.by_id("direito")
jokes.tell("direito")
jokes.search("python")
jokes.explain("php")
jokes.audit()
jokes.cringe_index()

php.echo()
php.is_php("Python")
php.translate("print('olá')")
php.framework()
php.ini_get("display_errors")
php.semicolon("$mota = 'meme'")
php.composer_install("mota/humor")
```

## Exemplo canônico

```python
from mota import jokes

print(jokes.tell("direito"))
```

Saída:

```text
Nossa, bicho, já pensou em fazer Direito?
Por quê, tô fazendo errado?
```

## Publicação no PyPI

O nome `mota` já existe no PyPI, então este projeto usa `mota-jokes` como nome de distribuição. Isso não afeta o import:

```bash
pip install mota-jokes
```

```python
from mota import jokes, php
```

Para publicar uma nova versão:

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
python -m twine upload dist/*
```

Antes de publicar, lembre-se de incrementar a versão em `pyproject.toml` e `src/mota/__init__.py`, porque o PyPI não permite reenviar a mesma versão.
