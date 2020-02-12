# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
<<<<<<< HEAD
# credits to @AvinashReddy3108
=======
>>>>>>> TelegramUserBot/master
#
"""
This module updates the userbot based on Upstream revision
"""

from os import remove, execle, path, makedirs, getenv, environ
from shutil import rmtree
import asyncio
import sys

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from userbot import CMD_HELP, bot, HEROKU_APIKEY, HEROKU_APPNAME, UPSTREAM_REPO_URL
from userbot.events import register

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), 'requirements.txt')


async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            ' '.join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


@register(outgoing=True, pattern="^\.update(?: |$)(.*)")
async def upstream(ups):
    "For .update command, check if the bot is up to date, update if specified"
<<<<<<< HEAD
    await ups.edit("`Checking for updates, please wait....`")
=======
    await ups.edit("`Sprawdzanie aktaulizacji, poczekaj....`")
>>>>>>> TelegramUserBot/master
    conf = ups.pattern_match.group(1)
    off_repo = UPSTREAM_REPO_URL
    force_update = False

    try:
<<<<<<< HEAD
        txt = "`Oops.. Updater cannot continue due to "
        txt += "some problems occured`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ups.edit(f'{txt}\n`directory {error} is not found`')
        repo.__del__()
        return
    except GitCommandError as error:
        await ups.edit(f'{txt}\n`Early failure! {error}`')
=======
        txt = "`Oops.. Wystąpił błąd "
        txt += "some problems occured`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ups.edit(f'{txt}\n`folder {error} nie odnaleziony`')
        repo.__del__()
        return
    except GitCommandError as error:
        await ups.edit(f'{txt}\n`Wczesny błąd! {error}`')
>>>>>>> TelegramUserBot/master
        repo.__del__()
        return
    except InvalidGitRepositoryError as error:
        if conf != "now":
            await ups.edit(
<<<<<<< HEAD
                f"`Unfortunately, the directory {error} does not seem to be a git repository.\
            \nBut we can fix that by force updating the userbot using .update now.`"
=======
                f"`Niestety folder {error} nie wygląda na repo .git\
            \nAle możesz to wymusić wpisując .update now`"
>>>>>>> TelegramUserBot/master
            )
            return
        repo = Repo.init()
        origin = repo.create_remote('upstream', off_repo)
        origin.fetch()
        force_update = True
<<<<<<< HEAD
        repo.create_head('sql-extended', origin.refs.sql-extended)
        repo.heads.sql-extended.set_tracking_branch(origin.refs.sql-extended)
        repo.heads.sql-extended.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != 'sql-extended':
        await ups.edit(
            f'**[UPDATER]:**` Looks like you are using your own custom branch ({ac_br}). '
            'in that case, Updater is unable to identify '
            'which branch is to be merged. '
            'please checkout to any official branch`')
=======
        repo.create_head('master', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != 'master':
        await ups.edit(
            f'**[Aktualizator]:**` Wygląda na to że używasz własnego repozytorium ({ac_br}). '
            'w tym wypadku aktualizator nie wykryje wersji '
            'która może zostać scalona. '
            'wybierz oficjalny branch`')
>>>>>>> TelegramUserBot/master
        repo.__del__()
        return

    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if not changelog and not force_update:
        await ups.edit(
<<<<<<< HEAD
            f'\n`Your BOT is`  **up-to-date**  `with`  **{ac_br}**\n')
=======
            f'\n`Twój bot jest aktualny`  **up-to-date**  `z`  **{ac_br}**\n')
>>>>>>> TelegramUserBot/master
        repo.__del__()
        return

    if conf != "now" and not force_update:
<<<<<<< HEAD
        changelog_str = f'**New UPDATE available for [{ac_br}]:\n\nCHANGELOG:**\n`{changelog}`'
        if len(changelog_str) > 4096:
            await ups.edit("`Changelog is too big, view the file to see it.`")
