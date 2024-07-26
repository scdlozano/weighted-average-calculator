#Defining empty lists for user inputted values and weights to be appended
values = []
weights = []

#Main function controls the control flow
def main():
#Initializes the first yes value
    yes_value = ask_yes_value()
    if yes_value == "YES":
        while yes_value == "YES":
            input_values()
            yes_value = ask_yes_value()
        weighted_average = calculate_weighted_average()
        print_weighted_average(weighted_average)
    else:
        print("DONE")

#Decomposed functions
def ask_yes_value():
    yes = str(input("Do you want to add a number? Type YES if so.: "))
    return yes

def input_values():
    value = float(input("Please input a number: "))
    values.append(value)
    weight = float(input("Please input this number's weight: "))
    weights.append(weight)

def calculate_weighted_average():
    value_weight_product = sum((v * w) for v, w in zip(values, weights))
    weight_sum = float(sum(weights))
    weighted_average = float(value_weight_product) / float(weight_sum)
    return weighted_average
    
def print_weighted_average(weighted_average):
    print("Weighted average: ", weighted_average)
    print("Length of values list: ", len(values))
    print("Length of values list: ", len(weights))
    
if __name__ == '__main__':
    main()