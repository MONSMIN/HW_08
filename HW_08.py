
from datetime import datetime, timedelta, date
from collections import defaultdict
from pprint import pprint

def get_next_week_start(d: datetime):
    diff_days = 0 - d.weekday()
    return d + timedelta(days=diff_days)


def prepare_birthday(text: str):
    bd = datetime.strptime(text, '%d, %m, %Y' )
    return bd.replace(year=datetime.today().year).date()


def get_birthdays_per_week(users):
    birthdays = defaultdict(list)

    today = datetime(2023, 3, 20).date()#datetime.now().date() 

    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)

    happy_users = [user for user in users 
                   if start_period <= prepare_birthday(user['birthday']) <= end_period]

    for user in happy_users:
        current_bd: date =  prepare_birthday(user['birthday'])
        if current_bd.weekday() in (5,6):
            birthdays['Monday'].append(user['name'])
        else:
            birthdays[current_bd.strftime('%A')].append(user['name'])
    
    return birthdays
        




if __name__ == "__main__":
    
    users = [{'name': 'Andrey', 'birthday': '21, 3, 1990'},
             {'name': 'Borys', 'birthday': '22, 3, 1992'},
             {'name': 'Viktor', 'birthday': '23, 3, 1980'},
             {'name': 'Galagan', 'birthday': '26, 3, 2000'},
             {'name': 'Elvira', 'birthday': '24, 3, 1939'},
             {'name': 'Anna', 'birthday': '18, 3, 1992'},
             {'name': 'Dima', 'birthday': '19, 3, 1994'},
             {'name': 'Mykyta', 'birthday': '17, 3, 2003'},
             {'name': 'Zhanna', 'birthday': '18, 3, 1994'},
             {'name': 'Kateryna', 'birthday': '20, 3, 1994'}]
    
    result = get_birthdays_per_week(users)
    pprint(result)