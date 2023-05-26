import json

def answer_output(answer):
    try:
        answer = answer.strip()

        split_values = answer.split(',')

        job_vacancies = {}

        for value in split_values:
            vacancy, match_value = value.split(':')
            vacancy = vacancy.strip()
            match_value = match_value.strip('%.')
            job_vacancies[vacancy] = float(match_value)

        json_data = json.dumps(job_vacancies, indent=4)
    except:
        answer = answer.strip()
        split_values = answer.split(', ')
        job_vacancies = {}

        for value in split_values:
            vacancy_name, match_value = value.split(': ')
            vacancy_name = vacancy_name.strip()
            match_value = match_value.strip('%.')
            job_vacancies[vacancy_name] = float(match_value) / 100

        json_data = json.dumps(job_vacancies, indent=4)
    return json_data

if __name__ == '__main__':
    answer_output()