from rich.console import Console


def add_new_record(file_path: str, record: str, separator: str = ','):
    console = Console()
    try:
        with open(rf"./user_tables/{file_path}", 'a', encoding='utf-8') as f:
            f.write(separator.join(record) + '\n')
    except FileNotFoundError:
        console.print("[bold red]Файл базы данных не найден.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Ошибка: {e}[/bold red]")

