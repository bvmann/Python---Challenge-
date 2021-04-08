import os 
import csv 
import statistics

poll_path = os.path.join('Resources','election_data.csv')

with open(poll_path) as pollcsv : 
    csvreader = csv.reader(pollcsv, delimiter=',')
    next(csvreader, None) 
    
    main=[]
    candidate=[]
    candidate2=[]
    candidate0count=0
    candidate1count=0
    candidate2count=0
    candidate3count=0
    for row in csvreader : 
        #main.append(row)
        candidate.append(row[2])
       
    
    #print(len(main))
    #print(main[1])
    #print(len(candidate))
    #print(candidate)
    votes_cast=(len(candidate))
    candidate_name=(set(candidate))
    for x in candidate_name :
        candidate2.append(x)
   
    print(candidate_name)
    print(candidate2[1])

    for x in candidate: 
        if x==candidate2[0]:
            candidate0count+=1
        elif x==candidate2[1]:
            candidate1count+=1
        elif x==candidate2[2]:
            candidate2count+=1
        elif x==candidate2[3]:
            candidate3count+=1

            
    print(candidate0count)
    print(candidate1count) 
    print(candidate2count)
    print(candidate3count)    
    percentwonc0=candidate0count/votes_cast
    print(percentwonc0)

    print(f'{candidate2[1]}', " : ")

    print(statistics.mode(candidate))