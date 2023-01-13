#this web scraper will return price for the ASUS rtx 4090 graphics cards on newegg
def web_scraper():
    import requests
    from bs4 import BeautifulSoup as bs
    
    #load web page content
    walmart = requests.get("https://www.newegg.com/asus-geforce-rtx-4090-rog-strix-rtx4090-o24g-gaming/p/N82E16814126593?quicklink=true")

    #convert to bs object
    doc = bs(walmart.text, "html.parser")
    price = doc.find_all(text="$")
    stock = doc.find_all(text="stock")
    parent = price[0].parent
    strong = parent.find("strong")
    return(f"The current price for the ASUS RTX 4090 graphics card on NewEgg is {strong.string}$")



        
def price_check(sender: str, password: str):
    from email.message import EmailMessage
    import ssl, smtplib

    subscribers = ""

    subject = "Graphics Card Price RTX 4090"
    body = web_scraper()

    message = EmailMessage()
    message["From"] = sender
    message["To"] = subscribers
    message["Subject"] = subject
    message.set_content(str(body))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, subscribers, message.as_string())



if __name__=="__main__":

    price_check("","")