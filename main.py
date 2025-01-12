from telebot import TeleBot, types
import random
import os

bot = TeleBot('7184508258:AAFzvF1R6Owgwwou_6jUD3TP7TrkbWgjZjw')

 

@bot.message_handler(commands=['start'])
def start_comment(message):
    keyboard = types.InlineKeyboardMarkup()

    row1 = [
        types.InlineKeyboardButton('📥 Скачать приложение', callback_data='download'),
        types.InlineKeyboardButton('📚 Полезные ресурсы', callback_data='resources')
    ]

    row2 = [
        types.InlineKeyboardButton('❓ Часто задаваемые вопросы', callback_data='faq'),
        types.InlineKeyboardButton('🚀 Почему Python?', callback_data='why python'),
        types.InlineKeyboardButton('📝 Жалобы и Предложения', callback_data='feedback')
    ]

    row3 = [
        types.InlineKeyboardButton('💻 Сайты для практики', callback_data='practice'),
        types.InlineKeyboardButton('📄 Примеры кода', callback_data='examples'),
        types.InlineKeyboardButton('🧠 Тест', callback_data='quiz')
    ]

    row4 = [
        types.InlineKeyboardButton('📅 Ежедневные задания', callback_data='daily_task'),
        types.InlineKeyboardButton('🌟 Особенные темы', callback_data='special_topics'),
        types.InlineKeyboardButton('🏫 Список вузов', callback_data='listhigh')
    ]

    row5 = [
        types.InlineKeyboardButton('👤 Создатель', callback_data='the_creator')
    ]

    keyboard.add(*row1)
    keyboard.add(*row2)
    keyboard.add(*row3)
    keyboard.add(*row4)
    keyboard.add(*row5)

    bot.send_message(message.chat.id, '👋 Добро пожаловать! Выберите опцию:', reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'faq':
        reply_keyboard = types.ReplyKeyboardMarkup(True, True)
        reply_keyboard.add(types.KeyboardButton('💡 О Python'))
        reply_keyboard.add(types.KeyboardButton('📖 Рекомендации о учебе'))

        bot.send_message(call.message.chat.id, 'Выберите нужный вопрос:', reply_markup=reply_keyboard)

    elif call.data == 'О Python':
        about_python_message = ('🐍 Python — это высокоуровневый язык программирования, '
                                'известный своей простотой и читаемостью. '
                                'Он активно используется в веб-разработке, тестировании, '
                                'машинном обучении и Data Science.\n'
                                '🔗 Дополнительную информацию можно найти на официальном сайте: https://www.python.org/')
        bot.send_message(call.message.chat.id, about_python_message)
    
    
    elif call.data == 'Рекомендации о учебе':
        studying_recommendations_message = ('Вот несколько советов по изучению Python:\n'
                                             '1. 📚 Если Вы в 10 классе, изучайте постепенно, но если в 11, '
                                             'занимайтесь каждый день (минимум час).\n'
                                             '2. 🌐 Используйте полезные сайты для подготовки.\n'
                                             '3. ❗ Постарайтесь не заучивать шаблоны, а вникнуть в суть задач.\n'
                                             '4. 🤝 Не стесняйтесь обращаться к своему учителю за помощью!')
        bot.send_message(call.message.chat.id, studying_recommendations_message)

    elif call.data == 'listhigh':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('🎓 220+', callback_data='220ballov'))
        keyboard.add(types.InlineKeyboardButton('🎓 270+', callback_data='270ballov'))
        keyboard.add(types.InlineKeyboardButton('🎓 290+', callback_data='290ballov'))

        bot.send_message(call.message.chat.id, 'Если что, это списки вузов, куда можно поступить с такими баллами ПО НАПРАВЛЕНИЮ IT. Укажите сколько баллов у Вас за ЕГЭ:', reply_markup=keyboard)

    elif call.data == '220ballov':
        ballov220_message = ('🎓 Есть очень много вузов, куда ты можешь поступить с такими баллами:\n'
                             'Например:\n'
                             '1) МИСИС\n'
                             '2) СТАНКИН\n'
                             '3) Московский институт электронной техники.\n'
                             '💡 P.S. Их очень много, главное смотрите на факультет, который вас интересует')
        bot.send_message(call.message.chat.id, ballov220_message)

    elif call.data == '270ballov':
        ballov270_message = ('🎓 Есть очень много вузов, куда ты можешь поступить с такими баллами:\n'
                             '1) Финансовый университет при Правительстве Российской Федерации (Финуниверситет): Программа «Бизнес-информатика».\n'
                             '2) Российский университет дружбы народов (РУДН): Факультет математики и естественных наук.\n'
                             '3) РТУ МИРЭА\n'
                             '4) МИФИ\n'
                             '💡 P.S. Их очень много, главное смотрите на факультет, который вас интересует')
        bot.send_message(call.message.chat.id, ballov270_message)

    elif call.data == '290ballov':
        ballov290_message = ('🎓 Есть очень много вузов, куда ты можешь поступить с такими баллами:\n'
                             '1) МГТУ им. Баумана\n'
                             '2) МФТИ\n'
                             '3) МГУ им. Ломоносова\n'
                             '4) НИУ ВШЭ\n'
                             '5) ИТМО\n'
                             '💡 P.S. Их очень много, главное смотрите на факультет, который вас интересует')
        bot.send_message(call.message.chat.id, ballov290_message)

    elif call.data == 'the_creator':
        the_creator_message = ('👋 Всем привет!\n'
                               'Я Зубаиров Рамис, ученик 10 класса. Обучаюсь в физ-мат классе.\n'
                               '🛠 Я создал этого телеграм бота для более удобной подготовки к ЕГЭ.\n'
                               'Тут можно найти много материала для подготовки.\n'
                               '📅 В будущем планируется: Расширение функций и улучшение взаимодействия с пользователем')
        bot.send_message(call.message.chat.id, the_creator_message)

    elif call.data == 'quiz':
        start_quiz(call.message)


    elif call.data == 'examples':
        keyboard = types.InlineKeyboardMarkup()

        row1 = [
            types.InlineKeyboardButton('📄 Задание №2', callback_data='Задание №2'),
            types.InlineKeyboardButton('📄 Задание №6', callback_data='Задание №6'),
            types.InlineKeyboardButton('📄 Задание №12', callback_data='Задание №12'),
        ]

        row2 = [
            types.InlineKeyboardButton('📄 Задание №14', callback_data='Задание №14'),
            types.InlineKeyboardButton('📄 Задание №15', callback_data='Задание №15'),
            types.InlineKeyboardButton('📄 Задание №16', callback_data='Задание №16'),
        ]

        row3 = [
            types.InlineKeyboardButton('📄 Задание №17', callback_data='Задание №17'),
            types.InlineKeyboardButton('📄 Задание №22', callback_data='Задание №22'),
            types.InlineKeyboardButton('📄 Задание №23', callback_data='Задание №23'),
        ]

        row4 = [
            types.InlineKeyboardButton('📄 Задание №24', callback_data='Задание №24'),
            types.InlineKeyboardButton('📄 Задание №25', callback_data='Задание №25'),
            types.InlineKeyboardButton('📄 Задание №26', callback_data='Задание №26'),
            types.InlineKeyboardButton('📄 Задание №27', callback_data='Задание №27'),
        ]

        keyboard.add(*row1)
        keyboard.add(*row2)
        keyboard.add(*row3)
        keyboard.add(*row4)

        bot.send_message(call.message.chat.id, 'Выберите нужное задание:', reply_markup=keyboard)

    elif call.data == 'Задание №2':
        with open('photos/number2.png', 'rb') as photo_1:
            bot.send_photo(call.message.chat.id, photo_1)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 2:')

    elif call.data == 'Задание №6':
        with open('photos/number6.png', 'rb') as photo_2:
            bot.send_photo(call.message.chat.id, photo_2)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 6:')

    elif call.data == 'Задание №12':
        with open('photos/number12.png', 'rb') as photo_3:
            bot.send_photo(call.message.chat.id, photo_3)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 12:')

    elif call.data == 'Задание №14':
        with open('photos/number14.png', 'rb') as photo_4:
            bot.send_photo(call.message.chat.id, photo_4)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 14:')

    elif call.data == 'Задание №15':
        with open('photos/number15.png', 'rb') as photo_5:
            bot.send_photo(call.message.chat.id, photo_5)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 15:')

    elif call.data == 'Задание №16':
        with open('photos/number16.png', 'rb') as photo_6:
            bot.send_photo(call.message.chat.id, photo_6)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 16:')

    elif call.data == 'Задание №17':
        with open('photos/number17.png', 'rb') as photo_7:
            bot.send_photo(call.message.chat.id, photo_7)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 17:')

    elif call.data == 'Задание №22':
        with open('photos/number22.png', 'rb') as photo_8:
            bot.send_photo(call.message.chat.id, photo_8)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 22:')

    elif call.data == 'Задание №23':
        with open('photos/number23.png', 'rb') as photo_9:
            bot.send_photo(call.message.chat.id, photo_9)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 23:')

    elif call.data == 'Задание №24':
        with open('photos/number24.png', 'rb') as photo_10:
            bot.send_photo(call.message.chat.id, photo_10)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 24:')

    elif call.data == 'Задание №25':
        with open('photos/number25.png', 'rb') as photo_11:
            bot.send_photo(call.message.chat.id, photo_11)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 25:')

    elif call.data == 'Задание №26':
        with open('photos/number26.png', 'rb') as photo_12:
            bot.send_photo(call.message.chat.id, photo_12)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 26:')

    elif call.data == 'Задание №27':
        with open('photos/number27.png', 'rb') as photo_13:
            bot.send_photo(call.message.chat.id, photo_13)
        bot.send_message(call.message.chat.id, 'Пример кода для номера 27:')
    
    elif call.data == 'resources':
        resources_message = ('📚 Вот некоторые ресурсы для изучения Python и подготовки к ЕГЭ:\n'
                             '- Официальная документация: https://docs.python.org/3/\n'
                             '- Планета Информатики: https://inf1.info/\n'
                             '- Приложение CodeBase: https://www.rustore.ru/catalog/app/com.avelycure.whoareyoumobile.developer\n'
                             '- Информатикс: https://informatics.msk.ru/')
        bot.send_message(call.message.chat.id, resources_message)

    elif call.data == 'why python':
        why_python = ("🤔 Почему именно Python?\n"
                      "1. Легкий в изучении и использовании: Python имеет простой и понятный синтаксис, что делает его доступным для начинающих.\n"
                      "2. Широкая область применения: используется в веб-разработке, автоматизации, анализе данных, искусственном интеллекте и других областях.\n"
                      "3. Легко понять: Программа может состоять всего лишь из одной строки.\n"
                      "4. Высокий спрос на рынке труда: навыки Python востребованы в различных областях.\n"
                      "5. Бесплатно: Python это бесплатная и открытая технология. Разработчики могут ее распространять, копировать и изменять.")
        bot.send_message(call.message.chat.id, why_python)

    elif call.data == 'download':
        download_python = ("⬇️ Скачивание программы Python:\n"
                           "Вы можете скачать последнюю версию Python с официального сайта: https://www.python.org/downloads/")
        bot.send_message(call.message.chat.id, download_python)

    elif call.data == 'practice':
        practice_message = ('💻 Вот несколько сайтов, где можно готовиться к ЕГЭ:\n'
                            '- Сайт Константина Полякова: https://kpolyakov.spb.ru/school/ege.htm\n'
                            '- Сдам ЕГЭ: https://ege.sdamgia.ru/\n'
                            '- КЕГЭ: https://kompege.ru/')
        bot.send_message(call.message.chat.id, practice_message)

    elif call.data == 'daily_task':
        daily_task(call.message)

    elif call.data == 'special_topics':
        reply_keyboard = types.ReplyKeyboardMarkup(True, True)
        reply_keyboard.add(types.KeyboardButton('🔤 Работа со строками'))
        reply_keyboard.add(types.KeyboardButton('📊 Списки и массивы'))
        reply_keyboard.add(types.KeyboardButton('⚖ Условные конструкции'))
        reply_keyboard.add(types.KeyboardButton('🔄 Циклы и итерации'))
        reply_keyboard.add(types.KeyboardButton('🔧 Функции'))

        bot.send_message(call.message.chat.id, 'Выберите тему для изучения:', reply_markup=reply_keyboard)

    elif call.data == 'feedback':
        bot.send_message(call.message.chat.id, "✉️ Пожалуйста, напишите вашу жалобу или предложение:")
        bot.register_next_step_handler(call.message, handle_complaint)

    

