from datetime import datetime

path='C:\Windows\System32\drivers\etc\hosts'
address='127.0.0.1'

web_list=["www.facebook.com","www.instagram.com"]

start_date=datetime(2020,8,8)
end_date=datetime(2020,8,9)
present_date=datetime(datetime.now().year,datetime.now().month,datetime.now().day)

while True:
    if start_date<=present_date<end_date:
        with open(path,"r+") as file:
            content=file.read()
            for site in web_list:
                if site in content:
                    pass
                else:
                    file.write(address+" "+site+"\n")
        print("All sites are blocked")
        break
    else:
        with open(path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in web_list):
                    file.write(line)
            file.truncate()
        print("All sites are unblocked")
        break
