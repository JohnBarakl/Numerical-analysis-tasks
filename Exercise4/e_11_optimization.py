from Exercise4.b_multiplication_method import power_method
from Exercise4.b_multiplication_method import construct_G
from Exercise4.b_multiplication_method import integer_vector_multiplication

if __name__ == '__main__':

    A_modified = [
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
    ]


    q = 0.15
    n = len(A_modified)

    G = construct_G(A_modified, q, n)

    print("\n\nSums of new Google matrix's columns: ")
    element_sum = 0
    for i in range(len(G)):
        element_sum = 0
        for j in range(len(G)):
            element_sum += G[j][i]
        print(element_sum, end="\t")
    print("\n")


    p = power_method(G, 7)

    element_sum = 0
    for i in p:
        element_sum += i
    p = integer_vector_multiplication(1 / element_sum, p)

    print("\nNew probability matrix p: ")
    element_sum = 0
    for count, i in enumerate(p):
        print("p[{:02d}]:".format(count + 1), round(i, 7))
        element_sum += i

    print("\nWith sum =", element_sum)

