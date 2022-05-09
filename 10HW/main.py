import json

from flask import Flask

def get_candidates(arg):
    """Получает список кандидатов из стороннего файла"""
    with open(arg, "r", encoding="utf-8") as file:
        return json.load(file)


app = Flask(__name__)

@app.route('/')
def main():
    candidates = get_candidates("candidates.json")
    result = '<pre>'
    for candidate in candidates:
        result += (f'Имя кандидата - {candidate["name"]}\n'
                   f'Позиция кандидата - {candidate["position"]}\n'
                   f'Навыки через запятую - {candidate["skills"]}\n\n')

    result += '</pre>'
    return result

@app.route('/candidate/<int:candidate_id>')
def page_candidate(candidate_id):
    candidates = get_candidates("candidates.json")
    result = ''
    for i in candidates:
        if candidate_id == i['id']:
            result += f'<img src={i["picture"]}>'
            result += (f'<pre>'
                       f'Имя кандидата - {i["name"]}\n'
                       f'Позиция кандидата - {i["position"]}\n'
                       f'Навыки через запятую - {i["skills"]}\n\n')
    result += '</pre>'
    if result == '</pre>':
        return f"<pre>Кандидат не найден</pre>", "404"
    return result



@app.route('/skills/<skill>')
def skills(skill):
    candidates = get_candidates("candidates.json")
    result = '<pre>'

    for candidate in candidates:
        if skill.lower() in candidate['skills'].lower():
            result += (f'Имя кандидата - {candidate["name"]}\n'
                   f'Позиция кандидата - {candidate["position"]}\n'
                   f'Навыки через запятую - {candidate["skills"]}\n\n')
    result += '</pre>'
    return result



app.run()