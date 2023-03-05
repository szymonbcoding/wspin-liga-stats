import os, glob

from bs4 import BeautifulSoup 
import pandas as pd

from algorithms import generate_transitional_growth

def open_html_file(path: str):
    """
    Returns soup. Help yourself.
    """
    with open(path) as f:
        #read File
        content = f.read()
        #parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        daytime = path.split("/")[-1][6:8]
        
        return soup, daytime

def create_csv_from_soup(soup, daytime: str):
    tables = soup.findAll("table")
    for index, table in enumerate(tables):
        elements = table.findAll("td")
        big_list = []
        
        no_samples = int(len(elements)/4)

        for x in range(no_samples):
            new_list = [f"{elements[2+x*4].text} {elements[1+x*4].text}",  elements[3+x*4].text]
            big_list.append(new_list)

        if(index):
            df = pd.DataFrame(big_list, columns=['Name', 'Points'])
            df.to_csv(f'data/csv/f{daytime}.csv',index_label='Id')
        else:
            df = pd.DataFrame(big_list, columns=['Name', 'Points'])
            df.to_csv(f'data/csv/m{daytime}.csv', index_label='Id')

def get_unique_list_of_names(male: bool, max_value: int):
    if(male):
        sex = 'm'
    else:
        sex = 'f'

    unique_names = set()
    for x in range(4,max_value):
        if(x<10):
            filename = f"data/csv/{sex}0{x}.csv"
        else:
            filename = f"data/csv/{sex}{x}.csv"
        df = pd.read_csv(filename, index_col='Id')
        for row in df['Name']:
            unique_names.add(row)

    return list(unique_names)

def get_list_of_points_for_athlete(athlete_name: str, male: bool, max_value: int) -> list:
    if(male):
        sex = 'm'
    else:
        sex = 'f'

    points_list = []
    
    for x in range(4, max_value):
        if(x<10):
            filename = f"data/csv/{sex}0{x}.csv"
        else:
            filename = f"data/csv/{sex}{x}.csv"
        df = pd.read_csv(filename, index_col='Name')
        try:
            value = df.loc[athlete_name, 'Points']
        except:
            value = 0
        points_list.append(value)
    return points_list

def estimate_transitional_values(values_list: list):
    huge_values_list = []

    for index, _ in enumerate(values_list):
        if(index == len(values_list) - 1):
            break
        start_value = values_list[index]
        stop_value = values_list[index+1]
        new_list = generate_transitional_growth(start_sample=start_value, stop_sample=stop_value)
        huge_values_list.extend(new_list)
        
    huge_values_list.append(values_list[-1])
    return huge_values_list

def generate_datetime_list(start_time, end_time):
    return pd.date_range(start=start_time, end=end_time, freq='H')
    
def convert_html2csv():
    path = 'data/html/'
    for filename in glob.glob(os.path.join(path, '*.html')):
        soup, daytime = open_html_file(filename)
        create_csv_from_soup(soup, daytime)

def create_main_csv(male: bool, max_value: int):
    unique_names = get_unique_list_of_names(male, max_value)

    my_dict = { name : estimate_transitional_values(get_list_of_points_for_athlete(name, male,max_value)) for name in unique_names }
    df = pd.DataFrame(my_dict)
    df['time'] = generate_datetime_list('2023-01-04 14:00:00', '2023-01-28 14:00:00')
    df_i = df.set_index('time')
    if(male):
        df_i.to_csv("data/main_csv/m.csv", index=False)
    else:
        df_i.to_csv("data/main_csv/f.csv", index=False)

    
    
        
        
    

            
            
            

