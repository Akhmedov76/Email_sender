from users.admin import show_all_users, send_messages_all_users, send_message_to_males, send_message_to_females, \
    send_message_to_older_than_18, send_message_to_younger_than_18, show_message_with_time
from users.common import logout, register, login, UserTypes
from users.logs import log_settings
from users.users import show_all_new_messages, show_all_read_messages


def show_admin_menu():
    txt = """
    1. Show all users
    2. Send message from gmail:
    3. Show sent message with time
    4. Exit
    """
    print(txt)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        show_all_users()
        show_admin_menu()
    elif user_input == "2":
        show_message_menu()
        show_admin_menu()
    elif user_input == "3":
        show_message_with_time()
        show_admin_menu()
    elif user_input == "4":
        print("Exit successfully")
        return show_auth_menu()
    else:
        print("Invalid choice! Please try again.")
        show_admin_menu()


def show_message_menu():
    print("""
    1. Send message to all users
    2. Send message to males
    3. Send message to females
    4. Send message to higher from 18
    5. Send message to lower from 18
    6. Exit
    """)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        send_messages_all_users()
        show_message_menu()
    elif user_input == "2":
        if send_message_to_males():
            show_message_menu()
        else:
            print("No male users found.")
            show_message_menu()
    elif user_input == "3":
        if send_message_to_females():
            show_message_menu()
        else:
            print("No female users found.")
            show_message_menu()
    elif user_input == "4":
        send_message_to_older_than_18()
        show_message_menu()
    elif user_input == "5":
        send_message_to_younger_than_18()
        show_message_menu()
    elif user_input == "6":
        print("Exit successfully")
        return show_admin_menu()


def user_menu():
    print("""
1. Show all new messages
2. Show all read messages
3. Exit""")

    user_input = input("Enter your choice: ")
    if user_input == "1":
        show_all_new_messages()
        user_menu()
    elif user_input == "2":
        show_all_read_messages()
        user_menu()
    elif user_input == "3":
        print("Exit successfully!")
        return show_auth_menu()
    else:
        print("Invalid choice! Please try again.")
        user_menu()


def show_auth_menu():
    print("""
1. Register
2. Login
3. Exit""")
    # print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        if register():
            show_auth_menu()
    elif user_input == "2":
        user = login()
        if not user:
            print("Invalid username and password. Please try again.")
            show_auth_menu()
        elif user['user_type'] == UserTypes.ADMIN.value:
            show_admin_menu()
        elif user['user_type'] == UserTypes.USER.value:
            user_menu()
        else:
            print("Invalid credentials!")
            show_auth_menu()
    elif user_input == "3":
        if logout():
            print("Goodbye!")
            exit()
        else:
            print("Logout canceled!😊")
            show_auth_menu()
    else:
        print("Invalid input. Please try again.")
        show_auth_menu()


if __name__ == "__main__":
    log_settings()  # Enable logging for all functions in this module.
    show_auth_menu()
