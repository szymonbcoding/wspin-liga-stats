# Input: 1 html file 
# Output: 2 csv files {sex}{day}
# 
import os, glob

from bs4 import BeautifulSoup 
import pandas as pd

from algorithms import get_samples_step_function

def open_html_file(path: str):
    """
    Returns soup.
    """
    with open(path) as f:
        #read File
        content = f.read()
        #parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        daytime = path.split("/")[-1][6:8]
        
        return soup, daytime

def create_csv_from_soup(soup, daytime):
    tables = soup.findAll("table")
    print(tables)
    for index, table in enumerate(tables):
        elements = table.findAll("td")
        big_list = []
        
        print(elements)
        no_samples = int(len(elements)/4)
        print(len(elements))
        print(no_samples)
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
    
    max_value = 27 #finally should be 29
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
        huge_values_list.extend(get_samples_step_function(start_sample=start_value, stop_sample=stop_value))
        
    huge_values_list.append(values_list[-1])
    return huge_values_list
    
    

if __name__ == '__main__':

    M_UNIQUE_NAMES = get_unique_list_of_names(True, 27)
    F_UNIQUE_NAMES = get_unique_list_of_names(False, 27)

    # convert data from html files to csv files
    # path = 'data/html/'
    # for filename in glob.glob(os.path.join(path, '*.html')):
    #     soup, daytime = open_html_file(filename)
    #     create_csv_from_soup(soup, daytime)

    # get list of unique female and male athletes
    print(len(M_UNIQUE_NAMES))
    print(len(F_UNIQUE_NAMES))

    # df = pd.DataFrame(big_list, columns=['Name', 'Points'])
    # df.to_csv(f'data/csv/m{daytime}.csv', index_label='Id')

    # male_dict = { name : estimate_transitional_values(get_list_of_points_for_athlete(name, True,27)) for name in ['Szymon Balawajder'] }
    male_dict = { name : get_list_of_points_for_athlete(name, True, 27) for name in ['Szymon Balawajder']}
    # df_male = 
    # female_dict = { name : get_list_of_points_for_athlete(name, False,27) for name in F_UNIQUE_NAMES }
    # a = get_list_of_points_for_athlete('Szymon Balawajder', True, 27)
    print(male_dict)
    # print(female_dict)
    # df.to_csv()
    # 
    
    
        
        
    

            
            
            

