import rich_click as click

import logging

from src.run import run as run_cmd


@click.group()
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Increase verbosity (-v, -vv, -vvv).",
)
def cli(verbose: int) -> None:
    level = {
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG,
    }.get(verbose, logging.INFO)
    logging.basicConfig(format="%(levelname)s: %(message)s", level=level)


cli.add_command(run_cmd)


def main():
    cli()


if __name__ == "__main__":
    main()
