"""Interface de linha de comando para `mota`."""

from __future__ import annotations

import argparse
import sys

from . import jokes, php


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mota",
        description="Ferramentas inutilmente específicas para manter o meme do Mota vivo.",
    )
    subparsers = parser.add_subparsers(dest="module")

    jokes_parser = subparsers.add_parser("jokes", help="Conta e consulta piadas ruins.")
    jokes_parser.add_argument("id", nargs="?", help="ID da piada. Omita para uma aleatória.")
    jokes_parser.add_argument("--tags", nargs="*", help="Filtra piadas aleatórias por tags.")
    jokes_parser.add_argument("--audit", action="store_true", help="Mostra métricas nada científicas.")
    jokes_parser.add_argument("--search", help="Procura piadas por texto ou tag.")

    php_parser = subparsers.add_parser("php", help="Executa utilidades PHP emocionalmente corretas.")
    php_parser.add_argument(
        "action",
        nargs="?",
        default="echo",
        choices=("echo", "roast", "framework", "composer", "ini"),
    )
    php_parser.add_argument("value", nargs="?", help="Valor usado por composer ou ini.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    module = args.module or "jokes"

    try:
        if module == "jokes":
            if args.audit:
                for key, value in jokes.audit().items():
                    print(f"{key}: {value}")
            elif args.search:
                results = jokes.search(args.search)
                for joke in results:
                    print(joke)
                    print()
                if not results:
                    print("Nenhuma piada encontrada. Isso talvez seja uma melhoria.")
            else:
                print(jokes.tell(args.id, tags=args.tags))
        elif module == "php":
            if args.action == "echo":
                print(php.echo())
            elif args.action == "roast":
                print(php.roast())
            elif args.action == "framework":
                print(php.framework())
            elif args.action == "composer":
                print(php.composer_install(args.value or "mota/humor"))
            elif args.action == "ini":
                print(php.ini_get(args.value or "display_errors"))
        else:
            parser.print_help()
            return 2
    except (KeyError, ValueError) as error:
        print(error, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
