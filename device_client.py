import serial
import socket
import time

from parser import parse_ascii


interface = input('Выберите интерфейс (Serial/TCP): ')

if interface == 'Serial':
    while True:
        command = input('Введите (GET_A, GET_B, GET_C) или \'q\' чтобы выйти: ')
        if command.lower() == 'q':
            break
        else:
            with serial.Serial(port='COM5', baudrate=9600, timeout=1) as ser:
                print(f'Отправка: {command}')
                ser.write(f'{command}'.encode('ASCII'))
                time.sleep(0.1)
                response = parse_ascii(ser.readline())
                print(f'Ответ: {response}\n')

elif interface == 'TCP':
    while True:
        command = input('Введите (GET_A, GET_B, GET_C) или \'q\' чтобы выйти: ')
        if command.lower() == 'q':
            break
        else:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('localhost', 12345))
                print(f'Отправка: {command}')
                s.sendall(f'{command}'.encode('ASCII'))
                response = parse_ascii(s.recv(1024))
                print(f'Ответ: {response}\n')
else:
    print('Неизвестный интерфейс')

