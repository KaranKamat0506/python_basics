def substrDeletion(string, length) : 
  
    # To store the count of 0s and 1s  
    count0 = 0; 
    count1 = 0;  
  
    for i in range(length) : 
        if (string[i] == '0') : 
            count0 += 1;  
        else : 
            count1 += 1;  
  
    return min(count0, count1);  
  
# Driver code  
if __name__ == "__main__" : 
  
    string = "0100100111";  
    length = len(string);  
      
    print(substrDeletion(string, length));  



   
