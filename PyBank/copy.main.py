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
 main=[]

   #
 for x in csvreader:
   main.append(x)
   profits_loss.append(int(x[1]))
 dates=len(main)
change-=int(x[1])
#rate_change=change/dates
rate_change2=(int(max(enumerate(profits_loss))[1])-int(min(enumerate(profits_loss))[1]))/dates
print("number of days ",(dates))
print(change)
#print(profits_loss)
print(rate_change)
print(rate_change2)
netprofit = sum(profits_loss)
print(netprofit)
#print(main)
smallchange=str(min(profits_loss))
bigchange=str(max(profits_loss))
print(max(profits_loss))
print(min(profits_loss))
  
for i in main: 
   if i[1]==bigchange :
    print(i)
#for i in main:
   elif i[1]==smallchange : 
      print(i)

   #maybe make a date list and zip the list with profits_loss 
   
 
  # dates=dates+(len(list(profits_loss)))
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





