# mota-jokes

Uma biblioteca Python para honrar uma tradicao importante: as piadas ruins do Mota.

O pacote e instalado como `mota-jokes`, mas o import fica como `mota`.
Ele tem dois modulos de primeira classe:

- `mota.jokes`: acervo e motor de piadas ruins.
- `mota.php`: utilidades PHP emocionalmente duvidosas.

```python
from mota import jokes, php

print(jokes.tell("direito"))
print(php.composer_install("mota/bom-senso"))
```

## Instale localmente

```bash
python -m pip install -e .
```

Depois:

```bash
python -m mota
python -m mota jokes direito
python -m mota php
```

## Uso em Python

```python
from mota import jokes, php

print(jokes.random())
print(jokes.explain("direito"))
print(php.echo())
```

## API rapida

```python
jokes.all()
jokes.random()
jokes.by_id("direito")
jokes.tell("direito")
jokes.search("python")
jokes.explain("php")
jokes.cringe_index()

php.echo()
php.is_php("Python")
php.translate("print('ola')")
php.framework()
php.ini_get("display_errors")
php.semicolon("$mota = 'meme'")
php.composer_install("mota/humor")
```

## Publicacao no PyPI

O nome `mota` ja existe no PyPI, entao este projeto usa `mota-jokes` como nome de distribuicao. Isso nao afeta o import:

```bash
pip install mota-jokes
```

```python
from mota import jokes
```

Para publicar:

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine upload dist/*
```

Antes de publicar, troque os links em `pyproject.toml` para o repositorio real.
