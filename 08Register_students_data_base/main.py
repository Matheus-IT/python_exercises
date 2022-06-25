import sqlite3
from os import system


class Student():
	def __init__(self, name='', grades=[], average=0.0):
		self.name: str = name
		self.grades: list = grades
		self.average: float = average


def register(stds):
	from functools import reduce
	qtt: int

	qtt = int(input(' - Cadastrar quantos alunos? '))
	for c in range(qtt):
		n: str
		g: list = []
		a: float

		n = str(input(f' - Digite o nome do {c + 1} aluno: ')).strip().capitalize()
		for i in range(3):
			g.append(float(input(f' - Digite a {i + 1} nota de {n}: ')))
		a = (reduce(lambda x, y: x + y, g) / 3)
		stds.append(Student(n, g, a))


def show(stds):
	for std in stds:
		print(' = Resultado = ')
		print(f' - Nome: {std.name} \n' +
			  f' - Notas: {std.grades} \n' +
			  f' - Média: {std.average:.2f} \n')


def showDatabase(database):
	try:
		connection = sqlite3.Connection(database)
	except Error as e:
		print(e)
	else:
		cur = connection.cursor()
		cur.execute('SELECT * FROM students')
		for row in cur.fetchall():
			print(row)
		cur.close()
		connection.close()


def deleteFrom(database):
	showDatabase(database)
	rec_id: int = int(input(' - Qual registro deseja deletar? ').strip())
	try:
		connection = sqlite3.connect(database)
	except Error as e:
		print(e)
	else:
		cur = connection.cursor()
		cur.execute('CREATE UNIQUE INDEX index ON students(name, grade_01, grade_02, grade_03, average)')
		cur.execute('DELETE FROM students WHERE id = ?', (rec_id,))
		connection.commit()
		cur.close()
		connection.close()
		showDatabase(database)


def save(stds):
	try:
		connection = sqlite3.connect('students.db')
	except Error as e:
		print(e)
	else:
		cur = connection.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS students(' +
				  'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
				  'name TEXT NOT NULL, ' +
				  'grade_01 REAL NOT NULL, ' +
				  'grade_02 REAL NOT NULL, ' +
				  'grade_03 REAL NOT NULL, ' +
				  'average REAL NOT NULL)')
		cont: int = 0
		for std in stds:
			cont += 1
			cur.execute('INSERT INTO students (name, grade_01, grade_02, grade_03, average) VALUES(?, ?, ?, ?, ?)', (\
				std.name, std.grades[0], std.grades[1], std.grades[2], std.average))
		connection.commit()
		cur.close()
		connection.close()


def main():
	students: list = []
	r: str

	while True:
		r = str(input(' - Qual operação realizar? \n' +
							' - [1] Cadastrar estudantes \n' +
							' - [2] Mostrar estudantes cadastrados \n' +
							' - [3] Deletar registro \n' +
							' - [4] Sair \n' +
							'=>> ')).strip()[0]
		system('cls')
		if int(r) == 1:
			register(students)
			r = str(input(' - Salvar os dados dos estudantes no banco de dados [S/N]? ')).upper()[0]
			if r == 'S':
				save(students)
		elif int(r) == 2:
			showDatabase('students.db')
		elif int(r) == 3:
			deleteFrom('students.db')
		elif int(r) == 4:
			break
	print(' - Programa finalizado')


if __name__ == '__main__':
	main()
