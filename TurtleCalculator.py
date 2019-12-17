from turtle import *
from math import *


def shape(numberEdge,sizeEdge):
    n=numberEdge

    for i in range(n):
        forward(sizeEdge)
        left(360/n)



def sketch_shape(result_cal,number_edges,size_edge,gap_shape):
    x=0
    y=0

    a=ceil(result_cal**0.5)
    counter=0
    
    for row in range(a):
        for column in range(a):
            if counter>=result_cal:
                break
                
            else:
                pendown()
            
            shape(number_edges,size_edge)
            penup()
            x=x+(size_edge+gap_shape)
            goto(x,y)
            pendown()
            counter=counter+1

        penup()
        x=x-((a-1)*(size_edge+gap_shape)+(size_edge+gap_shape))
        y=y-(size_edge+gap_shape)
        goto(x,y)
        pendown()
        
        
       
def examine_val(result_val,num_edges_val,edge_size_val,shape_gap_val):
    if result_val < 0 :
        return "Result is less than zero. You cannot sketch this shape!"
    else:
        sketch_shape(result_val,num_edges_val,edge_size_val,shape_gap_val)


def turtle_calculator(number1,number2,operation, num_edges,edge_size,shape_gap):
    if operation == "add":
        
        result = number1+number2
        
        return examine_val(result,num_edges,edge_size,shape_gap)

    elif operation == "subtract":

        result=number1-number2

        return examine_val(result,num_edges,edge_size,shape_gap)

    elif operation == "multiply":

        result=number1*number2

        return examine_val(result,num_edges,edge_size,shape_gap)

    elif operation == "divide":

        if number2==0:
            return "Zero Division Error!"
        else:
            result=number1/number2
            return examine_val(result,num_edges,edge_size,shape_gap)
        





    
        
        
        
