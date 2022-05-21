# 210522 added telegram bot support for jobscraper
# 210522 changed results to show only top 5 results

import constants as c
from jobscraper_bot import search_all
from jobscraper_bot_v2 import search
import telegram.ext
import random
import requests

hi = ['hi', 'hey', 'hello', 'hiya', 'yo']
bye = ['bye', 'byebye' 'bye bye', 'bb']
thanks = ['thankyou', 'thank you', 'thanks', 'ty']
search_mode = False
searchall_mode = False
feedback_mode = False

print('Initializing bot..\n')


def greeting(ui, update):
    if ui in hi:
        x = random.randint(0, 2)
        if x == 0:
            update.message.reply_text('Hello!')
        elif x == 1:
            update.message.reply_text('Hi!')
        else:
            update.message.reply_text('Hey!')
    elif ui in bye:
        x = random.randint(0, 2)
        if x == 0:
            update.message.reply_text('Bye!')
        elif x == 1:
            update.message.reply_text('Goodbye!')
        else:
            update.message.reply_text('See you!')
    elif ui in thanks:
        update.message.reply_text('No problem!')
    else:
        update.message.reply_text("Please enter the /search or /searchall command before entering your desired job title!")


def handle_message(update, context):
    global search_mode
    global searchall_mode
    global feedback_mode
    with open('jobscraper_logs.txt', 'a') as logs:
        logs.write(f'''
{update.message.chat.first_name} {update.message.chat.last_name}:
{update.message.text}
{update['message']['date']}
''')
    user_input = str(update.message.text)

    if search_mode:
        update.message.reply_text(f'Searching for {user_input}..')
        search(user_input, update)
        with open('jobs_from_jobscraper1.txt', encoding="utf-8") as final:
            update.message.reply_text(final.read())
        with open('jobs_from_jobscraper2.txt', encoding="utf-8") as final:
            update.message.reply_text(final.read())
        with open('jobs_from_jobscraper3.txt', encoding="utf-8") as final:
            update.message.reply_text(final.read())
        with open('jobs_from_jobscraper4.txt', encoding="utf-8") as final:
            update.message.reply_text(final.read())
        with open('jobs_from_jobscraper5.txt', encoding="utf-8") as final:
            update.message.reply_text(final.read())
        search_mode = False
    elif searchall_mode:
        update.message.reply_text(f'Searching all {user_input}..')
        search_all(user_input, update)
        with open('alljobs_jobscraper.txt') as alljobsfile:
            update.message.reply_document(alljobsfile)
        searchall_mode = False
    elif feedback_mode:
        with open('jobscraper_feedbacks.txt', 'a') as logs:
            update.message.reply_text('Thank you for your input!')
            logs.write(f"{update.message.chat.first_name} {update.message.chat.last_name}\n{update['message']['date']}\n{user_input}\n\n")
            feedback_mode = False
    else:
        greeting(user_input, update)


def start_command(update, context):
    with open('jobscraper_logs.txt', 'a') as logs:
        logs.write(f'''
{update.message.chat.first_name} {update.message.chat.last_name}:
{update.message.text}
{update['message']['date']}
''')
    update.message.reply_text('Hello, My name is JobscraperSbot!\nI take the frontpage results from each of the 5 \
biggest job-search portals in Singapore such as indeed, jobstreet, jobsdb, linkedin, and jobscentral and display them \
here!')
    update.message.reply_text('To begin, enter the command /search or /searchall.')


def search_command(update, context):
    global search_mode
    global searchall_mode
    global feedback_mode
    searchall_mode = False
    feedback_mode = False
    with open('jobscraper_logs.txt', 'a') as logs:
        logs.write(f'''
{update.message.chat.first_name} {update.message.chat.last_name}:
{update.message.text}
{update['message']['date']}
''')
    update.message.reply_text('/search only shows the top 5 results from each of the websites. Use /searchall if \
you want to see all results!')
    update.message.reply_text('What is your desired job title?')
    search_mode = True


def searchall_command(update, context):
    global search_mode
    global searchall_mode
    global feedback_mode
    search_mode = False
    feedback_mode = False
    with open('jobscraper_logs.txt', 'a') as logs:
        logs.write(f'''
{update.message.chat.first_name} {update.message.chat.last_name}:
{update.message.text}
{update['message']['date']}
''')
    update.message.reply_text('/searchall shows ALL frontpage results from each of the website in a .txt file format. Use \
/search if you only want to see the top 5 results from each of the webpage!')
    update.message.reply_text('What is your desired job title?')
    searchall_mode = True


def feedback_command(update, context):
    global search_mode
    global searchall_mode
    global feedback_mode
    search_mode = False
    searchall_mode = False
    update.message.reply_text('What would you like to feedback on? Please keep your feedback to 1 message!')
    feedback_mode = True


def help_command(update, context):
    with open('jobscraper_logs.txt', 'a') as logs:
        logs.write(f'''
{update.message.chat.first_name} {update.message.chat.last_name}:
{update.message.text}
{update['message']['date']}
''')
    update.message.reply_text('''
Hello, thanks for using jobscraper!

This telegram bot takes the frontpage results from each of the top job searching websites such as:
sg.indeed.com
jobstreet.com.sg
sg.jobsdb.com
sg.linkedin.com
jobscentral.com.sg

and displays information such as:
-Job title Company 
-Salary 
-Location 
-Job type 
-Date posted 
-Link to the original job post so that you may apply 

so that you don't have to navigate through different websites for the results. Of course, some employers may not have posted certain information such as salary, location or job type so some information fields may be unavailable. 
''')
    update.message.reply_text('To begin, use /search or /searchall.')


def error(update, context):
    update.message.reply_text('An exception has occurred, please try again!')
    print(f"ERROR:\nUpdate {update} caused error {context.error}\n")
    with open('jobscraper_logs.txt', 'a') as logs:
        logs.write(f"ERROR:\nUpdate {update} caused error {context.error}\n")


def main():
    updater = telegram.ext.Updater(c.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(telegram.ext.CommandHandler('start', start_command))
    dp.add_handler(telegram.ext.CommandHandler('search', search_command))
    dp.add_handler(telegram.ext.CommandHandler('searchall', searchall_command))
    dp.add_handler(telegram.ext.CommandHandler('feedback', feedback_command))
    dp.add_handler(telegram.ext.CommandHandler('help', help_command))
    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
