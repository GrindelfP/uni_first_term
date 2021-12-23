from random import randint
from time import time
from research.a_bubble import bubble_sort, bubble_sort_2, bubble_sort_3
from research.b_sorting_cocktail import cocktail_sort
from research.c_hole_insertion_sorting import hole_insertion_sort
from research.d_chosen_sorting import select_sorting
from research.e_shell_sorting import shell_sorting
from research.f_QSORT import q_sort


N = 10
M = 10

time_initial = time()

time_0_l = []
time_1_l = []
time_2_l = []
time_3_l = []
time_4_l = []
time_5_l = []
time_6_l = []
time_7_l = []

result_1 = ()
result_2 = ()
result_3 = ()
result_4 = ()
result_5 = ()
result_6 = ()
result_7 = ()
result_8 = ()

times = 1
while times > 0:
    the_list_1 = []
    for i in range(N):
        the_list_1.append(randint(1, M))
    the_list_2 = []
    for i in range(N):
        the_list_2.append(randint(1, M))
    the_list_3 = []
    for i in range(N):
        the_list_3.append(randint(1, M))
    the_list_4 = []
    for i in range(N):
        the_list_4.append(randint(1, M))
    the_list_5 = []
    for i in range(N):
        the_list_5.append(randint(1, M))
    the_list_6 = []
    for i in range(N):
        the_list_6.append(randint(1, M))
    the_list_7 = []
    for i in range(N):
        the_list_7.append(randint(1, M))
    the_list_8 = []
    for i in range(N):
        the_list_8.append(randint(1, M))

    time_0 = time()
    result_1 = bubble_sort(the_list_1)
    time_0_l.append((time() - time_0) * 10000)
    time_1 = time()
    result_2 = bubble_sort_2(the_list_2)
    time_1_l.append((time() - time_1) * 10000)
    time_2 = time()
    result_3 = bubble_sort_3(the_list_3)
    time_2_l.append((time() - time_2) * 10000)
    time_3 = time()
    result_4 = cocktail_sort(the_list_4)
    time_3_l.append((time() - time_3) * 10000)
    time_4 = time()
    result_5 = hole_insertion_sort(the_list_5)
    time_4_l.append((time() - time_4) * 10000)
    time_5 = time()
    result_6 = select_sorting(the_list_6)
    time_5_l.append((time() - time_5) * 10000)
    time_6 = time()
    result_7 = shell_sorting(the_list_7)
    time_6_l.append((time() - time_6) * 10000)
    time_7 = time()
    result_8 = q_sort(the_list_8, 0, len(the_list_8) - 1)
    time_7_l.append((time() - time_7) * 10000)
    times -= 1

time_total = (time() - time_initial)

print("Bubble time: ", sum(time_0_l)/len(time_0_l))
print("Bubble+ time: ", sum(time_1_l)/len(time_1_l))
print("Bubble++ time: ", sum(time_2_l)/len(time_2_l))
print("Cocktail time: ", sum(time_3_l)/len(time_3_l))
print("Insert time: ", sum(time_4_l)/len(time_4_l))
print("CHOSEN time: ", sum(time_5_l)/len(time_5_l))
print("Shell time: ", sum(time_6_l)/len(time_6_l))
print("QSort time: ", sum(time_7_l)/len(time_7_l))
print("Done in", time_total, "seconds.")

comparisons = open("comparisons.txt", "w+")
comparisons.write(str(result_1[1]) + "\n")
comparisons.write(str(result_2[1]) + "\n")
comparisons.write(str(result_3[1]) + "\n")
comparisons.write(str(result_4[1]) + "\n")
comparisons.write(str(result_5[1]) + "\n")
comparisons.write(str(result_6[1]) + "\n")
comparisons.write(str(result_7[1]) + "\n")
comparisons.write(str(result_8[1]) + "\n")
comparisons.close()

movements = open("movements.txt", "w+")
movements.write(str(result_1[2]) + "\n")
movements.write(str(result_2[2]) + "\n")
movements.write(str(result_3[2]) + "\n")
movements.write(str(result_4[2]) + "\n")
movements.write(str(result_5[2]) + "\n")
movements.write(str(result_6[2]) + "\n")
movements.write(str(result_7[2]) + "\n")
movements.write(str(result_8[2]) + "\n")
movements.close()

functional_time = open("functional_time.txt", "w+")
functional_time.write(str(sum(time_0_l)/len(time_0_l)) + "\n")
functional_time.write(str(sum(time_1_l)/len(time_1_l)) + "\n")
functional_time.write(str(sum(time_2_l)/len(time_2_l)) + "\n")
functional_time.write(str(sum(time_3_l)/len(time_3_l)) + "\n")
functional_time.write(str(sum(time_4_l)/len(time_4_l)) + "\n")
functional_time.write(str(sum(time_5_l)/len(time_5_l)) + "\n")
functional_time.write(str(sum(time_6_l)/len(time_6_l)) + "\n")
functional_time.write(str(sum(time_7_l)/len(time_7_l)) + "\n")
functional_time.close()
