"""Módulo PHP do pacote Mota.

Não interpreta PHP. Apenas interpreta a fase da vida em que alguém defende PHP
com convicção demais.
"""

from __future__ import annotations

from random import SystemRandom


_random = SystemRandom()

_FRAMEWORKS = (
    "Laravel, porque até o caos merece fachada bonita.",
    "Symfony, quando a piada precisa de injeção de dependência.",
    "CodeIgniter, preservado em formol e memória afetiva.",
    "WordPress, tecnicamente não era para ser framework, mas também tecnicamente funciona.",
)

_ECHOES = (
    "<?php echo 'Por quê, tô fazendo errado?'; ?>",
    "<?php var_dump('humor'); // string(5) \"ruim\" ?>",
    "<?php require_once 'bom_senso.php'; // arquivo não encontrado ?>",
    "<?php $mota->contarPiada()->arrependimento(); ?>",
)

_INI_VALUES = {
    "display_errors": "On, principalmente em produção, segundo o folclore.",
    "memory_limit": "-1, porque limite é coisa de linguagem sem fé.",
    "date.timezone": "America/Sao_Paulo; ajuste técnico para sofrer no horário certo.",
    "short_open_tag": "Off, mas a discussão continua ligada.",
}


def echo() -> str:
    """Retorna uma frase com energia PHP."""

    return _random.choice(_ECHOES)


def is_php(language: str) -> bool:
    """Descobre se uma linguagem é PHP, inclusive quando ela insiste que mudou."""

    normalized = language.strip().casefold()
    return normalized in {"php", "<?php", "laravel", "wordpress"}


def translate(python_code: str) -> str:
    """Traduz Python para PHP emocionalmente, não sintaticamente."""

    stripped = python_code.strip() or "# nada"
    return (
        "<?php\n"
        "// Tradução oficial do Mota, certificada por zero comitês.\n"
        f"// Python original: {stripped}\n"
        "echo 'Funcionou na minha máquina';\n"
        "?>"
    )


def framework() -> str:
    """Recomenda um framework PHP com a precisão de uma piada de corredor."""

    return _random.choice(_FRAMEWORKS)


def ini_get(name: str) -> str:
    """Consulta uma configuração PHP imaginária."""

    normalized = name.strip()
    return _INI_VALUES.get(normalized, f"{normalized}=talvez; depende do servidor compartilhado.")


def semicolon(line: str) -> str:
    """Adiciona ponto e vírgula com a autoridade moral de quem já viu PHP demais."""

    stripped = line.rstrip()
    if stripped.endswith(";"):
        return stripped
    return f"{stripped};"


def composer_install(package: str = "mota/humor") -> str:
    """Simula uma instalação Composer que não resolve o problema central."""

    normalized = package.strip() or "mota/humor"
    return (
        f"composer require {normalized}\n"
        "Pacote instalado. O humor ainda requer configuração manual."
    )


def roast() -> str:
    """Resumo executivo do módulo."""

    return "PHP: porque toda amizade merece um ponto e vírgula mal resolvido."
