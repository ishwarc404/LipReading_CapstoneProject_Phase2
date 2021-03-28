import pandas as pd 
import matplotlib.pyplot as plt
from frechetdist import frdist

dataset_parent_path = "datasets/"

datasets = ["hello_vertical_data","bye_vertical_data","hello_horizontal_data","bye_horizontal_data","hello_data","bye_data"]



def similarityIndex(prediction_list):
    datasets = ["datasets/hello_vertical_data.csv" , "datasets/bye_vertical_data.csv" ]
    master_list = []
    row_counts = {}
    for eachdataset in datasets:
        count = 0
        df = pd.read_csv(eachdataset, index_col=[0])
        df_list = df.values.tolist()
        for eachrow in df_list:
            temp = eachrow
            temp.insert(0,eachdataset.split('/')[1].split('_')[0])
            master_list.append(temp)
            count+=1
        row_counts[eachdataset.split('/')[1].split('_')[0]] = count
    
    #now we have the master list ready
    #now we need to check the similarityif the prediction list

    #now lets calculate the frechet distance of each of the test rows with each of the train rows
    processed_predlist = []
    for k in range(0,len(prediction_list)):
        processed_predlist.append([k,prediction_list[k]])
    
    processed_masterlist = []
    for each in master_list:
        temp = []
        for k in range(0,len(prediction_list)):
            temp.append([k,each[k+1]])
        temp.insert(0,each[0])
        processed_masterlist.append(temp)

    avg_distances = []
    # print(len(master_list[0]))
    # print(len(prediction_list))
    for each_test in processed_masterlist:
        verdict = each_test[0]
        each_test.remove(verdict)
        distances = []
        # print(each_test[0:len(prediction_list)])
        # print(prediction_list)
        distances.append(frdist(each_test,processed_predlist))
        avg_distances.append((verdict,sum(distances)/len(distances)))
    
    print("\nFinal results are: ")
    key = {}
    for each in avg_distances:
        if(each[0] in key):
            key[each[0]] += each[1]
        else:
            key[each[0]] = each[1]
    
    # print(key)
    # print(row_counts)
    results = []
    # for each in key.keys():
    #     results.append([each,key[each]/row_counts[each]])
    #     print("AVG DISTANCE {} = {}".format(each,key[each]/row_counts[each]))

    
    results = sorted(results,key = lambda x: x[1])
    
    return results[0][0]
