import serial
import socket

from parser import parse_ascii

def get_responce(command):
    if command == 'GET_A':
        return 'A_10V'
    elif command == 'GET_B':
        return 'B_5V'
    elif command == 'GET_C':
        return 'C_15A'
    else:
        return 'Unknown command'


interface = input('Выберите интерфейс (Serial/TCP): ')

if interface == 'Serial':
    ser = serial.Serial(port='COM4', baudrate=9600, timeout=1)
    print('Начало работы')

    while True:
        if ser.in_waiting:
            command = parse_ascii(ser.readline())
            print(f'Получено: {command}')
            print(f'Отправка: {get_responce(command)}')
            ser.write(f'{get_responce(command)}'.encode('ASCII'))
    
elif interface == 'TCP':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    print('Начало работы')

    while True:
        client, addr = server.accept()
        print(f'Принято соединение от {addr}')
        
        while True:
            command = parse_ascii(client.recv(1024))
            if not command:
                break
            print(f'Получено: {command}')
            print(f'Отправка: {get_responce(command)}')
            client.send(f'{get_responce(command)}'.encode('ASCII'))
        
        client.close()
        print(f'Закрыто соединение с {addr} closed')
else:
    print('Неизвестный интерфейс')

