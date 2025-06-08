import rich_click as click

from src.console import console
from src._utils._cli import get_section


@click.command()
@click.argument("problem_id")
def run(problem_id: str) -> None:
    console.print("Calling command run...")

    codepath = ".".join(["src", get_section(problem_id), problem_id])

    # (calvin): update so there's a function call here
    # right now we just execute the file on import
    __import__(codepath)