@bot.message_handler(func=lambda message: message.text == '🔤 Работа со строками')
def string_operations(message):
    bot.send_message(message.chat.id, 'Работа со строками включает операции, такие как:\n'
                                       '- Извлечение подстрок. Статья: https://www.geeksforgeeks.org/extract-substrings-from-a-list-into-a-list-in-python/\n'
                                       '- Конкатенация строк. Статья: https://timeweb.com/ru/community/articles/konkatenaciya-strok-python\n'
                                       '- Сравнение строк. Статья: https://pythonist.ru/sravnenie-strok-v-python/\n'
                                       '- Изменение регистра. Статья: https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/\n'
                                       '❗ Это основа работы с текстовыми данными в Python.')


@bot.message_handler(func=lambda message: message.text == '📊 Списки и массивы')
def list_operations(message):
    bot.send_message(message.chat.id, 'Списки и массивы в Python позволяют хранить коллекции объектов:\n'
                                       '- Создание списков. Статья: https://skillbox.ru/media/code/spiski-v-python-chto-eto-takoe-i-kak-s-nimi-rabotat/\n'
                                       '- Добавление и удаление элементов. Статья: https://habr.com/ru/articles/319876/\n'
                                       '- Индексация. Статья: https://habr.com/ru/articles/811247/\n'
                                       '- Сортировка и фильтрация. Статья: https://stackoverflow.com/questions/72450566/how-to-sort-and-filter-a-list-in-python\n'
                                       '📈 Использование списков позволяет эффективно обрабатывать данные.')

