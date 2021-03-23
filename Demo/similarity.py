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

    # for i in range(0,len(avg_distances_correct)):
    #     if(avg_distances_correct[i] < avg_distances_incorrect[i]):
    #         count_correct +=1

    #     print(" {} \t {} \t \t{} ".format(i,avg_distances_correct[i],avg_distances_incorrect[i]))
    # print("\n")
    # print("Total avg correct: ", sum(avg_distances_correct)/len(avg_distances_correct))
    # print("Total avg incorrect: ", sum(avg_distances_incorrect)/len(avg_distances_incorrect))
    # print("Total correct predictions: ",count_correct)
    # print("Percentage of correct predictions: ", count_correct*100/len(avg_distances_correct))

# similarityIndex([0.09334070869305827, 0.08800246410349284, 0.09838974596144753, 0.0, 0.06222713912870551, 0.11218157042698963, 0.09334070869305827, 0.08800246410349284, 0.04400123205174642, 0.06957205656856127, 0.06957205656856127, 0.15864869834616124, 0.6908333562015215, 0.8452360662823337, 1.0, 0.9665258991095709, 0.47083374382811854, 0.18925645512987202, 0.2200061602587321, 0.2817453554274446, 0.3172973966923225, 0.15864869834616124, 0.18668141738611654, 0.031113569564352756, 0.0, 0.031113569564352756, 0.0, 0.06957205656856127, 0.04400123205174642, 0.06957205656856127, 0.06957205656856127, 0.031113569564352756, 0.08800246410349284, 0.06957205656856127])
# similarityIndex([0.05050762722761054, 0.03571428571428571, 0.05050762722761054, 0.05050762722761054, 0.03571428571428571, 0.03571428571428571, 0.07142857142857142, 0.07142857142857142, 0.05050762722761054, 0.03571428571428571, 0.0, 0.05050762722761054, 0.03571428571428571, 0.0, 0.03571428571428571, 0.05050762722761054, 0.03571428571428571, 0.03571428571428571, 0.05050762722761054, 0.05050762722761054, 0.07985957062499249, 0.11293848786315641, 0.0, 0.14285714285714285, 0.3234066120763363, 0.430056949242582, 0.5, 0.5725435550671928, 0.7151780140893138, 0.7857142857142857, 0.8571428571428571, 0.893571143085486, 0.8214285714285714, 0.8928571428571429, 0.8578865821045938, 0.8578865821045938, 1.0, 0.9649468632933068, 0.8578865821045938, 0.8578865821045938, 0.8214285714285714, 0.893571143085486, 0.9285714285714286, 0.8222046023729527, 0.8928571428571429, 0.643848442047141, 0.5714285714285714, 0.5012738874149357, 0.3589241293257461, 0.3292694449033174, 0.2525381361380527, 0.29450754468697576, 0.29450754468697576, 0.22587697572631282, 0.2879377767249482, 0.3234066120763363, 0.2600039246171614, 0.3292694449033174, 0.22587697572631282, 0.3589241293257461, 0.2719918966379967, 0.2525381361380527, 0.29450754468697576, 0.33881546358946923, 0.2525381361380527, 0.2600039246171614, 0.2525381361380527, 0.3944771791852593, 0.5050762722761054, 0.430056949242582, 0.3944771791852593, 0.3234066120763363, 0.2600039246171614, 0.15971914124998499, 0.11293848786315641, 0.03571428571428571, 0.03571428571428571, 0.07985957062499249, 0.03571428571428571, 0.05050762722761054, 0.07985957062499249, 0.03571428571428571, 0.07985957062499249, 0.07142857142857142, 0.07985957062499249, 0.05050762722761054, 0.07985957062499249, 0.03571428571428571, 0.11293848786315641, 0.03571428571428571])



#always pass hello_vertical_correct and bye_vertical_correct together
#always pass hello_horizontal_correct and bye_horizontal_correct together
#always pass hello_data and bye_data together
# print("VERTICAL DATA EDA:")
# similarityIndex( dataset_parent_path  + datasets[0] + ".csv" , dataset_parent_path  + datasets[1] + ".csv" )
# print("\n\n------------------------------------------------------------------------------------")
# print("HORIZONTAL DATA EDA:")
# similarityIndex( dataset_parent_path  + datasets[2] + ".csv" , dataset_parent_path  + datasets[3] + ".csv" )
# print("\n\n------------------------------------------------------------------------------------")
# print("AREA DATA EDA:")
# similarityIndex( dataset_parent_path  + datasets[4] + ".csv" , dataset_parent_path  + datasets[5] + ".csv" )
