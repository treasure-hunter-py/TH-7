
import pathlib

def core(user_file_name,user_n):
    class my_error(Exception):
        pass
    
    try:
        with open(pathlib.Path(__file__).parent.joinpath(user_file_name), 'r') as data_file:
            data_str = data_file.read()
            if len(data_str) < user_n*3:
                raise my_error
            groop1 = data_str[:user_n]
            groop2 = data_str[len(data_str) // 2:(len(data_str) // 2)+user_n]
            groop3 = data_str[len(data_str)-user_n:]
            count_space = len(data_str) - (user_n*3)
            l_space = count_space // 2
            r_space = count_space - l_space
            print(groop1 + (l_space*' ') + groop2 + (r_space*' ') + groop3)
    except FileNotFoundError:
        print('File not found')
    except my_error:
        print('count mor limit')
core('file.txt',40)