@bot.message_handler(func=lambda message: message.text == '⚖ Условные конструкции')
def conditional_statements(message):
    bot.send_message(message.chat.id, 'Условные конструкции позволяют реализовывать логику в программах:\n'
                                       '- Использование if, elif, else. Статья: https://education.yandex.ru/handbook/python/article/uslovnyy-operator\n'
                                       '- Вложенные условия. Статья: https://skillbox.ru/media/code/uslovnye-operatory-v-python-ot-prostykh-esli-do-vlozhennykh-konstruktsiy/\n'
                                       '- Тернарные операторы. Статья: https://pythonturbo.ru/ternarnyj-operator-v-python/\n'
                                       '🔄 Эти конструкции помогают управлять потоком выполнения программ.')

@bot.message_handler(func=lambda message: message.text == '🔄 Циклы и итерации')
def loops_and_iterations(message):
    bot.send_message(message.chat.id, 'Циклы в Python позволяют повторять действия:\n'
                                       '- Цикл for: для перебора коллекций. Статья: https://habr.com/ru/companies/vdsina/articles/560916/\n'
                                       '- Цикл while: для повторения до выполнения условия. Статья: https://timeweb.cloud/tutorials/python/cikl-while-v-python-rukovodstvo\n'
                                       '🔄 Циклы удобны для обработки больших объемов данных.')

