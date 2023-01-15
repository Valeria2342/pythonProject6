import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "Когда родился М.Ю. Лермнотов? ", #15.10.1814
    "Когда родился М.В. Ломоносов? ", #19.11.1711
    "Когда родился Н.В. Гоголь? ", #20.03.1809
    "Когда родился Ф.М. Достоевский? ", #11.11.1821
    "Когда родился А.П. Чехов? ", #29.01.1860
    "Когда родился М.А. Булгаков?", #15.05.1891
    "Когда родился Л.Н. Толстой?", #28.08.1828
    "Когда родился И.С. Тургенев?", #09.11.1818
    "Когда родился И.А. Бунин?",  #22.10.1870
    "Когда родился Н.А. Некрасов?", #10.12.1812
]

questions = [
    Question(question_prompts[0], "15.10.1814"),
    Question(question_prompts[1], "19.11.1711"),
    Question(question_prompts[2], "20.03.1809"),
    Question(question_prompts[3], "11.11.1821"),
    Question(question_prompts[4], "29.01.1860"),
    Question(question_prompts[5], "15.05.1891"),
    Question(question_prompts[6], "28.08.1828"),
    Question(question_prompts[7], "09.11.1818"),
    Question(question_prompts[8], "22.10.1870"),
    Question(question_prompts[9], "10.12.1812")
]

random_questions = random.sample(questions, 5)

def run_test(random_questions):
    score = 0
    wrong_answers = 0
    while True:
        for i in questions:
            answer = input(i.prompt)
            if answer == str(i.answer):
                score += 1
            else:
                wrong_answers += 1

        print('Вы ответили правильно на ' + str(score) + ' вопросов из ' + str(len(questions)))
        print('Вы ответили неправильно на ' + str(wrong_answers) + ' вопросов из ' + str(len(questions)))
        print('Процент правильных ответов: ' + str((score * 100) / len(questions)) + '%')
        print('Процент неправильных ответов: ' + str(100 - ((score * 100) / len(questions))) + '%')

        one_more_time = input('Хотите сыграть ещё? ')

        if one_more_time == "да":
            print("Сыграем ещё раз")
        else:
            break

run_test(questions)