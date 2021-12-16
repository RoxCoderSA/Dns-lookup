import socket #Importing library socket 
import argparse #Importing library arg

print('''

88 88""Yb             db    8888b.  8888b.  88""Yb 888888 .dP"Y8 .dP"Y8 
88 88__dP ________   dPYb    8I  Yb  8I  Yb 88__dP 88__   `Ybo." `Ybo." 
88 88"""  """"""""  dP__Yb   8I  dY  8I  dY 88"Yb  88""   o.`Y8b o.`Y8b 
88 88              dP""""Yb 8888Y"  8888Y"  88  Yb 888888 8bodP' 8bodP' @Roxcoder

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
    print(socket.gethostbyname(args.host)) #call the function gethostbyname to get IP Adderss of website the user entered
    print("\n") #newline for space
    #Exit from script 
    exit(0)

def website_ipAdderss(): # create function to get ip address
    URL = input("Enter website URL : ") #enter the website from userS
    URL = URL.replace("https://" , "") #remove https://
    URL = URL.replace("http://" , "") #remove http://
    URL = URL.replace("/" , "") #remove /
    print("\n")#newline for space
    print(socket.gethostbyname(URL)) #call the function gethostbyname to get IP Adderss of website the user entered
    print("\n") #newline for space
website_ipAdderss() #call the function to start script