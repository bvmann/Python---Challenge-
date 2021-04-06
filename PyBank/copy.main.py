import os
import csv 

bank_path = os.path.join("Resources","pybank.csv") 



with open(bank_path) as bankcsv: 
 csvreader= csv.reader(bankcsv, delimiter=',')
 next(csvreader, None) 
 netprofit=0
 dates = 0
 change = 0
 greatestincrease = []
 greatestdecrease = []
 profits_loss = []
 
 for x in csvreader:
   profits_loss.append(int(x[1]))
change-=int(x[1])
print(change)
#print(profits_loss)
netprofit = sum(profits_loss)
print(netprofit)

   
   
 
  # dates=dates+(len(list(csvreader)))
   #netprofit += int(row[1])    
   #change -=int(x[1])
   #avg_change=int(change/dates)
   #greatestincrease.append(x[1])
   #greatestdecrease.append(x[1])
      
 
   #print(row[1])
   #print(netprofit)
   #print(greatestdecrease)
     
   # for z in csvreader: 
    #    change -=int(x[1])
     #   avg_change=int(change/int(len(list(csvreader)))
      #      print(avg_change) 





