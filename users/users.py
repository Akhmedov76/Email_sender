from file_manager import data_manager, users_manager


def show_all_new_messages():
    messages = data_manager.read()
    is_login = users_manager.read()
    new_messages_found = False

    for login in is_login:
        if login['is_login']:
            for message in messages:
                if message['is_active'] and message['username'] == login['username']:
                    print(f"Username: {message['username']}\nMessage: {message['message']}\n")
                    message['is_active'] = False
                    new_messages_found = True

    if new_messages_found:
        data_manager.write(messages)
    else:
        print("No new messages found.")


def show_all_read_messages():
    messages = data_manager.read()
    is_login = users_manager.read()

    for login in is_login:
        if login['is_login']:
            for message in messages:
                if not message['is_active'] and message['username'] == login['username']:
                    print(f"Username: {message['username']}\nMessage: {message['message']}\n")

    print("All messages have been read.")
