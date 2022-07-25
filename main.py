from random import choice

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывай', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
           'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

def question_f():
    while True:
        question = input()
        print(choice(answers))
        break

def answer():

    while True:

        t = input().lower()

        if t == 'да':
            return True

        elif t == 'нет':
            return False

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.\nКак вас зовут?')
name = input()
print('Здраствуйте,', name, '\nЗадавайте вопрос?')

while True:
    question_f()
    print('Желаете задать ещё вопрос(да/нет)?')
    if answer():
        print('Задавайте.')
        continue
    break

print('Возвращайся, если возникнут вопросы!')
