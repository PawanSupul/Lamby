import json
import bcrypt
import datetime

credential_file = 'user/credential.json'


def load_credentials_file():
    try:
        with open(credential_file, 'r') as fid:
            return json.load(fid)
    except FileNotFoundError:
        print('Credential file not found')
        return {}


def save_credentials_file(json_dict):
    with open(credential_file, 'w') as fidw:
        json.dump(json_dict, fidw, indent=4)


def save_credentials_when_signup(input_dict):
    name = input_dict['name']
    age = input_dict['age']
    gender = input_dict['gender']
    username = input_dict['username']
    password = input_dict['password']
    # password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    password_hash = password
    today_date = str(datetime.datetime.today().date())
    credentials = load_credentials_file()
    if credentials == {}:
        credentials = {
            "current_user": username,
            "credentials": {}
        }
    if username not in credentials['credentials'].keys():
        credentials['credentials'][username] = {}

    credentials['credentials'][username]['name'] = name
    credentials['credentials'][username]['age'] = age
    credentials['credentials'][username]['gender'] = gender
    credentials['credentials'][username]['last-login'] = today_date
    credentials['credentials'][username]['password'] = password_hash
    credentials['credentials'][username]['updated'] = today_date

    save_credentials_file(credentials)


def update_current_user(username):
    credentials = load_credentials_file()
    credentials['current_user'] = username
    save_credentials_file(credentials)


def update_last_login_date(username):
    credentials = load_credentials_file()
    credentials['credentials'][username]['last-login'] = str(datetime.datetime.today().date())
    save_credentials_file(credentials)


def verify_user(username, password):
    """
    verify username and password

    :param username: username
    :param password: password
    :return:
        0: verified
        1: username does not exist
        2: password does not match
        3: password corrupted
        4: password update needed
    """
    credential_data = load_credentials_file()

    if username not in credential_data['credentials'].keys():
        return 1
    else:
        today_date = datetime.datetime.today()
        last_updated = datetime.datetime.strptime(credential_data['credentials'][username]['updated'], "%Y-%m-%d")
        stored_password = credential_data['credentials'][username]['password']
        if stored_password != '':
            if password == stored_password:

        # if stored_password.startswith("$2b$"):
        #     if bcrypt.checkpw(password.encode(), stored_password.encode()):
                # successful verification
                update_last_login_date(username)
                if (today_date - last_updated > datetime.timedelta(days=180)):
                    # password update needed
                    return 4
                else:
                    return 0
            else:
                # incorrect password
                return 2
        else:
            # invalid password
            return 3


def get_current_user():
    credentials = load_credentials_file()
    if credentials == {}:
        current_user = 'None'
    else:
        current_user = credentials['current_user']
    return current_user


def get_all_registered_users():
    credentials = load_credentials_file()
    if credentials == {}:
        user_list = []
    else:
        user_list = list(credentials['credentials'].keys())
    return user_list


def get_password_for_user(username):
    credentials = load_credentials_file()
    password = credentials['credentials'][username]['password']
    return password


def get_gender_for_user(username):
    credentials = load_credentials_file()
    gender = credentials['credentials'][username]['gender']
    return gender


""" Notes
1. Remove current user if the last login is more than 3 months


"""



if __name__ == '__main__':
    # save_credentials('test 3', 'test pw', True)
    # today_date = datetime.datetime.today()
    # updated = "2025-02-08"
    # last_update = datetime.datetime.strptime(updated, "%Y-%m-%d")
    # b = 9
    # results = verify_user('test', 'test pw 1')
    # print(results)
    credential_file = 'credential.json'
    save_credentials_when_signup('test', 'test', True)