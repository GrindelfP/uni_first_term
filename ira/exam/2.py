def partial_sum(num):
    the_sum = 0
    for i in range(0, num):
        yi = 3*i
        the_sum += yi
    return the_sum
# в данном случае вычисляется сумма ряда: y1 + y2 + y3 + ... + yn, где yi = 3*i (то есть последовательность имеет
# вид: 3 + 6 + 9 + 12 + 15 + ... + 3 * n
