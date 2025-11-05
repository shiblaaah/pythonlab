low = int (input (" Enter lower range : "))
high = int (input (" Enter Upper range : "))
for n in range ( low , high + 1):
    if int  (n ** 0.5) ** 2 == n :
        if all (int (d) % 2 == 0 for d in str (n)):
            print(n)
                                           
