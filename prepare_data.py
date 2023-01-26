# Input: 1 html file 
# Output: 2 csv files {sex}{day}
# 
import os, glob

from bs4 import BeautifulSoup 
import pandas as pd

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
    for index, table in enumerate(tables):
        elements = table.findAll("td")
        big_list = []
        no_samples = int(len(table)/4)
        for x in range(no_samples):
            new_list = [f"{elements[2+x*4].text} {elements[1+x*4].text}",  elements[3+x*4].text]
            big_list.append(new_list)

        if(index):
            df = pd.DataFrame(big_list, columns=['Name', 'Points'])
            df.to_csv(f'data/csv/f{daytime}.csv',index_label='Id')
        else:
            df = pd.DataFrame(big_list, columns=['Name', 'Points'])
            df.to_csv(f'data/csv/m{daytime}.csv', index_label='Id')

if __name__ == '__main__':

    # 
    path = 'data/html/'
    for filename in glob.glob(os.path.join(path, '*.html')):
        soup, daytime = open_html_file(filename)
        create_csv_from_soup(soup, daytime)
    
        
        
    

            
            
            

