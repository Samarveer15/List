L = [4,3,4,6,7,46,64,99,56]
print("Oringinal list :",L)


count = 0



for i in L:
    count += i



avg = count/len(L)



print("sum + ",count)
print("average = ", avg)



L.sort()




print("Samallest elemant is:",L[0])



print("Largest element is:",L[-1])