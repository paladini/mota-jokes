"""Piadas ruins do Mota, preservadas em API publica."""

from __future__ import annotations

from dataclasses import dataclass
from random import SystemRandom
from typing import Iterable


_random = SystemRandom()


@dataclass(frozen=True)
class Joke:
    """Uma piada ruim, mas com contrato de dados respeitavel."""

    id: str
    setup: str
    punchline: str
    tags: tuple[str, ...] = ()

    def __str__(self) -> str:
        return f"{self.setup}\n{self.punchline}"


_JOKES: tuple[Joke, ...] = (
    Joke(
        id="direito",
        setup="Nossa bicho, ja pensou em fazer Direito?",
        punchline="Pq, to fazendo errado?",
        tags=("classica", "faculdade", "crime-de-baixa-gravidade"),
    ),
    Joke(
        id="import",
        setup="O Mota foi contar uma piada boa.",
        punchline="Deu ImportError: cannot import name 'humor'.",
        tags=("python", "stacktrace"),
    ),
    Joke(
        id="commit",
        setup="O Mota subiu uma piada no Git.",
        punchline="O review pediu changes por excesso de trocadilho.",
        tags=("git", "review"),
    ),
    Joke(
        id="pep8",
        setup="A piada do Mota passou no formatador.",
        punchline="Mesmo assim o bom senso quebrou em 79 colunas.",
        tags=("python", "pep8"),
    ),
    Joke(
        id="debug",
        setup="Como o Mota testa uma piada?",
        punchline="Coloca um breakpoint antes da vergonha.",
        tags=("debug", "vergonha-controlada"),
    ),
    Joke(
        id="php",
        setup="O Mota disse que PHP e uma linguagem elegante.",
        punchline="A sala retornou HTTP 500.",
        tags=("php", "opiniao-forte"),
    ),
    Joke(
        id="async",
        setup="O Mota prometeu parar com piada ruim.",
        punchline="Ficou pendente para sempre: await mota.bom_senso().",
        tags=("async", "promessa"),
    ),
    Joke(
        id="typing",
        setup="O Mota adicionou type hints na piada.",
        punchline="Agora ela e ruim de forma estaticamente verificavel.",
        tags=("typing", "python"),
    ),
)


def all() -> tuple[Joke, ...]:
    """Retorna todas as piadas cadastradas."""

    return _JOKES


def ids() -> tuple[str, ...]:
    """Retorna os identificadores disponiveis."""

    return tuple(joke.id for joke in _JOKES)


def by_id(joke_id: str) -> Joke:
    """Busca uma piada pelo id."""

    normalized = joke_id.strip().lower()
    for joke in _JOKES:
        if joke.id == normalized:
            return joke
    available = ", ".join(ids())
    raise KeyError(f"Piada '{joke_id}' nao encontrada. Disponiveis: {available}")


def random(tags: Iterable[str] | None = None) -> Joke:
    """Retorna uma piada aleatoria, opcionalmente filtrada por tags."""

    pool = _JOKES
    if tags is not None:
        wanted = {tag.strip().lower() for tag in tags}
        pool = tuple(joke for joke in _JOKES if wanted.intersection(joke.tags))
    if not pool:
        raise ValueError("Nenhuma piada encontrada para essas tags. O Mota tentou, falhou, e ainda contou.")
    return _random.choice(pool)


def tell(joke_id: str | None = None, *, tags: Iterable[str] | None = None) -> str:
    """Conta uma piada pronta para terminal, chat ou constrangimento presencial."""

    joke = random(tags) if joke_id is None else by_id(joke_id)
    return str(joke)


def search(term: str) -> tuple[Joke, ...]:
    """Procura piadas por texto, porque ate piada ruim precisa de descoberta."""

    normalized = term.strip().casefold()
    return tuple(
        joke
        for joke in _JOKES
        if normalized in joke.id.casefold()
        or normalized in joke.setup.casefold()
        or normalized in joke.punchline.casefold()
        or any(normalized in tag.casefold() for tag in joke.tags)
    )


def direito() -> str:
    """Atalho para a piada canonica do acervo."""

    return by_id("direito").punchline


def explain(joke_id: str = "direito") -> str:
    """Explica a piada, porque algumas tragedias precisam de documentacao."""

    joke = by_id(joke_id)
    return (
        f"Setup: {joke.setup}\n"
        f"Punchline: {joke.punchline}\n"
        "Diagnostico: piada ruim com reproducibilidade alta."
    )


def audit() -> dict[str, object]:
    """Retorna metricas nada cientificas sobre o acervo."""

    return {
        "total": len(_JOKES),
        "qualidade_media": "questionavel",
        "risco_social": "alto",
        "mitigacao": "rir para nao incentivar, mas rir mesmo assim",
    }


def cringe_index(joke_id: str | None = None) -> int:
    """Calcula um indice de vergonha de 0 a 100, com ciencia nenhuma."""

    joke = random() if joke_id is None else by_id(joke_id)
    return min(100, 42 + len(joke.punchline) + len(joke.tags) * 7)
