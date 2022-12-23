import time
import json
import telebot

##TOKEN DETAILS
TOKEN = "ONS"

BOT_TOKEN = "5989686791:AAE49Nzp_HfGEgi84ac36NMQ2k8IBxWtW-8"
OWNER_ID = 5458705482 #write owner's user id here.. get it from @MissRose_Bot by /id
CHANNELS = ["@ONSBAseE"] #add channels to be checked here in the format - ["Channel 1", "Channel 2"] 
RATE_CHANNEL = "@onsbasee" #you can add as many channels here and also add the '@' sign before channel username
MENFES_CHANNEL = "@menfesonsbase"
Daily_bonus = 50 #Put daily bonus amount here!
Mini_Withdraw = 1000  #remove 0 and add the minimum withdraw u want to set
Per_Refer = 50 #add per refer bonus here
Daily_bonuss = 1000000000000
ROLEL = 5000
COSTT = 5
COST = 25

bot = telebot.TeleBot(BOT_TOKEN)



def check(id):
    for i in CHANNELS:
        check = bot.get_chat_member(i, id)
        if check.status != 'left':
            pass
        else:
            return False
    return True
bonus = {}

def menu(id):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('🆔 Account','👑 Set Role')
    keyboard.row('📸 Rated', '🎁 Bonus', '💸 Withdraw')
    keyboard.row('👩‍❤️‍💋‍👨 Promote', '💬 Menfes', '🙌🏻 Referrals')
    bot.send_message(id, "*🏡 Home*", parse_mode="Markdown",
                     reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start(message):
   try:
    user = message.chat.id
    msg = message.text
    if msg == '/start':
        user = str(user)
        data = json.load(open('users.json', 'r'))
        if user not in data['referred']:
            data['referred'][user] = 0
            data['total'] = data['total'] + 1
        if user not in data['referby']:
            data['referby'][user] = user
        if user not in data['checkin']:
            data['checkin'][user] = 0
        if user not in data['DailyQuiz']:
            data['DailyQuiz'][user] = "0"
        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['wallet']:
            data['wallet'][user] = "none"
        if user not in data['withd']:
            data['withd'][user] = 0
        if user not in data['id']:
            data['id'][user] = data['total']+1
        json.dump(data, open('users.json', 'w'))
        print(data)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(
           text='🤼‍♂️ Joined', callback_data='check'))
        msg_start = "*🍔 To Use This Bot You Need To Join This Channel - "
        for i in CHANNELS, MENFES_CHANNEL, "@ratemyonspartner":
            msg_start += f"\n➡️ {i}\n"
        msg_start += "*"
        bot.send_message(user, msg_start,
                         parse_mode="Markdown", reply_markup=markup)
    else:

        data = json.load(open('users.json', 'r'))
        user = message.chat.id
        user = str(user)
        refid = message.text.split()[1]
        if user not in data['referred']:
            data['referred'][user] = 0
            data['total'] = data['total'] + 1
        if user not in data['referby']:
            data['referby'][user] = refid
        if user not in data['checkin']:
            data['checkin'][user] = 0
        if user not in data['DailyQuiz']:
            data['DailyQuiz'][user] = 0
        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['wallet']:
            data['wallet'][user] = "none"
        if user not in data['withd']:
            data['withd'][user] = 0
        if user not in data['id']:
            data['id'][user] = data['total']+1
        json.dump(data, open('users.json', 'w'))
        print(data)
        markups = telebot.types.InlineKeyboardMarkup()
        markups.add(telebot.types.InlineKeyboardButton(
            text='🤼‍♂️ Joined', callback_data='check'))
        msg_start = "*🍔 To Use This Bot You Need To Join This Channel - \n➡️ @ Fill your channels at line: 101 and 157*"
        bot.send_message(user, msg_start,
                         parse_mode="Markdown", reply_markup=markups)
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
   try:
    ch = check(call.message.chat.id)
    if call.data == 'check':
        if ch == True:
            data = json.load(open('users.json', 'r'))
            user_id = call.message.chat.id
            user = str(user_id)
            bot.answer_callback_query(
                callback_query_id=call.id, text='✅ Wellcome to One Night Stand BASE')
            bot.delete_message(call.message.chat.id, call.message.message_id)
            if user not in data['refer']:
                data['refer'][user] = True

                if user not in data['referby']:
                    data['referby'][user] = user
                    json.dump(data, open('users.json', 'w'))
                if int(data['referby'][user]) != user_id:
                    ref_id = data['referby'][user]
                    ref = str(ref_id)
                    if ref not in data['balance']:
                        data['balance'][ref] = 0
                    if ref not in data['referred']:
                        data['referred'][ref] = 0
                    json.dump(data, open('users.json', 'w'))
                    data['balance'][ref] += Per_Refer
                    data['referred'][ref] += 1
                    bot.send_message(
                        ref_id, f"*🏧 New Referral on Level 1, You Got : +{Per_Refer} {TOKEN}*", parse_mode="Markdown")
                    json.dump(data, open('users.json', 'w'))
                    return menu(call.message.chat.id)

                else:
                    json.dump(data, open('users.json', 'w'))
                    return menu(call.message.chat.id)

            else:
                json.dump(data, open('users.json', 'w'))
                menu(call.message.chat.id)

        else:
            bot.answer_callback_query(
                _query_id=callbackcall.id, text='❌ You not Joined')
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(
                text='🤼‍♂️ Joined', callback_data='check'))
            msg_start = "*🍔 To Use This Bot You Need To Join This Channel - \n➡️ @ Fill your channels at line: 101 and 157*"
            bot.send_message(call.message.chat.id, msg_start,
                             parse_mode="Markdown", reply_markup=markup)
   except:
        bot.send_message(call.message.chat.id, "You must join channel the first")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+call.data)
        return