@bot.message_handler(func=lambda message: message.text == '🔧 Функции')
def functions(message):
    bot.send_message(message.chat.id, 'Функции в Python помогают организовать код:\n'
                                       '- Определение и вызов функций. Статья: https://skillbox.ru/media/code/funktsii-v-python-dlya-chego-oni-nuzhny-i-kak-s-nimi-rabotat/\n'
                                       '- Параметры и возвращаемые значения. Статья: https://pythonchik.ru/osnovy/funkcii-v-python\n'
                                       '- Лямбда-функции. Статья: https://habr.com/ru/companies/piter/articles/674234/\n'
                                       '🔧 Функции содействуют структурированию кода и уменьшению его дублирования.')


@bot.message_handler(commands=['resources'])
def resources(message):
    resources_message = ('📚 Вот некоторые ресурсы для изучения Python и подготовки к ЕГЭ:\n'
                         '- Официальная документация: https://docs.python.org/3/\n'
                         '- Планета Информатики: https://inf1.info/\n'
                         '- Приложение CodeBase: https://www.rustore.ru/catalog/app/com.avelycure.whoareyoumobile.developer\n'
                         '- Информатикс: https://informatics.msk.ru/')
    bot.send_message(message.chat.id, resources_message)

@bot.message_handler(commands=['practice'])
def practice(message):
    practice_message = ('💻 Вот несколько сайтов, где можно готовиться к ЕГЭ:\n'
                        '- Сайт Константина Полякова: https://kpolyakov.spb.ru/school/ege.htm\n'
                        '- Сдам ЕГЭ: https://ege.sdamgia.ru/\n'
                        '- КЕГЭ: https://kompege.ru/')
    bot.send_message(message.chat.id, practice_message)

