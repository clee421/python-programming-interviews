import rich_click as click

from src.console import console


@click.command()
def run() -> None:
    console.print("Calling command run...")
