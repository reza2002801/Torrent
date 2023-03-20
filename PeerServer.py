import socket
import threading


def share():
    pass


def get():
    pass


def main():
    while True:
        print('Enter any command \n'
              ' share: share any file you want \n'
              ' get: get any file you want \n'
              ' q: quit the app\n-----------------------------------------------------' )
        command = input()
        if command == 'share': share()
        elif command == 'get': get()
        elif command == 'q':break
        else: print('I didnt undrestand!!!')
if __name__ == '__main__':
    main()