# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module which contains afk-related commands """

from random import choice, randint
from asyncio import sleep

from telethon.events import StopPropagation

from userbot import (AFKREASON, COUNT_MSG, CMD_HELP, ISAFK, BOTLOG,
                     BOTLOG_CHATID, USERS, PM_AUTO_BAN)
from userbot.events import register

<<<<<<< HEAD
# ========================= CONSTANTS ============================
AFKSTR = [
    "I'm busy right now. Please talk in a bag and when I come back you can just give me the bag!",
    "I'm away right now. If you need anything, leave a message after the beep:\n`beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep`!",
    "You missed me, next time aim better.",
    "I'll be back in a few minutes and if I'm not...,\nwait longer.",
    "I'm not here right now, so I'm probably somewhere else.",
    "Roses are red,\nViolets are blue,\nLeave me a message,\nAnd I'll get back to you.",
    "Sometimes the best things in life are worth waiting for…\nI'll be right back.",
    "I'll be right back,\nbut if I'm not right back,\nI'll be back later.",
    "If you haven't figured it out already,\nI'm not here.",
    "Hello, welcome to my away message, how may I ignore you today?",
    "I'm away over 7 seas and 7 countries,\n7 waters and 7 continents,\n7 mountains and 7 hills,\n7 plains and 7 mounds,\n7 pools and 7 lakes,\n7 springs and 7 meadows,\n7 cities and 7 neighborhoods,\n7 blocks and 7 houses...\n\nWhere not even your messages can reach me!",
    "I'm away from the keyboard at the moment, but if you'll scream loud enough at your screen, I might just hear you.",
    "I went that way\n---->",
    "I went this way\n<----",
    "Please leave a message and make me feel even more important than I already am.",
    "I am not here so stop writing to me,\nor else you will find yourself with a screen full of your own messages.",
    "If I were here,\nI'd tell you where I am.\n\nBut I'm not,\nso ask me when I return...",
    "I am away!\nI don't know when I'll be back!\nHopefully a few minutes from now!",
    "I'm not available right now so please leave your name, number, and address and I will stalk you later.",
    "Sorry, I'm not here right now.\nFeel free to talk to my userbot as long as you like.\nI'll get back to you later.",
    "I bet you were expecting an away message!",
    "Life is so short, there are so many things to do...\nI'm away doing one of them..",
    "I am not here right now...\nbut if I was...\n\nwouldn't that be awesome?",
=======
try:
    from userbot.modules.sql_helper.globals import gvarstatus, addgvar, delgvar
    afk_db = True
except AttributeError:
    afk_db = False

# ========================= CONSTANTS ============================
AFKSTR = [
    "Aktualnie mnie nie ma, ale niebawem wrócę. Wytrzymasz?",
    "Jestem bardzo daleko. Nagraj się po komunikacie:\n`beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep`!",
    "Wiem, że tęsknisz. Aktualnie mnie nie ma, ale niebawem wrócę!",
    "Wrócę za kilka minut, godzin, dni.\nJeśli nie...\npoczekaj dłużej!.",
    "Powiedz co chcesz,\nzostaw wieść.\n\nI może wrócę do Ciebie!",
    "Czasami na najlepsze rzeczy w życiu warto czekać…\nNiebawem się odezwę.",
    "Być, albo nie być - o to jest pytanie.\nMnie nie ma, więc znasz odpowiedź.",
    "Wielka tajemnica,\nNie ma mnie.",
    "Witaj, tutaj niby ja, ale nie ja. Jak mogę cię dzisiaj zignorować?",
    "Witaj, nie ma mnie.\nPogadaj sobie z moim userbotem tak długo jak masz na to ochotę.\nOdezwę się niebawem.",
    "Życie jest za krótkie, żeby cały czas tu przesiadywać...\nDozobaczenia",
>>>>>>> TelegramUserBot/master
]
# =================================================================


<<<<<<< HEAD
@register(incoming=True, disable_edited=True)
=======
@register(incoming=True, disable_errors=True)
>>>>>>> TelegramUserBot/master
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
<<<<<<< HEAD
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK:
            if mention.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply(f"I'm AFK right now.\
                        \nBecause I'm `{AFKREASON}`")
=======
    global AFFKREASON
    ISAFK_SQL = False
    AFKREASON_SQL = None
    if afk_db:
        ISAFK_SQL = gvarstatus("AFK_STATUS")
        AFKREASON_SQL = gvarstatus("AFK_REASON")
    EXCUSE = AFKREASON_SQL if afk_db else AFKREASON
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK or ISAFK_SQL:
            if mention.sender_id not in USERS:
                if EXCUSE:
                    await mention.reply(f"Jestem z dala od klawiatury.\
                    \nPowód: `{EXCUSE}`")
>>>>>>> TelegramUserBot/master
                else:
                    await mention.reply(str(choice(AFKSTR)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if USERS[mention.sender_id] % randint(2, 4) == 0:
<<<<<<< HEAD
                    if AFKREASON:
                        await mention.reply(f"I'm still AFK.\
                            \nReason: `{AFKREASON}`")
=======
                    if EXCUSE:
                        await mention.reply(
                            f"Nadal mnie nie ma.\
                        \nPowód: `{EXCUSE}`")
>>>>>>> TelegramUserBot/master
                    else:
                        await mention.reply(str(choice(AFKSTR)))
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
<<<<<<< HEAD
    global USERS
    global COUNT_MSG
=======
    global AFFKREASON
    ISAFK_SQL = False
    AFKREASON_SQL = None
    if afk_db:
        ISAFK_SQL = gvarstatus("AFK_STATUS")
        AFKREASON_SQL = gvarstatus("AFK_REASON")
    global USERS
    global COUNT_MSG
    EXCUSE = AFKREASON_SQL if afk_db else AFKREASON
>>>>>>> TelegramUserBot/master
    if sender.is_private and sender.sender_id != 777000 and not (
            await sender.get_sender()).bot:
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
<<<<<<< HEAD
        if apprv and ISAFK:
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(f"I'm AFK right now.\
                    \nReason: `{AFKREASON}`")
=======
        if apprv and (ISAFK or ISAFK_SQL):
            if sender.sender_id not in USERS:
                if EXCUSE:
                    await sender.reply(f"Jestem z dala od klawiatury.\
                    \nPowód: `{EXCUSE}`")
>>>>>>> TelegramUserBot/master
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
<<<<<<< HEAD
                    if AFKREASON:
                        await sender.reply(f"I'm still AFK.\
                        \nReason: `{AFKREASON}`")
=======
                    if EXCUSE:
                        await sender.reply(
                            f"Nadal mnie nie ma.\
                        \nPowód: `{EXCUSE}`")
>>>>>>> TelegramUserBot/master
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


<<<<<<< HEAD
@register(outgoing=True, pattern="^.afk(?: |$)(.*)", disable_errors=True)
=======
@register(outgoing=True, pattern="^\.afk(?: |$)(.*)", disable_errors=True)
>>>>>>> TelegramUserBot/master
async def set_afk(afk_e):
    """ For .afk command, allows you to inform people that you are afk when they message you """
    message = afk_e.text
    string = afk_e.pattern_match.group(1)
    global ISAFK
<<<<<<< HEAD
    global AFKREASON
    if string:
        AFKREASON = string
        await afk_e.edit(f"Going AFK!\
        \nReason: `{string}`")
    else:
        await afk_e.edit("Going AFK!")
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\nYou went AFK!")
=======
    global AFFKREASON
    ISAFK_SQL = False
    AFKREASON_SQL = None
    if afk_db:
        ISAFK_SQL = gvarstatus("AFK_STATUS")
        AFKREASON_SQL = gvarstatus("AFK_REASON")
    if string:
        if afk_db:
            addgvar("AFK_REASON", string)
        AFKREASON = string
        await afk_e.edit(f"Jestem z dala od klawiatury.\
                    \nPowód: `{string}`")
    else:
        await afk_e.edit("AFK: Musze kończyć , narazie!")
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\nAFCZYSZ SUKO!")
    if afk_db:
        addgvar("AFK_STATUS", True)
>>>>>>> TelegramUserBot/master
    ISAFK = True
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
<<<<<<< HEAD
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    if ISAFK:
        ISAFK = False
        await notafk.respond("I'm no longer AFK.")
        await sleep(2)
=======
    global COUNT_MSG
    global USERS
    global ISAFK
    global AFFKREASON
    AFKREASON_SQL = None
    ISAFK_SQL = False
    if afk_db:
        ISAFK_SQL = gvarstatus("AFK_STATUS")
        AFKREASON_SQL = gvarstatus("AFK_REASON")
    if ISAFK or ISAFK_SQL:
        if afk_db:
            delgvar("AFK_STATUS")
            delgvar("AFK_REASON")
        ISAFK = False
        AFKREASON = None
>>>>>>> TelegramUserBot/master
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "You've recieved " + str(COUNT_MSG) + " messages from " +
                str(len(USERS)) + " chats while you were away",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "](tg://user?id=" + str(i) + ")" +
                    " sent you " + "`" + str(USERS[i]) + " messages`",
                )
        COUNT_MSG = 0
        USERS = {}
<<<<<<< HEAD
        AFKREASON = None
=======
>>>>>>> TelegramUserBot/master


CMD_HELP.update({
    "afk":
    ".afk [Optional Reason]\
\nUsage: Sets you as afk.\nReplies to anyone who tags/PM's \
you telling them that you are AFK(reason).\n\nSwitches off AFK when you type back anything, anywhere.\
"
})
