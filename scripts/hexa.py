

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update,ForceReply
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)
# Import module
import sqlite3
  
# Connecting to sqlite
conn = sqlite3.connect('tgbot_button')
  
# Creating a cursor object using 
# the cursor() method
cursor = conn.cursor()
#from tgbot.models import Button


sbc=0
fbc=0
dbc=0
usbc=0
ufbc=0
udbc=0


# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
stupid,fat,dumb = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    """Send a message when the command /start is issued."""
    user = update.effective_user
    
    #print(user.first_name)
    await update.message.reply_html(
        rf"Hi {user.mention_html()} Bot is under construction - Available commands :: /start , /help ",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Use /jokes for Joke service")



async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    #user = update.message.from_user
    
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("Stupid Jokes", callback_data="stupid"),
            InlineKeyboardButton("Fat Jokes", callback_data="fat"),
        ],
        [InlineKeyboardButton("Dumb Jokes", callback_data="dumb")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
   
    await update.message.reply_text("Choose joke genre", reply_markup=reply_markup)
    
    return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("Stupid Jokes", callback_data="stupid"),
            InlineKeyboardButton("Fat Jokes", callback_data="fat"),
        ],
        [InlineKeyboardButton("Dumb Jokes", callback_data="dumb")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
   
    await query.edit_message_text(text="Choose joke genre", reply_markup=reply_markup)
    
    return START_ROUTES


async def stupid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global sbc
    global usbc
    sbc = sbc +1
    usbc = usbc +1
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton('Go Back', callback_data='one'),
            InlineKeyboardButton('Exit', callback_data='two'),
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text= " Imprisoned Picture\nQ: Why did the picture get arrested?\nA: It got framed.", reply_markup=reply_markup
    )
    return END_ROUTES


async def fat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global fbc,ufbc
    fbc = fbc +1
    ufbc=ufbc+1
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton('Go Back', callback_data='one'),
            InlineKeyboardButton('Exit', callback_data='two'),
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text= "My 6-pack is very precious to me.\n That’s why I protect it with a layer of fat.", reply_markup=reply_markup
    )
    return END_ROUTES

async def dumb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global dbc,udbc
    dbc = dbc +1
    udbc=udbc+1
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton('Go Back', callback_data='one'),
            InlineKeyboardButton('Exit', callback_data='two'),
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text= "What is a witch’s favorite subject in school?\nSpelling!", reply_markup=reply_markup
    )
    return END_ROUTES

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    global usbc,ufbc,udbc
    user = update.effective_user
    uid=user.id
    uname=user.first_name

    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="See you next time!")
    
    #packing button counters as a tuple and write to a file 
    bttuple=(sbc,fbc,dbc)
    ustuple=[uid,uname,usbc,ufbc,udbc]
    
    #cursor.execute(''' UPDATE tgbot_button SET stupid_btn_counter=sbc,dumb_btn_counter=dbc,fat_btn_counter=fbc ''')
    f = open("tempdatastorage.txt", "w")
    f.write(str(bttuple))
    f.close()
   
    
    file = open("tempuserstorage.txt", "w")
    for  item in ustuple:
       file.write("%s\n" % item)
    usbc=0
    ufbc=0
    udbc=0
    #Button.save(bttuple)
    return ConversationHandler.END


def run():
    """Run the bot."""
    token = '6150422012:AAFixoycshJiSqiBT0d19L1wdsHuBrjheMc'
    application = Application.builder().token(token).build()
    

    # Add ConversationHandler to application that will be used for handling updates
    
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("jokes", jokes)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(stupid, pattern="stupid"),
                CallbackQueryHandler(fat, pattern="fat"),
                CallbackQueryHandler(dumb, pattern="dumb"),
                
            ],
            END_ROUTES: [
                CallbackQueryHandler(start_over, pattern="one"),
                CallbackQueryHandler(end, pattern="two"),
            ],
        },
        fallbacks=[CommandHandler("jokes", jokes)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()
    #return sbc,fbc,dbc

#if __name__ == "__run__"
#print(run())