@bot.message_handler(commands=['daily_task'])
def daily_task(message):
    tasks = [
        '📝 Задание №2. Построение таблиц истинности логических выражений.',
        '📝 Задание №6. Анализ программ.',
        '📝 Задание №12. Выполнение алгоритмов для исполнителей.',
        '📝 Задание №14. Системы счисления.',
        '📝 Задание №15. Преобразование логических выражений.',
        '📝 Задание №16. Рекурсивные алгоритмы.',
        '📝 Задание №17. Проверка на делимость.',
        '📝 Задание №22. Анализ программ с циклом и условными операторами.',
        '📝 Задание №23. Оператор присваивания и ветвления. Перебор вариантов, построение дерева.',
        '📝 Задание №24. Обработка символьных строк.',
        '📝 Задание №25. Обработка целочисленной информации.',
        '📝 Задание №26. Сортировка.',
        '📝 Задание №27. Анализ числовых последовательностей.',
        '🎉 Сегодня можно отдохнуть:)'
    ]
    task = random.choice(tasks)
    bot.send_message(message.chat.id, f'Ваше задание на сегодня: {task}')

@bot.message_handler(func=lambda message: message.text == '💡 О Python')
def conditional_statements(message):
    bot.send_message(message.chat.id, '🐍 Python — это высокоуровневый язык программирования, '
                                       'известный своей простотой и читаемостью. '
                                       'Он активно используется в веб-разработке, тестировании, '
                                       'машинном обучении и Data Science.\n'
                                       '🔗 Дополнительную информацию можно найти на официальном сайте: https://www.python.org/')
    
@bot.message_handler(func=lambda message: message.text == '📖 Рекомендации о учебе')
def conditional_statements(message):
    bot.send_message(message.chat.id, 'Вот несколько советов по изучению Python:\n'
                                       '1. 📚 Если Вы в 10 классе, изучайте постепенно, но если в 11, '
                                       'занимайтесь каждый день (минимум час).\n'
                                       '2. 🌐 Используйте полезные сайты для подготовки.\n'
                                       '3. ❗ Постарайтесь не заучивать шаблоны, а вникнуть в суть задач.\n'
                                       '4. 🤝 Не стесняйтесь обращаться к своему учителю за помощью!')

@bot.message_handler(func=lambda message: message.text == '👤 Создатель')
def the_creator(message):
    bot.send_message(message.chat.id, '👋 Всем привет!\n'
                                       'Я Зубаиров Рамис, ученик 10 класса. Обучаюсь в физ-мат классе.\n'
                                       '🛠 Я создал этого телеграм бота для более удобной подготовки к ЕГЭ.\n'
                                       'Тут можно найти много материала для подготовки.\n'
                                       '📅 В будущем планируется: Расширение функций и улучшение взаимодействия с пользователем')

    
@bot.message_handler(commands=['why python'])
def why_python(message):
    resources_message = ("Почему именно Python?\n"
        "1. Легкий в изучении и использовании: Python имеет простой и понятный синтаксис, что делает его доступным для начинающих.\n"
        "2. Широкая область применения: используется в веб-разработке, автоматизации, анализе данных, искусственном интеллекте и других областях.\n"
        "3. Легко понять: Программа может состоять всего лишь из одной строки.\n"
        "4. Высокий спрос на рынке труда: навыки Python востребованы в различных областях.\n"
        "5. Бесплатно: Python это бесплатная и открытая технология. Разработчики могут ее распространять, копировать и изменять.")
    bot.send_message(message.chat.id, resources_message)

