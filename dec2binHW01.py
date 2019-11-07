## Made by Ertan Özdemir - Computational Thinking HW01 | 11.2019 ##


def bin2dec(binary_val):


    a = str(binary_val)
    a = a[::-1]

    binary_list=[]
    counter=0
    dec_val=0
    

    for i in a:
        binary_list.append(i)
        
        

    lenghtOfValue=len(binary_list)
    

    while lenghtOfValue>=1:


        if binary_list[counter]=="1":

            lenghtOfValue=lenghtOfValue-1
            dec_val=dec_val+(2**(counter))
            counter=counter+1
            
           
        elif binary_list[counter]=="0":
            lenghtOfValue=lenghtOfValue-1
            counter=counter+1
            

        else:
            print("Wrong Number")
            break
    print(dec_val)

    
            
        

    
