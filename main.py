import telebot, re, cv2, os
from pytube import YouTube

bot = telebot.TeleBot('6796523964:AAHp6e12JcflNRI-o-C59Bu1DIIEsMZs0xw')

#@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #btn1 = types.KeyboardButton("👋 Прислать ссылку на видеофайл")
    #markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)
'''@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    if message.text == '👋 Прислать ссылку на видеофайл':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Как стать автором на Хабре?')
        btn2 = types.KeyboardButton('Правила сайта')
        btn3 = types.KeyboardButton('Советы по оформлению публикации')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Как стать автором на Хабре?':
        bot.send_message(message.from_user.id, 'Вы пишете первый пост, его проверяют модераторы, и, если всё хорошо, отправляют в основную ленту Хабра, где он набирает просмотры, комментарии и рейтинг. В дальнейшем премодерация уже не понадобится. Если с постом что-то не так, вас попросят его доработать.\n \nПолный текст можно прочитать по ' + '[ссылке](https://habr.com/ru/sandbox/start/)', parse_mode='Markdown')

    elif message.text == 'Правила сайта':
        bot.send_message(message.from_user.id, 'Прочитать правила сайта вы можете по ' + '[ссылке](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')

    elif message.text == 'Советы по оформлению публикации':
        bot.send_message(message.from_user.id, 'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](https://habr.com/ru/docs/companies/design/)', parse_mode='Markdown')

print(yt.streams.filter(file_extension='mp4'))
stream = yt.streams.get_by_itag(22)

'''

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if 'привет' in message.text.lower():
        bot.send_message(message.from_user.id,
                         "Привет, я могу скачать для тебя видео с ютуба, просто отправь мне ссылку")
    elif '/start' in message.text.lower():
        bot.send_message(message.from_user.id,
                         "Привет, я могу скачать для тебя видео с ютуба, просто отправь мне ссылку, или репост")

    elif 'https' in message.text.lower():
        links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
        #print('Link = ' + str(links))
        #link = 'https://www.youtube.com/watch?v=90KZnwrVMgY'
        for i in range(len(links)):
            yt = YouTube(links[i])
            print(f' {yt.title!r}: {message.text}')
            #streams = yt.streams.filter(progressive=True, file_extension='mp4', resolution='480p').order_by('resolution')
            #print(streams)
            video = yt.streams.get_by_itag(22)
            fname = str(message.from_user.id) + '.mp4'
            video.download(filename=fname)
            file = open(fname, 'rb')
            cap = cv2.VideoCapture(fname)
            _, frame = cap.read()
            h, w, _ = frame.shape
            cap.release()
            try:
                file_size = os.path.getsize(fname)
                if file_size < 49999900:
                    bot.send_message(message.from_user.id, "Готово! 👇")
                    bot.send_video(message.from_user.id, file, width=w, height=h)
                else: bot.send_document(message.from_user.id, file, width=w, height=h)
                #bot.send_video(message.from_user.id, file, width=w, height=h)
            except:
                bot.send_message(message.from_user.id, "Ошибка, попробуйте другое видео")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Привет.")
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
