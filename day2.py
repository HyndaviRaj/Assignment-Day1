def remove_items(num_list, item):
      
    for i in num_list:
        if(i == item):
            num_list.remove(i)
  
    return num_list
  

if __name__=="__main__":
      
    num_list = [1, 3, 4, 6, 5, 4]
  
    item = int(input('enter value to be removed: '))
  
    print ("Given list is : " + str(num_list))
  
    res = remove_items(num_list, item)
  
    print ("after performing the remove operation : " + str(res))