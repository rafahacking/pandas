import pandas as pd

dataframe = pd.read_csv('notas.csv')
dataframe

materia = dataframe[dataframe['Disciplina'] == 'Matematica']
materia
nota = materia[['Aluno','Disciplina' , 'Nota']]
nota.sort_values('Nota', ascending=False).head(1)

materia = dataframe[dataframe['Disciplina'] == 'Historia']
materia
nota = materia[['Aluno','Disciplina' , 'Nota']]
nota.sort_values('Nota').head(1)

materia = dataframe[dataframe['Disciplina'] == 'Historia']
materia
nota = materia[['Aluno','Disciplina' , 'Nota']]
nota.sort_values('Nota').head(10)

media = dataframe.groupby('Aluno')['Nota'].mean()
media

media.reset_index().sort_values('Nota', ascending=False).head(3)

notasfisicaequimica = dataframe[(dataframe['Disciplina'] == 'Fisica') | (dataframe['Disciplina'] == 'Quimica')]
notasfisicaequimica
notasfisicaequimica = notasfisicaequimica.groupby('Aluno')['Nota'].mean()
notasfisicaequimica.reset_index().sort_values('Nota', ascending=False).head(1)


pior_disciplina = dataframe.groupby('Disciplina')['Nota'].mean()
pior_disciplina
print(pior_disciplina.reset_index().sort_values('Nota'))
pior_disciplina.reset_index().sort_values('Nota').head(1)

acima_ingles = dataframe[(dataframe['Disciplina'] == 'Ingles') & (dataframe['Nota']> 9)]
acima_ingles

disciplinas = dataframe['Disciplina'].unique()
for disciplina in disciplinas:
    notass = dataframe[dataframe['Disciplina']== disciplina].sort_values(by='Nota', ascending=False)
    notass = notass.head(1)
    print(notass)
