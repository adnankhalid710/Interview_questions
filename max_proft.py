# This problem was asked by Facebook.
'''
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling
that stock once. You must buy before you can sell it.
For example,
given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''
def calculate_max_profit(arr1):
    arr2 = []
    num1 = min(arr1)  #Finding the minimum price in the array
    num2 = 0
    index_num = 0
    l = len(arr1)

    for i in range(l-1):     # Finding the index of the minimum price
        if num1 == arr1[i]:
            index_num = i
            bb = index_num
            #num2 = arr1[bb]
            arr2 = arr1[bb:]
            num2 = max(arr2)
            #print(num2)
            prof = num2-num1
    return num1, num2, prof

a = [9, 1, 18, 5, 7, 10]
qq, ww, ee = calculate_max_profit(a)
print("Buying price is {} $ and selling price is {} $, net profit is {} $".format(qq, ww, ee))
