# if __name__ == '__main__':
#     N = int(input())
#     list=[]
#     argument=input()
#     def switcher_demo(argument):
#         switcher={
#             "insert":insert_list()
#         }
#         print switcher.get(argument,"invalid option")
        
    
    
#     print_list()
#     list_remove()
#     list_append()
#     list_sort()
#     print_list()
#     list_pop()
#     list_reverse()
#     print_list()
    
    
       
# def insert_list():
#     i=int(input())
#     e=int(input())
#     list.insert(i,e)
    
# def print_list():
#     print(list)

# def list_append(e):
#     # for i in range(0,N):
#     #     e=int(input())
#         e=int(input())
#         list.append(e)

# def list_pop():
#     list.pop()
    
# def list_sort():
#     list.sort()

# def list_reverse():
#     list.reverse()

# def list_remove():
#     e=int(input())
#     list.remove(e)
    
def one():
    return "January"
 
def two():
    return "February"
 
def three():
    return "March"
 
def four():
    return "April"
 
def five():
    return "May"
 
def six():
    return "June"
 
def seven():
    return "July"
 
def eight():
    return "August"
 
def nine():
    return "September"
 
def ten():
    return "October"
 
def eleven():
    return "November"
 
def twelve():
    return "December"
 
 
def numbers_to_months(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }
    # Get the function from switcher dictionary
    
   
    print(switcher.get(argument, lambda: "Invalid month"))
    # Execute the function
    

option=input("Enter the option:")
numbers_to_months(option)