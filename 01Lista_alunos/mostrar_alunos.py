def mostrar(alunos):
    print('='*25)
    for cont in range(3):
        print(f' {cont+1} aluno {alunos["nomes"][cont]}')
        print(f' notas {alunos["1nota"][cont]:4.2f}, {alunos["2nota"][cont]:4.2f}, {alunos["3nota"][cont]:4.2f}')
    print('='*25)
