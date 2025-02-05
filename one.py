import telebot
from telebot import types
import config



bot=telebot.TeleBot(config.TOKEN)



CHANNELS = ['!!!!!!!!!!!!!!!!!!!!!!']


def is_subscribed(user_id):
    for channel in CHANNELS:
        try:
            status = bot.get_chat_member(channel, user_id)
            if status.status not in ['left', 'kicked']:
                return True
        except Exception as e:
            print(f'Ошибка при проверке подписки: {e}')
    return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
  


  keyboard = types.InlineKeyboardMarkup()
  sponsr = types.InlineKeyboardButton(text ='Подписаться', callback_data ='item')
  keyboard.add(sponsr) 


  photo = open('logo.jpg', 'rb')
  bot.send_photo(message.chat.id, photo, caption='Подписаться!!!', reply_markup=keyboard)
  

@bot.callback_query_handler(lambda c: c.data == 'item')
def send_message(callback_query):

    key = types.InlineKeyboardMarkup(row_width = 1)
    
    sponsr_one = types.InlineKeyboardButton(text ='Подписаться',url='!!!!!!!!!!!!!!!!!!!!', callback_data ='item1')
    sponsr_two = types.InlineKeyboardButton(text ='Подписаться',url='!!!!!!!!!!!!!!!!!!!',callback_data ='item2')
    #sponsr_theer = types.InlineKeyboardButton(text ='Подписаться',callback_data ='item3')
    #sponsr_five = types.InlineKeyboardButton(text ='Подписаться',callback_data ='item5')
    #sponsr_six = types.InlineKeyboardButton(text ='Подписаться',callback_data ='item6')
    #sponsr_seven = types.InlineKeyboardButton(text ='Подписаться',callback_data ='item7')
    #sponsr_eight = types.InlineKeyboardButton(text ='Подписаться',callback_data ='item8')
    heck_app = types.InlineKeyboardButton(text ='Я подписался(-ась)',callback_data ='item9')

    key.add(sponsr_one,sponsr_two,heck_app)#sponsr_theer,sponsr_four,sponsr_five,sponsr_six,sponsr_seven,sponsr_eight,heck_app#) 
    bot.send_message(callback_query.message.chat.id, "Подпишитесь на наших спонсоров!", reply_markup = key)
    
    message_id = callback_query.message.message_id 
    bot.delete_message(callback_query.message.chat.id, message_id)  


@bot.callback_query_handler(func=lambda call: True)
def check_subscription(callback_query):
    user_id = callback_query.from_user.id
    if is_subscribed(user_id):
        keyv = types.InlineKeyboardMarkup(row_width = 1)
        privat = types.InlineKeyboardButton(text ='Подписаться',url='!!!!!!!!!!!!!!!!!!!!!!',callback_data ='item0')
        keyv.add(privat)
        
        bot.answer_callback_query(callback_query.id, "Вы подписаны на все необходимые каналы!", show_alert=False)
        bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Приватный канал❤️", reply_markup=keyv)
        
    else:
        bot.answer_callback_query(callback_query.id, f"Вы не подписаны на все обязательные каналы. Пожалуйста, подпишитесь на следующие каналы: {', '.join(CHANNELS)}", show_alert=True)
  
 
if __name__=='__main__':

 bot.polling(non_stop=True)