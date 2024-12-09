from rich.table import Table
from rich.console import Console


def display_db(file_path: str, separator: str = ','):
    console = Console()
    try:
        if "." in file_path:
            db_name = file_path.split('.')[-2]
        else:
            db_name = file_path

        table = Table(title=f"Содержимое таблицы {db_name}", expand=True)
        with open(rf"./user_tables/{file_path}", 'r', encoding='utf-8') as f:
            for line in f:
                row = line.strip().split(separator)
                table.add_row(*row)

        console.print(table)
    except FileNotFoundError:
        console.print("[bold red]Файл базы данных не найден.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Ошибка: {e}[/bold red]")
