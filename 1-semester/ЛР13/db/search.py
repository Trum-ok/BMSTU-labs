from rich.console import Console


def search_by_one_field(file_path, field_index, value):
    console = Console()
    try:
        with open(rf"./user_tables/{file_path}", 'r', encoding='utf-8') as f:
            for line in f:
                record = line.strip().split(',')
                if record[field_index] == value:
                    print(line.strip())
    except FileNotFoundError:
        console.print("[bold red]Файл базы данных не найден.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Ошибка: {e}[/bold red]")


def search_by_two_fields(file_path, field1_index, value1, field2_index, value2):
    console = Console()
    try:
        with open(rf"./user_tables/{file_path}", 'r', encoding='utf-8') as f:
            for line in f:
                record = line.strip().split(',')
                if record[field1_index] == value1 and record[field2_index] == value2:
                    print(line.strip())
    except FileNotFoundError:
        console.print("[bold red]Файл базы данных не найден.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Ошибка: {e}[/bold red]")
