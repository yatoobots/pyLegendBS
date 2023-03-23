async def get_user(Legend, message):
    try:
        args = message.text.split(" ", 1)[1].split(" ", 1)
    except IndexError:
        args = None
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
    elif args:
        user_ = args[0]
        if user_.isnumeric():
            user_ = int(user_)
        if not user_:
            await message.reply_text(
                "I don't know who you're talking about, you're going to need to specify a user.!"
            )
            return
        try:
            user = await Legend.get_users(user_)
        except (TypeError, ValueError):
            await message.reply_text(
                "Looks like I don't have control over that user, or the ID isn't a valid one. If you reply to one of their messages, I'll be able to interact with them."
            )
            return
    else:
        await message.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user...!"
        )
        return

    return user


def user_errors(error):
    if '[400 USERNAME_NOT_OCCUPIED]' in str(error):
       return "You didn't provide username"
    elif '[400 USERNAME_INVALID]' in str(error):
       return "Username is invalid"
    elif '[400 PEER_ID_INVALID]' in str(error):
       return "Invalid User ID!"
    else:
       return f"**Unknown Error:** \n\n {error}"
