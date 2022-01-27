from bs4 import BeautifulSoup
import requests
from tkinter import *






root = Tk()
root.geometry('500x400')
cityNameLabel = Label(root, text='please enter your city name')
cityNameLabel.pack()
cityNameEntry = Entry(root)
cityNameEntry.pack()
degreeLabel = Label(root, text='please choose').pack()
choosed = StringVar()
choosed.set('choose')


def save():
    global city
    global value
    city = cityNameEntry.get()
    value = choosed.get()
    procces()

degreeMenu = OptionMenu(root, choosed, "Celsius", "Farenheit")
degreeMenu.pack()

def procces():
    address = '''
    https://www.google.com/search?rlz=1C1CHBF_enIR891IR891&sxsrf=ALeKk03m9OMWKOC2j_DtHgAfvdyH4BmfXQ%3A1594136371743&ei=M5cEX-PtLMLikgXfmoGgCw&q=weather+{}+{}&oq=weather+{}+{}&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeUJFTWMBXYMhZaABwAHgAgAHgAYgB8QmSAQMyLTaYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwij06ThvLvqAhVCsaQKHV9NALQQ4dUDCAw&uact=5
    '''.format(city,value,city,value)
    source = requests.get(address)
    soup = BeautifulSoup(source.content, 'html.parser')
    global cityName, date, degree
    cityName = soup.find('span', class_='BNeawe tAd8D AP7Wnd')
    date = soup.find('div', class_='BNeawe tAd8D AP7Wnd')
    degree = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
    status()
    


def myDelete():
    try:
        weatherStatus.destroy()
        
    except Exception:
        labelError.destroy()
    confirmButton['state']=NORMAL
    deleteButton['state']= DISABLED
        
            
def status():
    global weatherStatus
    try:
        weatherStatus = Label(root, text="the weather in {} on {} is {}".format(cityName.text,date.text,degree.text))
        weatherStatus.pack()
    except Exception:
        global labelError
        labelError= Label(root, text='city not found')
        labelError.pack()
    confirmButton['state']=DISABLED
    deleteButton['state']= NORMAL
    
        

confirmButton = Button(root, text='Confirm', command=save)
confirmButton.pack()
deleteButton = Button(root, text='Delete',  command=myDelete)
deleteButton.pack()
root.mainloop()
