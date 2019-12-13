import discord
from discord.ext import commands
from discord.utils import get
import config
import random
import sqlite3
import json

conn = sqlite3.connect("Discord.db") # или :memory:
cursor = conn.cursor()




bot = commands.Bot(command_prefix="")
bot.remove_command("help")
##################################################################Load##########################################################################
@bot.event
async def on_ready():
    print(r"""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ 
▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     
▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌     
▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░▌ ▐░▌       ▐░▌     ▐░▌     
▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀      ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌     ▐░▌     
▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌      ▐░▌      ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌     ▐░▌     
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀       ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀       ▀      
                                                                                                
    """)
    print(f"{bot.user.name} {bot.user.id}")
    
##################################################################Load##########################################################################
try:
    @bot.event
    async def on_member_join(member, message):
        role = get(member.guild.roles, name="Игрок")
        print(f"member {member} has joined to guild")
        await member.add_roles(role)
        await message.member.send(f"Hello, {member}")
        
except discord.errors.NotFound:
    print("[waring]error discord.errors.NotFound")

@bot.event
async def on_typing(channel, user, when):
    print(channel, user, when)






####################################################################################################################################
@bot.event
async def on_message(message):
    if message.channel == 630454759668580362:    
        if message.content == 'acc':
            await message.channel.send(f"Сравнение с базой данных... Если ответа не последует, пропишите reg")
            for row in cursor.execute(f"SELECT id FROM users WHERE id ={message.author.id}"):
                a = message.author.id
                b = row[0]
                if a == b:
                    await message.channel.send(f"|  id  |  nick  |  Money  |  Xp  |  lvl  |")
                    for row in cursor.execute(f"SELECT id,nickname,money,xp,lvl FROM users WHERE id ={message.author.id}"):
                        await message.channel.send(f"|  {row[0]}  |  {row[1]}  |  {row[2]}  |  {row[3]}  |  {row[4]}  |")

        if message.content == 'reg':
            cursor.execute(f"SELECT id FROM users where id ={message.author.id}")
            fin=cursor.fetchone()
            if fin == None:
                await message.channel.send(f"Регистрация...")
                cursor.execute(f"INSERT INTO users VALUES ({message.author.id}, '{message.author.name}', '<@{message.author.id}>', 50000, 'S','[]',0,0)")
                await message.channel.send(f"Вы успешно зарегестрированны. Ваш ник: {message.author.name}")
                cursor.execute(f"SELECT id FROM users where id ={message.author.id}")
                fin=cursor.fetchone()
            else:
                await message.channel.send(f"Вы уже зарегестрированны! Введите acc")
                cursor.execute(f"SELECT id FROM users where id ={message.author.id}")
                fin=cursor.fetchone()
        if message.content == 'DB':
            role = get(message.author.guild.roles, name="Bot Dev")
            if role in message.author.roles:
                await message.channel.send("|  id  |  nickname  |  mention  |  money  |  rep_rank  |") 
                for row in cursor.execute("SELECT * FROM users LIMIT 10"):
                    await message.channel.send(f"| {row[0]} | {row[1]} | mention.type | {row[3]} | {row[4]} |")
                await message.channel.send("...and more")
            else:
                await message.channel.send(f"{message.author.nick}, У вас нет доступа к комманде")
        if message.content == 'shop':
            cursor.execute(f"SELECT id FROM users where id ={message.author.id}")
            fin=cursor.fetchone()
            if fin == None:
                await message.channel.send(f"Вы не зарегестрированны. Введите комманду reg")
                cursor.execute(f"SELECT id FROM users where id ={message.author.id}")
                fin=cursor.fetchone()
            else:
                await message.channel.send("loading shop...")
                await message.channel.send(f"|  id  |  тип предмета  |  название  |  цена  |  ")
                for row in cursor.execute(f"SELECT * FROM shop"):
                    await message.channel.send(f"|  {row[0]}  |  {row[1]}  |  {row[2]}  |  {row[3]}  |")
                await message.channel.send(f"Для покупки Введите buy id")
        if message.content == "inv":
            await message.channel.send("loading Inventory...")
            await message.channel.send(f"тип  |  название")
            for row in cursor.execute(f"SELECT inventory FROM users where id={message.author.id}"):
                data=json.loads(row[0])
                for row in data:
                    prt=row
                    for row in cursor.execute(f"SELECT type,name FROM shop where id={prt}"):
                        await message.channel.send(f"{row[0]}  |  {row[1]}")
        if len(message.content) > 10:
            for row in cursor.execute(f"SELECT xp,lvl FROM users where id={message.author.id}"):
                print(row[0])
                expi=row[0]+random.randint(5, 40)
                print(expi)
                cursor.execute(f'UPDATE users SET xp={expi} where id={message.author.id}')
                lvch=expi/(row[1]*1000)
                print(lvch)
                print(int(lvch))
                lv=int(lvch)
                print(" ",row[1]," ",lvch," ",lv," ",row[0])
                if row[1] < lv:
                    await message.channel.send(f'Новый уровень!')
                    cursor.execute(f'UPDATE users SET lvl={lv} where id={message.author.id}')
        
        
        
    await bot.process_commands(message)
    conn.commit()





@bot.command()
async def buy(ctx, a: int):
    uid=ctx.author.id
    await ctx.send('Обработка... Если ответа не последует, значит нарушен синтаксис [buy {id}]')
    for row in cursor.execute(f"SELECT money FROM users where id={uid}"):
        money = row[0]
        for row in cursor.execute(f"SELECT id,name,cost FROM shop where id={a}"):
            cost=row[2]
            if money >= cost:
                money -=cost
                await ctx.send(f'Вы преобрели "{row[1]}" за {row[2]}')
                
                for row in cursor.execute(f"SELECT inventory FROM users where id={uid}"):
                    data=json.loads(row[0])
                    data.append(a)
                    daed=json.dumps(data)
                    cursor.execute('UPDATE users SET money=?,inventory = ? where id=?',(money,daed,uid))
                    pass
            if money < cost:
                await ctx.send(f'Недостаточно средств')
                pass
    conn.commit()
@bot.command()
async def help(ctx):
    await ctx.send('Обработка...')
    await ctx.send("""
● ● ● ● ● ● ● ● ● ● ● ● ● Основные ● ● ● ● ● ● ● ● ● ● ● ● ● 
[reg] - Регистрация игрока (Требуется 1 раз на всегда)
[acc] - Информация об аккаунте
[shop] - Список предметов для покупки и их стоимость
[inv] - Инвентарь игрока
[buy {id}] - Покупка вещей. Использование "buy 1"
● ● ● ● ● ● ● ● ● ● ● ● ● ● Debug ● ● ● ● ● ● ● ● ● ● ● ● ● ● 
[DB] - Debug информация об игроках из sqlite
    """)
@bot.command()
async def debug(ctx):
    await ctx.send(f'{ctx.author.id}')
####################################################################################################################################












bot.run(config.discord_token)


