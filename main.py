from bs4 import BeautifulSoup
import requests
import logging
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from sys import getsizeof
import time

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

def some_job() -> None:
    pass


# def main():
#     scheduler = BlockingScheduler()
#     scheduler.add_job(some_job, 'interval', minutes = 15)
#     scheduler.start()
#     some_job()

if __name__ == '__main__':

    a = get_parsed_page_html_code('https://liga.blokline.pl/Home/Ranking')

    timestr = time.strftime("%Y%m%d-%H%M%S")
    with open(f"data/{timestr}", mode="w") as f:
        f.write(str(a))

    