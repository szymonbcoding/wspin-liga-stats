# Input: 1 html file 
# Output: 2 csv files {sex}{day}
# 
from bs4 import BeautifulSoup 

if __name__ == '__main__':
    with open('data/20230104-200203.html') as f:
        #read File
        content = f.read()
        #parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        #print Title tag
        print(soup.title) 
    
    tables = soup.findAll("table")
    for table in tables:
        elements = table.findAll("td")
        no_samples = int(len(table)/4)
        for x in range(no_samples):
            new_tuple = ()

            
            
            

