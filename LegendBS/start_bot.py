from pyrogram.types import BotCommand


async def start_bot(Client):
    await Client.start()
    try:
        x = await Client.get_me()
        print(f"Client - [INFO]: @{x.username} get started ")
    except Exception as e:
        print(f"Error - {e}")
    try:
        print("Settings All Commands")
        await Client.set_bot_commands(
            [
                BotCommand("start", "Start Bot By Anyone"),
                BotCommand("ping", "Check that bot is alive or dead"),
                BotCommand("banall", "banall the member in Group"),
                BotCommand("birthday", "spam the chat with birthday message"),
                BotCommand("restart", "Restart The Bot"),
                BotCommand("eval", "Run Python Code"),
                BotCommand("exec", "Install The Requirements"),
                BotCommand("gm", "Spam The Chat with good morning message"),
                BotCommand("ga", "Spam The Chat With Good Afternoon Messages"),
                BotCommand("gn", "Spam The Chat With Good Night Message"),
                BotCommand("raid", "Spam The Chat With Raid"),
                BotCommand("rraid", "Start The Raid in Chat By Replying to person"),
                BotCommand("draid", "Stop The Raid in Chat"),
                BotCommand("listraid", "Ceck the list on started raid on it"),
                BotCommand("shayri", "Spam in chat with shayri"),
                BotCommand("stop","To stop unlimited spam/raid/abuse"),
                BotCommand("dspam", "Sart the chat with delay spam"),
                BotCommand("pspam", "Pornspam with raid"),
                BotCommand("hang", "Start hang command used to hang the chat"),
                BotCommand("uspam", "Start the Spam till used command .stop"),
                BotCommand("uraid", "Start the unlimited raid"),
                BotCommand("abuse", "Start abusing non stop"),
                BotCommand("echo", "echo the reply msg")
                
            ]
        )
    except:
        pass
        
