import threading
import ijson
import smtplib
from datetime import datetime
from file_manager import users_manager, data_manager
from users.logs import log_decorator


def show_all_users():
    # Read users data from file
    with open('./data/users.json', 'r') as file:
        users_data = ijson.items(file, 'item')
        for users in users_data:
            print(
                f"username: {users['username']}\ngmail: {users['gmail']}\nage: {users['age']}\ngender: "
                f"{users['gender']}\n")


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_sender = 'ahmedovj5016@gmail.com'
smtp_password = 'bzlc srjb brsa mfpg'


@log_decorator
def send_mail_message(to_user, subject, message):
    email = f"Subject: {subject}\n\n{message}"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, email)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")


@log_decorator
def send_messages_all_users():
    all_users = users_manager.read()
    user_subject = "Verification code:"
    message = input("Enter message:").capitalize().strip()
    for user in all_users:
        current_time = datetime.now().strftime("%Y.%m.%d %H.%M")
        threading.Thread(target=send_mail_message, args=({user['gmail']}, user_subject, message)).start()
        data = {
            'username': user['username'],
            'gmail': user['gmail'],
            'age': user['age'],
            'gender': user['gender'],
            'message': message,
            'time': current_time,
            'is_active': True
        }
        data_manager.add_data(data)
        print(f"Sent message to {user['username']} at {current_time}")


@log_decorator
def send_message_to_males():
    all_users = users_manager.read()
    user_subject = "Verification code:"
    message = input("Enter message:").capitalize().strip()
    try:
        for user in all_users:
            if user['gender'] == 'Male':
                current_time = datetime.now().strftime("%Y.%m.%d %H.%M")
                threading.Thread(target=send_mail_message, args=({user['gmail']}, user_subject, message)).start()
                print(f"Sent message to {user['username']} at {current_time}")
                data = {
                    'username': user['username'],
                    'gmail': user['gmail'],
                    'age': user['age'],
                    'gender': user['gender'],
                    'message': message,
                    'time': current_time,
                    'is_active': True
                }
                data_manager.add_data(data)
        return True
    except smtplib.SMTPException as e:
        print(f"Something went wrong {e}")
        return False


@log_decorator
def send_message_to_females():
    all_users = users_manager.read()
    user_subject = "Verification code:"
    message = input("Enter message:").capitalize()
    try:
        for user in all_users:
            if user['gender'] == 'Female':
                current_time = datetime.now().strftime("%Y.%m.%d %H.%M")
                threading.Thread(target=send_mail_message, args=({user['gmail']}, user_subject, message)).start()
                print(f"Sent message to {user['username']} at {current_time}")
                data = {
                    'username': user['username'],
                    'gmail': user['gmail'],
                    'age': user['age'],
                    'gender': user['gender'],
                    'message': message,
                    'time': current_time,
                    'is_active': True
                }
                data_manager.add_data(data)
                return True
    except Exception as e:
        print(f"Something went wrong {e}")
        return False
    except smtplib.SMTPException as e:
        print(f"Failed {e}")
        return False


@log_decorator
def send_message_to_older_than_18():
    all_users = users_manager.read()
    user_subject = "Verification code:"
    message = input("Enter message:")
    try:
        for user in all_users:
            if int(user['age']) > 18:
                current_time = datetime.now().strftime("%Y.%m.%d %H.%M")
                threading.Thread(target=send_mail_message, args=({user['gmail']}, user_subject, message)).start()
                print(f"Sent message to {user['username']} at {current_time}")
                data = {
                    'username': user['username'],
                    'gmail': user['gmail'],
                    'age': user['age'],
                    'gender': user['gender'],
                    'message': message,
                    'time': current_time,
                    'is_active': True
                }
                data_manager.add_data(data)
        return True
    except smtplib.SMTPException as e:
        print(f"Something went wrong {e}")
        return False
    except Exception as e:
        print(f"Something went wrong {e}")
        return False


@log_decorator
def send_message_to_younger_than_18():
    all_users = users_manager.read()
    user_subject = "Verification code:"
    message = input("Enter message:")
    try:
        for user in all_users:
            if int(user['age']) <= 18:
                current_time = datetime.now().strftime("%Y.%m.%d %H.%M")
                threading.Thread(target=send_mail_message, args=({user['gmail']}, user_subject, message)).start()
                print(f"Sent message to {user['username']} at {current_time}")
                data = {
                    'username': user['username'],
                    'gmail': user['gmail'],
                    'age': user['age'],
                    'gender': user['gender'],
                    'message': message,
                    'time': current_time,
                    'is_active': True
                }
                data_manager.add_data(data)
        return True
    except smtplib.SMTPException as e:
        print(f"Something went wrong {e}")
        return False
    except Exception as e:
        print(f"Something went wrong {e}")
        return False


@log_decorator
def show_message_with_time():
    data = data_manager.read()
    for message in data:
        print(f"Username: {message['username']}\nGmail: {message['gmail']}\nAge: {message['age']}\n"
              f"Gender: {message['gender']}\nTime: {message['time']}\nMessage: {message['message']}\n")
