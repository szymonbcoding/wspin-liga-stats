from bs4 import BeautifulSoup
import requests
import re
import smtplib
import google.cloud.logging
import logging
import os
from apscheduler.schedulers.blocking import BlockingScheduler

def get_parsed_page_html_code(path: str):

    html_doc = requests.get(path)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    return soup

def change_polish_marks(input: str) -> str:
    input = input.replace('ł','l')
    input = input.replace('Ł','L')
    input = input.replace('ą', 'a')
    input = input.replace('ę', 'e')
    input = input.replace('ó', 'o')
    input = input.replace('ć', 'c')
    input = input.replace('Ć', 'C')
    input = input.replace('ń', 'n')
    input = input.replace('ś', 's')
    input = input.replace('Ś', 'S')
    input = input.replace('ź', 'z')
    input = input.replace('Ź', 'Z')
    return input


def get_current_no_routes() -> str:
    value = get_parsed_page_html_code("http://liga.blokline.pl")
    route_raw = str(value.find('p', {"class" : "lead"}))
    no_routes = re.findall("[0-9][0-9]", route_raw)[0]
    return no_routes

def some_job() -> None:
    with open('nr.txt') as f:
        lines = f.readlines()
    nr = get_current_no_routes()
    check = nr in lines[0]
    f.close()

    if(check):
        logging.info("No changes.")
    else:
        f = open("nr.txt", "w")
        f.write(nr)
        f.close()
        v = get_parsed_page_html_code("http://liga.blokline.pl/Results/Index/3")
        value = v.table.find_all("td")
        # for x in range(10):
        #     m += value[x*4].string + '. ' + value[x*4+2].string + ' ' + value[x*4+1].string + ' - ' + value[x*4+3].string + "\n"
        
        message = "Current number of routes is " + nr + "." + "\n" + "https://liga.blokline.pl/"

        smnr(change_polish_marks(message))


def smnr(m: str) -> None:
    try: 
        #Create your SMTP session 
        smtp = smtplib.SMTP('smtp.gmail.com', 587) 

    #Use TLS to add security 
        smtp.starttls() 

        #User Authentication 
        smtp.login(EMAIL_SENDER, GMAIL_PASSWORD_NEW)

        #Sending the Email
        smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, m) 

        #Terminating the session 
        smtp.quit() 
        logging.info("Email sent successfully!") 

    except Exception as ex: 
        logging.warning("Something went wrong....", ex)


def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(some_job, 'interval', minutes = 1)
    scheduler.start()
    some_job()

if __name__ == '__main__':
    
    # logging
    logging.basicConfig(level=logging.INFO)
    
    if int(os.environ.get("PRODUCTION", 0)) == 1:
        logging_client = google.cloud.logging.Client()
        logging_client.setup_logging()
    
    logging.info("Starting app")
    logging.info(f"Emails receivers: {EMAIL_RECEIVERS}")
    # app
    main()
    