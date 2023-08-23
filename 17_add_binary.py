def add_binary(b_1,b2):
    rev_b_1 = binary_1[::-1]   
    rev_b_2 = binary_2[::-1]
    if len(rev_b_1) < len(rev_b_2):
        rev_b_1 += "0"*(len(rev_b_2)-len(rev_b_1))
    else:
        rev_b_2 += "0"*(len(rev_b_1)-len(rev_b_2))

    add_  = ""
    carry = 0
    for i in range(len(rev_b_1)):
        temp_= int(rev_b_2[i])+int(rev_b_1[i])+carry
        # print(int(rev_b_2[i]),int(rev_b_1[i]),carry, end=" ")
        if temp_ <= 1:
            carry = 0
        elif temp_ == 2:
            carry = 1
            temp_ = 0
        else:
            carry = 1
            temp_ = 1

        add_ += str(temp_)
        # print(add_)

    if carry != 0:
        add_ += str(carry)

    return add_[::-1]

binary_1 =    "1010" #=> 26
binary_2 = "1011" #=> 162
# out_put  = "10111100" #=> 188
print(add_binary(binary_1,binary_2))
