import os,sys
from test_automate_fun import facematch
import json
from itertools import permutations

folder = "test samples"
results={}
for folder_sub in os.listdir(folder):
    subpath = "C:/drive/internships/intainai/face_match/test samples/"+folder_sub
    input_path=[]
    for filename in os.listdir(subpath):
        filename = "C:/drive/internships/intainai/face_match/test samples/"+folder_sub+"/"+filename
        input_path.append(filename)
    print(input_path)
    
    images_cnt = len(input_path)
    if images_cnt==2:
        results[folder_sub]=facematch(input_path[0],input_path[1])
    else:
        perm = permutations(input_path, 2)
        cnt=1
        for combinations in list(perm):
            combination = list(combinations)
            #print(combination)
            key=folder_sub+str(cnt)
            cnt=cnt+1
            results[key]=facematch(combination[0],combination[1])

        
print(results)
with open("sample.json", "w") as outfile:  
    json.dump(results, outfile) 