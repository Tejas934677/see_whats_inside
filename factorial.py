def factorial(n):
    if n == 0 :
        return 1
   
    result = 1
    for i in range(1 , n+1) : 
        result *= i 
    
    return result 
def binomial_coefficient(N,R):
    
    return factorial(N)//(factorial(R)*(factorial(N-R)))
N = int(input("1st coefficient >>"))
R = int(input("2nd cofficient>>"))
print(binomial_coefficient(N,R))