import keyboard
from winotify import Notification
import datetime

fsm_tech = {
    'INT': {
        "EAST EST": [3001, 3002, 3003, 3004, 3005],
        "WEST CST": [3011, 3012, 3013]
    },
    'QA2': {
        "EAST EST": [5001, 5002, 5003, 5004, 5005],
        "WEST EST": [5021, 5022, 5023]
    }
}


    
lab_support = {
    0: ['Venkatesh', 'Shiraz'],
    1: ['Seema', 'Jaspreet'],
    2: ['Venkatesh', 'Sahil'],
    3: ['Shiraz', 'Seema'],
    4: ['Sahil', 'Jaspreet']
}

validations = [
    'ODO',
    'Order Manager',
    'Neustar',
    'NetQ',
    'MetaView Web',
    'Strata',
    'Boost',
    'LDAP',
    'Trio',
    'Leaf Lite',
    'SDP',
    'IDA',
    'DDP'
]


def all_validations():
    global validations
    msg = ', '.join(validations)
    
    toast = Notification(app_id='Validations',
                         title='Validations',
                         msg=msg)
    toast.show()

def fsm(env):
    global fsm_tech
    print(fsm_tech[env])
    msg = ''
    for k, v in fsm_tech[env].items():
        msg += f'{k}: {v}\n'
    toast = Notification(app_id='FSM Tech ID',
                         title=env,
                         msg=msg)
    toast.show()

def lab(day):
    global lab_support
    msg = ''
    msg += ', '.join(lab_support[day])
    
    toast = Notification(app_id='Lab Support',
                         title='Lab Support',
                         msg=msg)   
    toast.show()
    
keyboard.add_hotkey('ctrl+f+i', lambda: fsm('INT'))
keyboard.add_hotkey('ctrl+f+2', lambda: fsm('QA2'))
keyboard.add_hotkey('ctrl+l', lambda: lab(datetime.datetime.today().weekday()))
keyboard.add_hotkey('ctrl+j', all_validations)

while True:
    keyboard.read_key()