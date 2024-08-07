import sqlite3
import hashlib

class Database:
    def __init__(self, db_name="eduPass.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    #Função para criar as tabelas que serão utilizadas
    def create_tables(self):

        try:
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS Alunos(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    cpf TEXT NOT NULL,
                                    email TEXT NOT NULL,
                                    celular TEXT NOT NULL,
                                    password TEXT NOT NULL
                                )
                            ''')
        
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS Cursos(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    tipo TEXT NOT NULL,
                                    unidade TEXT NOT NULL,
                                    curso TEXT NOT NULL,
                                    turno TEXT NOT NULL,
                                    frequencia TEXT NOT NULL,
                                    aprovado TEXT CHECK(aprovado IN ('aprovado', 'analise', 'reprovado')) DEFAULT 'analise',
                                    comentario TEXT,
                                    aluno_id INTEGER,
                                    FOREIGN KEY (aluno_id) REFERENCES Alunos(id)
                                )
                            ''')
            
            self.conn.commit()

            print("Tabelas criadas com sucesso")

        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")
        

    #Função para gerar hash da senha
    def hash_password(self, password):
        # Cria o hash da senha com salt
        hasher = hashlib.sha256()
        hasher.update(password.encode('utf-8'))
        return hasher.hexdigest()

    #Função para inserir alunos no banco de dados
    def add_student(self, nome, cpf, email, celular, password):

        hashed_password = self.hash_password(password)

        try:
            self.cursor.execute("INSERT INTO Alunos (nome, cpf, email, celular, password) VALUES (?, ?, ?, ?, ?)", (nome, cpf, email, celular, hashed_password))

            self.conn.commit()

            print("Aluno inserido com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir aluno: {e}")

    #Função para inserir cursos no banco de dados
    def add_course(self, tipo, unidade, curso, turno, frequencia, aprovado, comentario, aluno_id):
        try:
            self.cursor.execute('''
                                INSERT INTO Cursos (tipo, unidade, curso, turno, frequencia, aprovado, comentario, aluno_id) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                                (tipo, unidade, curso, turno, frequencia, aprovado, comentario, aluno_id))
            
            self.conn.commit()

            print("Curso inserido com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir curso: {e}")

    #Função para fechar a conexão
    def close(self):
        self.conn.close()
