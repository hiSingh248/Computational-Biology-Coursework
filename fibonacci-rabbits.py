def fibonacciRabits(n, m,initialState):
    months = 2
    while (months < n):
        #before rabbits start dying
        if (months < m):
            totalRabbits=initialState[-2] + initialState[-1]
        #count of rabbits after death in a month
        elif (months == m or months == m+1):
             
            totalRabbits=((initialState[-2] + initialState[-1]) - 1)
        #count afterwards
        else:
            totalRabbits=((initialState[-2] + initialState[-1]) - (initialState[-(m+1)])) 
        initialState.append(totalRabbits)
        months += 1
    return (initialState[-1])




if __name__ == '__main__':

    n, m = 83,20
    initialState = [1, 1] 
    number=fibonacciRabits(n,m,initialState)
    print(number)