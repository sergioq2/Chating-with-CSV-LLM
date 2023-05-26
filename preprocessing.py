import pandas as pd
import re

def get_data():
    vacantes = pd.read_excel('vacantes.xlsx')
    vacantes_summary = vacantes.drop('description', axis=1)
    users = pd.read_excel('Users.xlsx')
    return vacantes, vacantes_summary, users


def depuration(df):
    df.drop('degrees', axis=1, inplace=True)
    df.drop('wage_aspiration', axis=1, inplace=True)
    df.drop('currency', axis=1, inplace=True)
    df.drop('current_wage', axis=1, inplace=True)
    df['months_experience'] = df['months_experience'].fillna(0)
    df['experience'] = df['years_experience'] + (df['months_experience']/12)
    df.drop(['years_experience','months_experience'], axis=1, inplace=True)
    return df


def mayuscula(df):
    cat_vars = [var for var in df.columns if df[var].dtype=='O']
    for var in cat_vars:
        df[var] = df[var].str.upper()


def limpieza(df):
    cat_vars = [var for var in df.columns if df[var].dtype == 'O']
    for var in cat_vars:
        df[var] = df[var].apply(lambda x: re.sub(r'[^\w\s]', '', x) if isinstance(x, str) else x)

def preprocesamiento():
    vacantes, vacantes_summary, users = get_data()
    users = depuration(users)
    mayuscula(vacantes)
    mayuscula(users)
    limpieza(vacantes)
    limpieza(users)
    return vacantes, vacantes_summary, users

if __name__ == '__main__':
    preprocesamiento()

    