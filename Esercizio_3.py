
def sum_csv(file_name):
    values = []
    my_file = open(file_name, 'r')
    
    for line in my_file:
        
        elements = line.split(',')
        
        if elements[0] != 'Date':
            
            date = elements[0]
            value = float(elements[1])

            values.append(value)

    print(values)
    
    sumlist = sum(values)
    print(sumlist)
    
    my_file.close()

sum_csv("shampoo_sales.csv")

    
