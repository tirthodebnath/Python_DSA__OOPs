a = "Good_Morning 12345 !@#!@#"
count_item = {}

for i in a:
    if i in count_item:
        count_item[i] +=1
    else:
        count_item[i] =1
        
print(count_item) 