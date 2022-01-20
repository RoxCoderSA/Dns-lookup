import socket #Importing library socket 
import argparse #Importing library arg

print(''' 

 /$$$$$$$                             /$$                     /$$                          
| $$__  $$                           | $$                    | $$                          
| $$  \ $$ /$$$$$$$   /$$$$$$$       | $$  /$$$$$$   /$$$$$$ | $$   /$$ /$$   /$$  /$$$$$$ 
| $$  | $$| $$__  $$ /$$_____//$$$$$$| $$ /$$__  $$ /$$__  $$| $$  /$$/| $$  | $$ /$$__  $$
| $$  | $$| $$  \ $$|  $$$$$$|______/| $$| $$  \ $$| $$  \ $$| $$$$$$/ | $$  | $$| $$  \ $$
| $$  | $$| $$  | $$ \____  $$       | $$| $$  | $$| $$  | $$| $$_  $$ | $$  | $$| $$  | $$
| $$$$$$$/| $$  | $$ /$$$$$$$/       | $$|  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/| $$$$$$$/
|_______/ |__/  |__/|_______/        |__/ \______/  \______/ |__/  \__/ \______/ | $$____/ 
                                                                                 | $$      
                                                                                 | $$      
                                                                                 |__/   @RoxCoderSA

''')

#Create varble call parser and adding description of script
parser=argparse.ArgumentParser(description="Ths script help user get ip adderss of websites")
#Printing description of and help option
parser.print_help()
#Add argument for parser that call host
parser.add_argument( "-H" , "--host" , help="enter the website" , type=str)
#Assgin parser value to args varble 
args=parser.parse_args()

#Chack the value from user if the user writing host or not 
if args.host:
    args.host = args.host.replace("https://" , "") # remove https://
    args.host = args.host.replace("http://" , "") #remove http://
    args.host = args.host.replace("/" , "") #remove /
    print("\n")#newline for space
    print( "IP Address: " + socket.gethostbyname(args.host)) #call the function gethostbyname to get IP Adderss of website the user entered
    print("\n") #newline for space
    #Exit from script 
    exit(0)

def website_ipAdderss(): # create function to get ip address
    URL = input("Enter website URL : ") #enter the website from userS
    URL = URL.replace("https://" , "") #remove https://
    URL = URL.replace("http://" , "") #remove http://
    URL = URL.replace("/" , "") #remove /
    print("\n")#newline for space
    print("IP Address: " + socket.gethostbyname(URL)) #call the function gethostbyname to get IP Adderss of website the user entered
    print("\n") #newline for space
website_ipAdderss() #call the function to start script