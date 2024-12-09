def initialize_db(file_path: str, records: str, separator: str = ","):
    with open(rf"./user_tables/{file_path}", 'w', encoding='utf-8') as f:
        for record in records:
            f.write(separator.join(record) + '\n')