@bot.message_handler(commands=['getcoin'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/getcoin':
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        #bot.send_message(user_id, "*🎁 Bonus Button is Under Maintainance*", parse_mode="Markdown")
        if (user_id == OWNER_ID):
            data['balance'][(user)] += Daily_bonuss
            bot.send_message(
                user_id, "Congrats you just received 1000000000000 ONS")
            json.dump(data, open('users.json', 'w'))
        else:
            bot.send_message(
                message.chat.id, "❌*You not admin!*",parse_mode="markdown")
        return menu(message.chat.id)
        
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and tezt /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return
@bot.message_handler(commands=['topup'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/topup':
        user_id = message.chat.id
        user = str(user_id)

        bot.send_message(
                user_id, "*ONS coin di gunakan semua transaksi yang ada di @onsbasebot, seperti kirim menfes di @onsbasse dan @onsbasemenfes, mengatur role dan transfer coin ons ke sesama user @onsbasebot.\n\n💱 Cara Membeli Coin ONS dengan automatis\n1. klik https://trakteer.id/nazhak-tv-dfbf2/post/ons-base-PzPVa\n2. nama: (masukan nama kalian)\n├masukan id telegram (pesan dukungan)\n3. masukan nilai top up kalian (pesan dukungan)\nTunggu beberapa saat hingga admin cek transaksi kalian\n\n💱Cara membeli ONS coin secara manual bisa langsung hubungi @lolot0, pembayaran via dana/ovo/gopay/s-pay/qris.*")
        
        return menu(message.chat.id)
        
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and tezt /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.message_handler(commands=['readme'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/readme':
        user_id = message.chat.id
        user = str(user_id)

        bot.send_message(
                user_id, "👐!Selamat datang di One Night Stand!👐\n\n❓ Apa itu One Night Stand ❓\nOne Night Stand dibagi menjadi :\n\n• @onsbasse adalah lapak promote untuk mencari pasangan, teman, Partner dengan kalimat. Kirim pesan promote difitur promote anda di @onsbasebot.\n\n• @onsbasemenfes adalah lapak menfes untuk sekedar melampiaskan keluh kesah sender dengan kalimat tanpa mengunakan '@'. Kirim pesan promote difitur menfes anda di @onsbasebot.\n\n• @ratemyonspartner adalah lapak untuk mengirim foto atau video apapun untuk di nilai oleh user bot lainnya. Kirim pesan promote difitur rated di @onsbasebot.\n\nOne Night Stand menyediakan fitur account untuk melihat status user. Cek di @onsbasebot\n\nOne Night Stand menyediakan fitur set role, user bisa mengunakan fitur itu untuk menambah role, dengan ini user diharapkan untuk tidak mengunakan kalimat dengan hastag dikarenakan kalimat user terhubung automatis dengan  role yang menjadi hastag. cek di @onsbasebot\n\nOne Night Stand juga menyediakan fitur withdraw untuk transfer coin ONS kesesama penguna @onsbasebot\n\n❗️PERINGATAN❗️\n\nHANYA UNTUK USER @onsbasebot\n\nHANYA MENGIRIM 1000 ONS/TF\n\nOne Night Stand tak lupa menyediakan fitur bonus untuk user dapat claim 50 ONS Coin per hari. Cek di @onsbasebot.\n\n💳 Terms and Conditions :\n• Dengan bergabung & menggunakan layanan di @onsbasebot, pengguna menyetujui semua persyaratan kami.\n• Dengan bergabung & menggunakan layanan di @onsbasebot, pengguna menyetujui semua persyaratan kami.\n• Kami tidak bertanggung jawab atas segala jenis masalah setelah pengguna menggunakan layanan kami.\n• Kami tidak bertanggung jawab atas segala jenis masalah setelah pengguna menggunakan layanan kami.• Kami hanya dapat melayani laporan pengguna jika ada masalah saat pengguna tidak dapat mengirim pesan di bot, tidak dapat bergabung dengan channel / grup, atau pengguna dibanned dari BOT & Channel dll.\n\n🔞 Terima kasih telah meluangkan waktu untuk membaca pesan ini, jika ada hal lain yang ingin ditanyakan bisa mendiskusikannya di @onsbase_grub.\n\n\nBest Regards,\n@lolot0")

        return menu(message.chat.id)
        
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.message_handler(commands=['rules'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/rules':
        user_id = message.chat.id
        user = str(user_id)

        bot.send_message(
                user_id, "📖 RULES One Night Stand\n\n1. DILARANG SARA / RUSUH / SPAM\n2. DILARANG Mengemis { mengirim link refferal }\n3. DILARANG PROMOSI LINK GROUP / LPM / BOT LAIN\n\n— MELANGGAR = AUTO BANNED —\n\nPengaduan bisa disampaikan kepada @lolot0 dan team\n\nBest Regards,\n@lolot0")

        return menu(message.chat.id)
        
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.message_handler(content_types=['text'])
def send_text(message):
   try:
    if message.text == '🆔 Account':
        data = json.load(open('users.json', 'r'))
        accmsg = '*👮 User : {}\n\n🆔 ID : {}\n\n👑 Role : *`{}`*\n\n💸 Balance : *`{}`* {}*'
        user_id = message.chat.id
        user = str(user_id)
        ID = int(user_id)

        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['wallet']:
            data['wallet'][user] = "none"

        json.dump(data, open('users.json', 'w'))

        balance = data['balance'][user]
        wallet = data['wallet'][user]
        msg = accmsg.format(message.from_user.first_name, user,
                            wallet, balance, TOKEN)
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")

    if message.text == '🙌🏻 Referrals':
        data = json.load(open('users.json', 'r'))
        ref_msg = "*⏯️ Total Invites : {} Users\n\n👥 Refferrals System\n\n1 Level:\n🥇 Level°1 - {} {}\n\n🔗 Referral Link ⬇️\n{}*"

        bot_name = bot.get_me().username
        user_id = message.chat.id
        user = str(user_id)

        if user not in data['referred']:
            data['referred'][user] = 0
        json.dump(data, open('users.json', 'w'))

        ref_count = data['referred'][user]
        ref_link = 'https://telegram.me/{}?start={}'.format(
            bot_name, message.chat.id)
        msg = ref_msg.format(ref_count, Per_Refer, TOKEN, ref_link)
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")

    if message.text == "👑 Set Role":
        user_id = message.chat.id
        user = str(user_id)

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('🚫 Cancel')
        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 0
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        if bal >= ROLEL:
            bot.send_message(user_id, "_⚠️Set your role._",
                             parse_mode="Markdown", reply_markup=keyboard)
            bot.register_next_step_handler(message, lol_address)
        else:
            bot.send_message(
                user_id, f"_❌Your balance low you should have at least {ROLEL} {TOKEN} to Withdraw_", parse_mode="Markdown")
            return menu(message.chat.id)

    if message.text == "📸 Rated":
        user_id = message.chat.id
        user = str(user_id)

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('🚫 Cancel')
        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 0
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        if bal >= 0:
            bot.send_message(user_id, "_🤪Send photo or video with caption, if you want it +your role😜_",
                             parse_mode="Markdown", reply_markup=keyboard)
            bot.register_next_step_handler(message, meki_luko)
        else:
            bot.send_message(
                user_id, f"_❌Your balance low you should have at least {0} {TOKEN} to Withdraw_", parse_mode="Markdown")
            return menu(message.chat.id)
        
    if message.text == "🎁 Bonus":
        user_id = message.chat.id
        user = str(user_id)
        cur_time = int((time.time()))
        data = json.load(open('users.json', 'r'))
        #bot.send_message(user_id, "*🎁 Bonus Button is Under Maintainance*", parse_mode="Markdown")
        if (user_id not in bonus.keys()) or (cur_time - bonus[user_id] > 60*60*24):
            data['balance'][(user)] += Daily_bonus
            bot.send_message(
                user_id, f"Congrats you just received {Daily_bonus} {TOKEN}")
            bonus[user_id] = cur_time
            json.dump(data, open('users.json', 'w'))
        else:
            bot.send_message(
                message.chat.id, "❌*You can only take bonus once every 24 hours!*",parse_mode="markdown")
        return

    if message.text == "💬 Menfes":
        user_id = message.chat.id
        user = str(user_id)

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('🚫 Cancel')
        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 0
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        if bal >= COSTT:
            bot.send_message(user_id, "_Sent Your Text_",
                             parse_mode="Markdown", reply_markup=keyboard)
            bot.register_next_step_handler(message, lalo_push)
        else:
            bot.send_message(
                user_id, f"_❌Your balance low you should have at least {COSTT} {TOKEN} to send message_", parse_mode="Markdown")
            return menu(message.chat.id)

    if message.text == "👩‍❤️‍💋‍👨 Promote":
        user_id = message.chat.id
        user = str(user_id)

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('🚫 Cancel')
        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 0
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        if bal >= COST:
            bot.send_message(user_id, "_Sent Your Text_",
                             parse_mode="Markdown", reply_markup=keyboard)
            bot.register_next_step_handler(message, trx_amin)
        else:
            bot.send_message(
                user_id, f"_❌Your balance low you should have at least {COST} {TOKEN} to send message_", parse_mode="Markdown")
            return menu(message.chat.id)

    if message.text == "💸 Withdraw":
        user_id = message.chat.id
        user = str(user_id)

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('🚫 Cancel')

        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 0
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        if bal >= Mini_Withdraw:
            bot.send_message(user_id, "_Enter Your Amount Just Type 1000_",
                             parse_mode="Markdown", reply_markup=keyboard)
            bot.register_next_step_handler(message, amo_with)

        else:
            bot.send_message(
                user_id, f"_❌Your balance low you should have at least {Mini_Withdraw} {TOKEN} to Withdraw_", parse_mode="Markdown")
            return menu(message.chat.id)

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return menu(message.chat.id)


def trx_amin(message):
   try:
    if message.text == "🚫 Cancel":
        return menu(message.chat.id)
    if len(message.text) >= 9:
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        trx = message.text

        data['balance'][user] -= (COST)
        bot_name = bot.get_me().username
        json.dump(data, open('users.json', 'w'))

        bot.send_message(user_id, "✅ SENT!")
        
        send = bot.send_message(RATE_CHANNEL,  "#"+data['wallet'][user]+f" {trx}", parse_mode="Markdown")
        
        json.dump(data, open('users.json', 'w'))
        return menu(message.chat.id)
    else:
        bot.send_message(
            message.chat.id, "*⚠️ Yout Text Too Short!*", parse_mode="Markdown")
        return menu(message.chat.id)
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return
    

def amo_with(message):
   try:
    user_id = message.chat.id
    amo = message.text
    user = str(user_id)
    data = json.load(open('users.json', 'r'))
    if user not in data['balance']:
        data['balance'][user] = 0
    json.dump(data, open('users.json', 'w'))

    bal = data['balance'][user]
    msg = message.text
    if msg.isdigit() == False:
        bot.send_message(
            user_id, "_📛 Invaild value. Enter only numeric value. Try again_", parse_mode="Markdown")
        return menu(message.chat.id)
    if int(message.text) < Mini_Withdraw:
        bot.send_message(
            user_id, f"_❌ Minimum withdraw {Mini_Withdraw} {TOKEN}_", parse_mode="Markdown")
        return menu(message.chat.id)
    if int(message.text) > bal:
        bot.send_message(
            user_id, "_❌ You Can't withdraw More than Your Balance_", parse_mode="Markdown")
        return menu(message.chat.id)
        

    amo = int(amo) 
    data['balance'][user] -= int(amo)
    bot_name = bot.get_me().username
    json.dump(data, open('users.json', 'w'))
    bot.send_message(user_id, "_User Id_", parse_mode="Markdown")
    bot.register_next_step_handler(message, lero_susu)
    return

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

def meki_luko(message):
   try:
    if message.text == "🚫 Cancel":
        return menu(message.chat.id)
    if message:
        user_id = message.chat.id
        user = user_id
        bot.send_message(message.chat.id,"sent, wait for post")
        bot.forward_message(1941303148,message.chat.id,message.message_id)
        return menu(message.chat.id)

    else:
        bot.send_message(
            message.chat.id, "*⚠️Not gift!*", parse_mode="Markdown")
        return menu(message.chat.id)
   except:
        bot.send_message(message.chat.id, "This command having error pls text /start to restart bot")
        bot.send_photo(OWNER_ID, message.photo)
        return

def lalo_push(message):
   try:
    if message.text == "🚫 Cancel":
        return menu(message.chat.id)
    if len(message.text) >= 9:
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        lalo = message.text

        data['balance'][user] -= (COSTT)
        bot_name = bot.get_me().username
        json.dump(data, open('users.json', 'w'))

        bot.send_message(user_id, "✅ SENT!")
        
        send = bot.send_message(MENFES_CHANNEL,  "#"+data['wallet'][user]+f" {lalo}", parse_mode="Markdown")
        
        json.dump(data, open('users.json', 'w'))
        return menu(message.chat.id)
    else:
        bot.send_message(
            message.chat.id, "*⚠️ Yout Text Too Short!*", parse_mode="Markdown")
        return menu(message.chat.id)
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

def lero_susu(message):
   try:
    if len(message.text) >= 10:
        lero = message.text
        user_id = message.text
        user = str(user_id)
        data = json.load(open('users.json', 'r'))

        data['balance'][lero] += (Mini_Withdraw)
        bot_name = bot.get_me().username
        json.dump(data, open('users.json', 'w'))

        bot.send_message(user_id, "✅* Congrast!\n\n💹You get : 1000 ONS*", parse_mode="Markdown")
        json.dump(data, open('users.json', 'w'))
        return menu(message.chat.id)       
    else:
        bot.send_message(
            message.chat.id, "*⚠️ Username ID Not Found!*", parse_mode="Markdown")
        return menu(message.chat.id)
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return
    
def lol_address(message):
   try:
    if message.text == "🚫 Cancel":
        return menu(message.chat.id)
    if len(message.text) >= 3:
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        data['wallet'][user] = message.text

        data['balance'][user] -= (ROLEL)
        bot_name = bot.get_me().username
        json.dump(data, open('users.json', 'w'))

        bot.send_message(message.chat.id, "*💹Your role set to " +
                         data['wallet'][user]+"*", parse_mode="Markdown")
        json.dump(data, open('users.json', 'w'))
        return menu(message.chat.id)
    else:
        bot.send_message(
            message.chat.id, "*⚠️Your text too short!*", parse_mode="Markdown")
        return menu(message.chat.id)
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return



if __name__ == '__main__':
    bot.polling(none_stop=True)