from telethon import TelegramClient, events, Button
import subprocess
from random import choices, randint

try:
    subprocess.run("pip3 install postgresql postgresql-contrib", check=True, shell=True)
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")

api_id = "13740761"
api_hash = "4ce319a92c01fab2b02551af8d7f73a4"
bot_token = "7051519511:AAEf9oWi6U6MvY4k_sMa7lbW1f1m3ZBkV7U"

baqir = TelegramClient('repthon_session', api_id, api_hash).start(bot_token=bot_token)

@baqir.on(events.NewMessage(pattern='/start'))
async def repthon(event):
    keyboard = [[Button.inline('إنشاء قاعدة بيانات', b'repthon_postgres')]]
    await event.reply(
        f'''**اهلاً وسهلاً حبيبي {event.sender.first_name}،
‎لإنشاء قاعدة بيانات خاصة بسورس ريبثون قم بالضغط على زر إنشاء قاعدة بيانات**''',
        buttons=keyboard
    )

@baqir.on(events.CallbackQuery)
async def handle_callback(event):
    if event.data == b'repthon_postgres':
        OHussein = ''.join(choices('abcdefghijklmnopqrstuvwxyz0123456789', k=randint(5, 10)))
        await event.respond('**᯽︙ انتظرني أسوي لك قاعدة بيانات لعيونك**')

        create_user_repthon = f'sudo su - postgres -c "psql -c \\"CREATE USER repthon{OHussein} WITH PASSWORD \'repthon{OHussein}\';\\""'
        create_db_repthon = f'sudo su - postgres bash -c "createdb repthon{OHussein} -O repthon{OHussein}"'

        create_user_process = subprocess.Popen(create_user_repthon, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        user_res, user_err = create_user_process.communicate()

        if 'CREATE ROLE' in user_res.decode():
            create_db_process = subprocess.Popen(create_db_repthon, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            db_res, db_err = create_db_process.communicate()

            if not db_err:
                await event.respond(f'''**وهاي قاعدة البيانات وتدلل علينا : `postgresql://repthon{OHussein}:repthon{OHussein}@localhost:5432/repthon{OHussein}`**''')
            else:
                await event.respond(f'حدث خطأ أثناء إنشاء قاعدة البيانات:\n{db_err.decode()}')
        else:
            await event.respond(f'حدث خطأ أثناء إنشاء المستخدم:\n{user_err.decode()}')

print("البوت يشتغل استمتع ...")
baqir.run_until_disconnected()
