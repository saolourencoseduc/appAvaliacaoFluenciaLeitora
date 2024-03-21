import pandas as pd
from app import create_app, db  # Ajuste essa importação conforme necessário para o seu aplicativo
# Certifique-se de que os modelos estejam importados corretamente
from app.models.models import Aluno

app = create_app()

with app.app_context():
    db.create_all()

    csv_path = 'C:\\Users\\bruco\\Downloads\\alunos_2024-02-29_09_41_15.csv'
    df = pd.read_csv(csv_path, on_bad_lines='skip')
    
    # Substitui valores NaN por None para todos os campos do DataFrame
    df = df.where(pd.notnull(df), None)

    for index, row in df.iterrows():
        aluno = Aluno(
            nome=row['Nome'],
            cpf=row['CPF'],
            data_nascimento=pd.to_datetime(row['Data de nascimento'], errors='coerce'),  # Trata erros de conversão
            escola=row['Escola'],
            turma=row['Turma'],
            serie=row['Série'],
            curso=row['Curso'],
            ano=int(row['Ano']),
            turno=row['Turno'],
            nome_mae=row.get('Nome da mãe'),
            nome_pai=row.get('Nome do pai'),
            nome_responsavel=row.get('Nome do responsável')
        )
        
        db.session.add(aluno)

    try:
        db.session.commit()
        print("CSV data successfully imported into the database.")
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.session.close()
