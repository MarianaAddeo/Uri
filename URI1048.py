
Salary = float(input())
SalaryRound = float("{0:.2f}".format(Salary))
if SalaryRound >= 0.00 and SalaryRound <= 400.00:
    Reajuste = (SalaryRound * 15) / 100
    Novosalario = Reajuste + SalaryRound
    percentual = 15
    print('Novo salario: {0:.2f}'.format(Novosalario))
    print('Reajuste ganho: {0:.2f}'.format(Reajuste))
    print('Em percentual: {} %'.format(percentual))
elif SalaryRound >= 400.01 and SalaryRound <= 800:
    Reajuste = (salaryRound * 12) / 100
    Novosalario = Reajuste + SalaryRound
    percentual = 12
    print('Novo salario: {0:.2f}'.format(Novosalario))
    print('Reajuste ganho: {0:.2f}'.format(Reajuste))
    print('Em percentual: {} %'.format(percentual))
elif 800.01 <= SalaryRound <= 1200:
    Reajuste = (SalaryRound * 10) / 100
    Novosalario = Reajuste + SalaryRound
    percentual = 10
    print('Novo salario: {0:.2f}'.format(Novosalario))
    print('Reajuste ganho: {0:.2f}'.format(Reajuste))
    print('Em percentual: {} %'.format(percentual))
elif SalaryRound >= 1200.01 and SalaryRound <= 2000:
    Reajuste = (SalaryRound * 7) / 100
    Novosalario = Reajuste + SalaryRound
    percentual = 7
    print('Novo salario: {0:.2f}'.format(Novosalario))
    print('Reajuste ganho: {0:.2f}'.format(Reajuste))
    print('Em percentual: {} %'.format(percentual))
elif SalaryRound > 2000:
    Reajuste = (SalaryRound * 4) / 100
    Novo_salario = Reajuste + SalaryRound
    percentual = 4
    print('Novo salario: {0:.2f}'.format(Novosalario))
    print('Reajuste ganho: {0:.2f}'.format(Reajuste))
    print('Em percentual: {} %'.format(percentual))
