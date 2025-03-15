import os
import typer
from pathlib import Path
from cron_validator import CronValidator

app = typer.Typer(
    add_completion=True,
    help="tidyfs is a simple CLI tool to organize files in a directory"
)

@app.command(
    name="move", 
    help="Organize files in a directory by moving them to folders based on their extensions (e.g. .pdf, .png, .jpg, .mp3, .mp4, etc.)",
)
def organize_files(
    path: Path = typer.Argument(Path.cwd(), exists=True, file_okay=False, dir_okay=True, resolve_path=True, help="Path to the directory to organize")
):
    list_of_files = [f for f in path.iterdir() if f.is_file()]
    for file in list_of_files:
        extension = file.suffix
        name = f'{extension.upper().strip(".")} Files'
        new_dir = path / name
        new_dir.mkdir(exist_ok=True)
        file.rename(new_dir / file.name)

def cron_expression(cron):
    try:
        CronValidator.parse(cron)
        return cron
    except Exception:
        return None

@app.command(
    name="cron",
    help="Run a cron job to organize files in a directory, at a specified time using in the crontab",
)
def cron_organize_files(
    cron: str = typer.Argument(..., help="Time to run the cron job"),
    path: Path = typer.Argument(Path.cwd(), exists=True, file_okay=False, dir_okay=True, resolve_path=True, help="Path to the directory to organize")
):
    if cron_expression(cron):
        command = f"{cron} organize-files move {path}"
        typer.echo(f"Cron job to organize files in {path} has been scheduled to run at {cron}")
        cron_job = f'(crontab -l; echo "{command}") | crontab -'
        os.system(cron_job)
    else:
        typer.echo(f"Invalid cron time: {cron}")
        raise typer.Abort()

if __name__ == "__main__":
    app()