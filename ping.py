# Developed by Lateraluz++
# 07-02-2022



from ping3 import ping
import csv
import sys
import subprocess
import os
import time
import socket



def get_hosts_list():
    
    start_time = time.time()


    index = 0
    rows =[]

    file = open("systems2.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    #print(header)
    replace = []
    no_replace = []
    
    print("Begin Analizys !")
    for row in csvreader:        
        index= index + 1   
        #print("Procesando "+str(row[3]))
        if row[3] != "":     
            response = ping(row[3], timeout=10)         
            if type(response) is float:               
                hostname = get_hostname(row[3])
                replace.append(str(row[3])+"-"+str(hostname))
                print(row[3] + " " +str(response) + " "+str(hostname))
            elif type(response) is type(None):            
                print(row[3] + " " +str(response))
                no_replace.append(str(row[3])+"-"+str(row[0]))
            else:
                print(row[3] + " " +str(response))  
                no_replace.append(str(row[3])+"-"+str(row[0]))      
            
    
    file.close()

    #Show Responsers
    print("Responsers")    
    print("-------------------------------------------------------------------")
    for row in replace:
        print(row)

    print("NO Responsers ")    
    print("-------------------------------------------------------------------")
    for row in no_replace:
        print(row)   

    end_time = time.time()
    time_elapsed = (end_time - start_time)

    print("-------------------------------------------------------------------")
    print("Time elapsed:  "+str(time_elapsed)+" seg")

def is_alive_ip(host):
    print(host +" " +str(ping( host, timeout=5)))      


def get_hostname(ip):
 
    try:
        host = socket.gethostbyaddr(ip)
        return host
    except:
        return "*** It doesnt detect network Full Name ***"    



 
def cls():
    os.system('cls' if os.name=='nt' else 'clear') 

def main():  


    cls()     
    #is_alive_ip("192.168.120.11")
    get_hosts_list()
     
     
     
if __name__ == "__main__":
    main()
    