@bot.message_handler(commands=['download'])
def load_python(message):
    download_python = ("Скачивание программы Python:\n"
        "Вы можете скачать последнюю версию Python с официального сайта: https://www.python.org/downloads/")
    bot.send_message(message.chat.id, download_python)



@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'listhigh':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('🎓 220+', callback_data='220ballov'))
        keyboard.add(types.InlineKeyboardButton('🎓 270+', callback_data='270ballov'))
        keyboard.add(types.InlineKeyboardButton('🎓 290+', callback_data='290ballov'))

        bot.send_message(call.message.chat.id, 'Если что, это списки вузов, куда можно поступить на бюджет с такими баллами ПО НАПРАВЛЕНИЮ IT. Укажите сколько баллов у Вас за ЕГЭ:', reply_markup=keyboard)

    

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'examples':
        keyboard = types.InlineKeyboardMarkup()

        row1 = [
            types.InlineKeyboardButton('📄 Задание №2', callback_data='Задание №2'),
            types.InlineKeyboardButton('📄 Задание №6', callback_data='Задание №6'),
            types.InlineKeyboardButton('📄 Задание №12', callback_data='Задание №12'),
        ]

        row2 = [
            types.InlineKeyboardButton('📄 Задание №14', callback_data='Задание №14'),
            types.InlineKeyboardButton('📄 Задание №15', callback_data='Задание №15'),
            types.InlineKeyboardButton('📄 Задание №16', callback_data='Задание №16'),
        ]

        row3 = [
            types.InlineKeyboardButton('📄 Задание №17', callback_data='Задание №17'),
            types.InlineKeyboardButton('📄 Задание №22', callback_data='Задание №22'),
            types.InlineKeyboardButton('📄 Задание №23', callback_data='Задание №23'),
        ]

        row4 = [
            types.InlineKeyboardButton('📄 Задание №24', callback_data='Задание №24'),
            types.InlineKeyboardButton('📄 Задание №25', callback_data='Задание №25'),
            types.InlineKeyboardButton('📄 Задание №26', callback_data='Задание №26'),
            types.InlineKeyboardButton('📄 Задание №27', callback_data='Задание №27'),
        ]

        keyboard.add(*row1)
        keyboard.add(*row2)
        keyboard.add(*row3)
        keyboard.add(*row4)

        bot.send_message(call.message.chat.id, 'Выберите нужное задание:', reply_markup=keyboard)

