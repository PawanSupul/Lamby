
import json

progress_json = 'user/progress.json'
# progress_json = 'progress.json'

def read_progress_json():
    with open(progress_json, 'r') as fid:
        return json.load(fid)


def save_progress_json(json_dic):
    with open(progress_json, 'w') as fidw:
        json.dump(json_dic, fidw, indent=4)


def get_completed_lessons(username):
    json_data = read_progress_json()
    if username not in json_data.keys():
        completed = []
    else:
        completed = json_data[username]['completed-lessons']
    return completed


def add_completed_lesson_to_user(username, lesson):
    json_data = read_progress_json()
    if(username not in json_data.keys()):
        json_data[username] = {
            "completed-lessons": [lesson]
        }
    else:
        if lesson not in json_data[username]['completed-lessons']:
            json_data[username]['completed-lessons'].append(lesson)
    save_progress_json(json_data)






if __name__ == '__main__':
    add_completed_lesson_to_user('test1', 2)

