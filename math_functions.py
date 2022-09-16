def trial_div3(number: int):
    #Check for bad input
    if number in [1,0] or number < 0 or type(number) != int:
        return(["Erroneous input"])
    
    #Perform the trial division
    startnum = number
    factors = []
    f = 2
    while f * f <= number:
        if number % f == 0:
            factors.append(f)
            number = int(number/f)
        else:
            f += 1
    
    if number != 1: factors.append(number)

    if len(factors) == 1:
        return([str(number) + " is a prime!"])
    
    #Group by factor. Example 180 = 2^2 * 3*2 * 5^1: [[2,2], [3,2], [5,1]]
    unique_factors = list(set(factors))
    grouped_factors = [[i, factors.count(i)] for i in unique_factors]

    #Create output message
    message = str(startnum)
    if len(grouped_factors) == 1 and grouped_factors[0][1] == 1:
        message += " is prime!"
    elif len(grouped_factors) == 1 and grouped_factors[0][1] != 1:
        message += " = " + str(grouped_factors[0][0]) + "^" + str(grouped_factors[0][1])
    else:
        message += " ="

        for i in grouped_factors:
            message += " *" if i != grouped_factors[0] else ""
            message += " " + str(i[0]) + str("" if i[1] == 1 else ("^" + str(i[1])))
    
    #return(grouped_factors, message)
    return([message])


#for i in [5040,30,14,10,100,7,5,3,2,31,1,0,25,9]:
#    print(str(trial_div3(i)[0]))