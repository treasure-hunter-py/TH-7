from os import name, read
import pathlib
import csv

def start_main():
    pass

def balance_changer(user_id):
    print('add 1 | get 2')
    while True:
        chek = input()
        if chek == '1':
            try:
                temp_many = 0
                with open(pathlib.Path(__file__).parent.joinpath('DEPOSIT').joinpath(f'{user_id}.txt'), 'r') as validator_file:
                    temp_many = int(validator_file.read())
            except Exception:
                with open(pathlib.Path(__file__).parent.joinpath('DEPOSIT').joinpath(f'{user_id}.txt'), 'w') as validator_file:
                    validator_file.write('0')

                    
    

def balance_checkr():
    pass



def user_menu(user_id):
    #print(user_id)
    print('balance check 1 ')
    print('balance change 2 ')
    print('balance exit 3 ')
    aktor = input()
    if aktor == '1':
        balance_checkr(user_id)
    elif aktor == '2':
        balance_changer(user_id)
    elif aktor == '3':
        return

#    with open(pathlib.Path(__file__).parent.joinpath('DEPOSIT').joinpath(f'{user_id}.txt'), 'r') as validator_file:
        

def validator(user_name = 0,user_password = 0):
    with open(pathlib.Path(__file__).parent.joinpath('db').joinpath('db.txt'), 'r') as validator_file:
        #print(validator_file.read())
        temp_file = csv.DictReader(validator_file)
        for dict_user in temp_file:
            if user_name == dict_user['name']:
                if user_password == dict_user['password']:
                    user_menu(dict_user['name'])
                    break
                else:
                    print('error password')
            else:
                print('user is not found... ')


validator('user_1','1111')