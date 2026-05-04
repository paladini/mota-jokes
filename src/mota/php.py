"""Modulo PHP do pacote Mota.

Nao interpreta PHP. Apenas interpreta a fase da vida em que alguem defende PHP
com conviccao demais.
"""

from __future__ import annotations

from random import SystemRandom


_random = SystemRandom()

_FRAMEWORKS = (
    "Laravel, porque ate o caos merece fachada bonita.",
    "Symfony, quando a piada precisa de injecao de dependencia.",
    "CodeIgniter, preservado em formol e memoria afetiva.",
    "WordPress, tecnicamente nao era para ser framework, mas tambem tecnicamente funciona.",
)

_ECHOES = (
    "<?php echo 'Pq, to fazendo errado?'; ?>",
    "<?php var_dump('humor'); // string(5) \"ruim\" ?>",
    "<?php require_once 'bom_senso.php'; // arquivo nao encontrado ?>",
    "<?php $mota->contarPiada()->arrependimento(); ?>",
)

_INI_VALUES = {
    "display_errors": "On, principalmente em producao, segundo o folclore.",
    "memory_limit": "-1, porque limite e coisa de linguagem sem fe.",
    "date.timezone": "America/Sao_Paulo; ajuste tecnico para sofrer no horario certo.",
    "short_open_tag": "Off, mas a discussao continua ligada.",
}


def echo() -> str:
    """Retorna uma frase com energia PHP."""

    return _random.choice(_ECHOES)


def is_php(language: str) -> bool:
    """Descobre se uma linguagem e PHP, inclusive quando ela insiste que mudou."""

    normalized = language.strip().casefold()
    return normalized in {"php", "<?php", "laravel", "wordpress"}


def translate(python_code: str) -> str:
    """Traduz Python para PHP emocionalmente, nao sintaticamente."""

    stripped = python_code.strip() or "# nada"
    return (
        "<?php\n"
        "// Traducao oficial do Mota, certificada por zero comites.\n"
        f"// Python original: {stripped}\n"
        "echo 'Funcionou na minha maquina';\n"
        "?>"
    )


def framework() -> str:
    """Recomenda um framework PHP com a precisao de uma piada de corredor."""

    return _random.choice(_FRAMEWORKS)


def ini_get(name: str) -> str:
    """Consulta uma configuracao PHP imaginaria."""

    normalized = name.strip()
    return _INI_VALUES.get(normalized, f"{normalized}=talvez; depende do servidor compartilhado.")


def semicolon(line: str) -> str:
    """Adiciona ponto e virgula com a autoridade moral de quem ja viu PHP demais."""

    stripped = line.rstrip()
    if stripped.endswith(";"):
        return stripped
    return f"{stripped};"


def composer_install(package: str = "mota/humor") -> str:
    """Simula uma instalacao Composer que nao resolve o problema central."""

    normalized = package.strip() or "mota/humor"
    return (
        f"composer require {normalized}\n"
        "Package installed. Humor still requires manual configuration."
    )


def roast() -> str:
    """Resumo executivo do modulo."""

    return "PHP: porque toda amizade merece um ponto e virgula mal resolvido."
