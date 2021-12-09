import socket #Importing library socket 
import argparse #Importing library argparse

print("""
       8888888 8888888b.                          d8888      888      888                                    
         888   888   Y88b                        d88888      888      888                                    
         888   888    888                       d88P888      888      888                                    
         888   888   d88P                      d88P 888  .d88888  .d88888  .d88b.  888d888 .d8888b  .d8888b  
         888   8888888P"                      d88P  888 d88" 888 d88" 888 d8P  Y8b 888P"   88K      88K      
         888   888             888888        d88P   888 888  888 888  888 88888888 888     "Y8888b. "Y8888b. 
         888   888                          d8888888888 Y88b 888 Y88b 888 Y8b.     888          X88      X88 
       8888888 888                         d88P     888  "Y88888  "Y88888  "Y8888  888      88888P'  88888P'   @Roxcoder                                                                                          
""")

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
    print("\n")#newline for space
    print(socket.gethostbyname(args.host)) #call the function gethostbyname to get IP Adderss of website the user entered
    print("\n") #newline for space
    #Exit from script 
    exit(0)

def website_ipAdderss(): # create function to get ip address
    URL = input("Enter website URL : ") #enter the website from userS
    print("\n")#newline for space
    print(socket.gethostbyname(URL)) #call the function gethostbyname to get IP Adderss of website the user entered
    print("\n") #newline for space
website_ipAdderss() #call the function to start script