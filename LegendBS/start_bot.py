def start_bot(Client):
    Client.start()
    try:
        x = await Client.get_me()
        print(f"Client - [INFO]: @{x.username} get started ")
    except Exception as e:
        print(f"Error - {e}")