questions = [
    {
        'image_path': 'photos/number2_2.PNG',  
        'options': ['dbca', 'bcda', 'abcd', 'dbac'],
        'answer': 'dbca'
    },
    {
        'image_path': 'photos/number6_6.PNG',
        'options': ['56', '160', '120', '80'],
        'answer': '120'
    },
    {
        'image_path': 'photos/number12_12.PNG',
        'options': ['8', '9', '12', '5'],
        'answer': '9'
    },
    {
        'image_path': 'photos/number14_14.PNG',
        'options': ['11', '8', '20', '10'],
        'answer': '10'
    },
    {
        'image_path': 'photos/number15_15.PNG',
        'options': ['22', '8', '19', '17'],
        'answer': '19'  
    },
    {
        'image_path': 'photos/number16_16.PNG',
        'options': ['4094550', '4082612', '4058365', '4184965'],
        'answer': '4094550'  
    },
    {
        'image_path': 'photos/number17_17.PNG',
        'text_file_path': 'texts/17_17873.txt',
        'options': ['1213 176024', '1214 176024', '1211 166024', '1264 166024'],
        'answer': '1214 176024' 
    },
    {
        'image_path': 'photos/number22_22.PNG',
        'text_file_path': 'texts/22_17876.xls',
        'options': ['5', '6', '8', '3'],
        'answer': '5' 
    },
    {
        'image_path': 'photos/number23_23.PNG',
        'options': ['34', '28', '48', '36'],
        'answer': '36' 
    },
    {
        'image_path': 'photos/number24_24.PNG',
        'text_file_path': 'texts/24_17878.txt',
        'options': ['154', '146', '138', '153'],
        'answer': '154' 
    },
    {
        'image_path': 'photos/number25_25.PNG',
        'options': ['351261495 183235\n'
                    '3212614035 1675855\n'
                    '3412614645 1780185\n'
                    '3712414275 1936575\n'
                    '3912414885 2040905',
                    '351361495 183235\n'
                    '3211614035 1675855\n'
                    '3412614645 1780185\n'
                    '3712414275 1936575\n'
                    '3912414885 2040905',
                    '351571495 183235\n'
                    '3212614035 1675855\n'
                    '3412614645 1780185\n'
                    '3712414275 1936575\n'
                    '3912414885 2040905',
                    '351261495 183235\n'
                    '3212614035 1675855\n'
                    '3412114645 1780185\n'
                    '3712414275 1936575\n'
                    '3912414885 2040905'],
        'answer': '351261495 183235\n'
                    '3212614035 1675855\n'
                    '3412614645 1780185\n'
                    '3712414275 1936575\n'
                    '3912414885 2040905'
    },
    {
        'image_path': 'photos/number26_26.PNG',
        'text_file_path': 'texts/26_17881.txt',
        'options': ['52356 635', '12356 635', '52326 635', '54356 635'],
        'answer': '52326 635' 
    },
    {
        'image_path': 'photos/number27_27.PNG',
    'text_file_path': [
        'texts/27_A_17882.txt',
        'texts/27_B_17882.txt',
        'texts/27_A_17882.xlsx',
        'texts/27_B_17882.xlsx'
    ],
    'options': [
        '10738 30730\n'
        '37522 51277',
        '10438 30130\n'
        '37524 51577',
        '10738 30730\n'
        '37522 51277',
        '10731 30630\n'
        '37522 51277'
    ],
    'answer': '10738 30730\n'
              '37522 51277'



    }
]

current_question = 0

def send_message(chat_id, text, reply_markup=None):
    bot.send_message(chat_id, text, reply_markup=reply_markup)

def send_photo(chat_id, photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo)

def send_document(chat_id, document_path):
    with open(document_path, 'rb') as document:
        bot.send_document(chat_id, document)

@bot.message_handler(commands=['quiz'])
def start_quiz(message):
    global current_question
    current_question = 0
    send_message(message.chat.id, "🎉 Добро пожаловать в квиз 'Python для ЕГЭ по информатике'! Отвечайте на вопросы, выбирая один из вариантов.")
    send_question(message.chat.id)

def send_question(chat_id):
    global current_question
    if current_question < len(questions):
        question = questions[current_question]
        send_photo(chat_id, question['image_path'])
        if 'text_file_path' in question:
            if isinstance(question['text_file_path'], list):
                for text_file_path in question['text_file_path']:
                    if os.path.exists(text_file_path):
                        send_document(chat_id, text_file_path)
            else:
                if os.path.exists(question['text_file_path']):
                    send_document(chat_id, question['text_file_path'])

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for option in question['options']:
            markup.add(option)
        send_message(chat_id, "🤔 Выберите ответ:", reply_markup=markup)
    else:
        send_message(chat_id, "🏁 Квиз завершен! Ты мегахорош, продолжай в том же духе:), нажимай /start, чтоб выбрать другую опцию!")
        current_question = 0


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    global current_question
    question = questions[current_question]
    if message.text in question['options']:
        if message.text == question['answer']:
            send_message(message.chat.id, "✅ Правильно!")
            current_question += 1
            send_question(message.chat.id)
        else:
            send_message(message.chat.id, "❌ Неправильно!")
            send_question(message.chat.id)
    else:
        send_message(message.chat.id, "❓ Я не знаю такой функции, нажмите /start!")


feedback_file_path = 'feedback.txt'

def handle_complaint(message):
    if message.text:
        with open(feedback_file_path, 'a', encoding='utf-8') as file:
            file.write(f"{message.from_user.username}: {message.text}\n")
        send_message(message.chat.id, "🙏 Спасибо за вашу жалобу/предложение! Мы рассмотрим его в ближайшее время.")
    else:
        send_message(message.chat.id, "❗ Пожалуйста, введите текст вашей жалобы или предложения.")




bot.polling(none_stop=True)