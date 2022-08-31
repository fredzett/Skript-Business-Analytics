from bs4 import BeautifulSoup
from glob import glob

def find_prev(soup):
    el = soup.find("a", {"class":"left-prev"})
    if el: 
        el = el.find("p", {"class": "prev-next-subtitle"})
        if el:
            el = el.find(text="previous")
            if el:
                el.replace_with("zurück")
        else:
            return None
    else: 
        return None 

def find_next(soup):
    el = soup.find("a", {"class":"right-next"})
    if el: 
        el = el.find("p", {"class": "prev-next-subtitle"})
        if el:
            el = el.find(text="next")
            if el:
                el.replace_with("weiter")
        else:
            return None
    else: 
        return None 

files = glob("./Skript-Business-Analytics/_build/html/chapters/**/*.html", recursive=True)

for file in files:
    print(file)
    
    # open html
    html = open(file)

    # convert to soup
    soup = BeautifulSoup(html, "html.parser")

    # Replace previous and next
    #find_prev(soup)
    #find_next(soup)

    # Replace "Dieses Buch durchsuchen"
    #soup.find("input").attrs["placeholder"] = "Durchsuchen..."
 
    # Save (i.e. overwrite existing file)
    with open(file, "w") as f_output:
        f_output.write(str(soup))#.prettify("utf-8")) 