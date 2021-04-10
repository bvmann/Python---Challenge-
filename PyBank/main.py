import os
import csv 
import sys 

bank_path = os.path.join("Resources","pybank.csv") 
naturalpath = sys.stdout 

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

   
 for x in csvreader:
   main.append(x)
   profits_loss.append(int(x[1]))
 dates=len(profits_loss)

rate_change2=round((int(max(enumerate(profits_loss))[1])-int(min(enumerate(profits_loss))[1]))/(dates-1),2)


netprofit = sum(profits_loss)

smallchange=str(min(profits_loss))
bigchange=str(max(profits_loss))

for i in main: 
  if i[1]==bigchange :
     greatestincrease1 = i 
  elif i[1]==smallchange : 
    greatestdecrease1 = i  
     

print('Financial Analysis')
print('---------------------')
print("Total months: ",(dates))
print('Total',"$",(netprofit))
print('Average Change: ','$',(rate_change2))

print('Greatest Increase in Profits: ',(greatestincrease1))
print('Greatest Decrease in Profits: ',(greatestdecrease1))
sys.stdout=open('analysis\_bankanalysis1.txt','w')

print('Financial Analysis')
print('---------------------')
print("Total months: ",(dates))
print('Total',"$",(netprofit))
print('Average Change: ','$',(rate_change2))
print('Greatest Increase in Profits: ',(greatestincrease1))
print('Greatest Decrease in Profits: ',(greatestdecrease1))

  