=======
        changelog_str = f'**Nowa aktualizacja dostępna [{ac_br}]:\n\nZMIANY:**\n`{changelog}`'
        if len(changelog_str) > 4096:
            await ups.edit("`Dziennik zmian jest za duzy.`")
>>>>>>> TelegramUserBot/master
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await ups.client.send_file(
                ups.chat_id,
                "output.txt",
                reply_to=ups.id,
            )
            remove("output.txt")
        else:
            await ups.edit(changelog_str)
<<<<<<< HEAD
        await ups.respond('`do \".update now\" to update`')
=======
        await ups.respond('`zrob \".update now\" aby zaaktualizować`')
>>>>>>> TelegramUserBot/master
        return

    if force_update:
        await ups.edit(
<<<<<<< HEAD
            '`Force-Syncing to latest stable userbot code, please wait...`')
    else:
        await ups.edit('`Updating userbot, please wait....`')
=======
            '`Wymuszono zbudowanie nowej wersji instancji. Zaczekaj...`')
    else:
        await ups.edit('`Aktualizowanie bota, Zaczekaj....`')
>>>>>>> TelegramUserBot/master
    # We're in a Heroku Dyno, handle it's memez.
    if HEROKU_APIKEY is not None:
        import heroku3
        heroku = heroku3.from_key(HEROKU_APIKEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if not HEROKU_APPNAME:
            await ups.edit(
<<<<<<< HEAD
                '`[HEROKU MEMEZ] Please set up the HEROKU_APPNAME variable to be able to update userbot.`'
=======
                '`[Heroku] Prosze ustaw HEROKU_APPNAME variable aby moc aktualizwać bota.`'
>>>>>>> TelegramUserBot/master
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APPNAME:
                heroku_app = app
                break
        if heroku_app is None:
            await ups.edit(
<<<<<<< HEAD
                f'{txt}\n`Invalid Heroku credentials for updating userbot dyno.`'
            )
            repo.__del__()
            return
        await ups.edit('`[HEROKU MEMEZ]\
                        \nUserbot dyno build in progress, please wait for it to complete.`'
=======
                f'{txt}\n`Złe dane heroku.`'
            )
            repo.__del__()
            return
        await ups.edit('`[HEROKU]\
                        \nBudowa instancji rozpoczęta, poczekaj na zakończenie.`'
>>>>>>> TelegramUserBot/master
                       )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_APIKEY + "@")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
<<<<<<< HEAD
            remote.push(refspec="HEAD:refs/heads/sql-extended", force=True)
=======
            remote.push(refspec="HEAD:refs/heads/master", force=True)
>>>>>>> TelegramUserBot/master
        except GitCommandError as error:
            await ups.edit(f'{txt}\n`Here is the error log:\n{error}`')
            repo.__del__()
            return
<<<<<<< HEAD
        await ups.edit('`Successfully Updated!\n'
                       'Restarting, please wait...`')
=======
        await ups.edit('`Pomyślnie zaaktualizowano!\n'
                       'Restartowanie, zaczekaj...`')
>>>>>>> TelegramUserBot/master
    else:
        # Classic Updater, pretty straightforward.
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        reqs_upgrade = await update_requirements()
<<<<<<< HEAD
        await ups.edit('`Successfully Updated!\n'
                       'Bot is restarting... Wait for a second!`')
=======
        await ups.edit('`Pomyślnie zaaktualizowano!\n'
                       'Restartowanie, zaczekaj...`')
>>>>>>> TelegramUserBot/master
        # Spin a new instance of bot
        args = [sys.executable, "-m", "userbot"]
        execle(sys.executable, *args, environ)
        return


CMD_HELP.update({
    'update':
    ".update\
\nUsage: Checks if the main userbot repository has any updates and shows a changelog if so.\
\n\n.update now\
\nUsage: Updates your userbot, if there are any updates in the main userbot repository."
})
