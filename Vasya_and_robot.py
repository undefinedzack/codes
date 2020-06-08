number_of_operations = int(input())
sequence_of_operations = str(input())
final = list(map(int, input().split(" ")))


def R(initial):
    initial[0] += 1
    return initial
def L(initial):
    initial[0] -= 1
    return initial
def U(initial):
    initial[1] += 1
    return initial
def D(initial):
    initial[1] -= 1
    return initial

initial = [0,0]
noR,noL,noU,noD = 0,0,0,0
ioR,ioL,ioU,ioD = [],[],[],[]
for i in range(number_of_operations):
    if sequence_of_operations[i] == 'R':
        R(initial)
        noR+=1
        ioR.append(i)
    if sequence_of_operations[i] == 'L':
        L(initial)
        noL+=1
        ioL.append(i)
    if sequence_of_operations[i] == 'U':
        U(initial)
        noU+=1
        ioU.append(i)
    if sequence_of_operations[i] == 'D':
        D(initial)
        noD+=1
        ioD.append(i)

number_of_L_to_be_changed,number_of_R_to_be_changed,number_of_U_to_be_changed,number_of_D_to_be_changed=0,0,0,0
flag = 0
if initial == final:
    flag == 1
    print(0)
else:
    if final[0] > initial[0]:
        diff = final[0] - initial[0]
        if diff % 2 != 0 and flag == 0:
            print(-1)
        else:
            number_of_L_to_be_changed = int(diff / 2)
            if number_of_L_to_be_changed > noL and flag == 0:
                print(-1)
                flag = 1

    elif final[0] == initial[0]:
        pass
    else:
        diff = initial[0] - final[0]
        if diff % 2 != 0 and flag == 0:
            print(-1)
        else:
            number_of_R_to_be_changed = int(diff / 2)
            if number_of_R_to_be_changed > noR and flag == 0:
                print(-1)
                flag = 1


    if final[1] > initial[1]:
        diff = final[1] - initial[1]
        if diff % 2 != 0 and flag == 0:
            print(-1)
        else:
            number_of_D_to_be_changed = int(diff / 2)
            if number_of_D_to_be_changed > noD and flag == 0:
                print(-1)
                flag = 1

    elif final[1] == initial[1]:
        pass
    else:
        diff = initial[1] - final[1]
        if diff % 2 != 0 and flag == 0:
            print(-1)
        else:
            number_of_U_to_be_changed = int(diff / 2)
            if number_of_U_to_be_changed > noU and flag == 0:
                print(-1)
                flag = 1


    #final
    max = 0
    min = 9999999
    if number_of_L_to_be_changed != 0 and flag == 0 :
        if ioL[len(ioL)-1] > max:
            max = ioL[len(ioL)-1]
        if (ioL[len(ioL)-1] - number_of_L_to_be_changed) < min:
            min = (ioL[len(ioL)-1] - number_of_L_to_be_changed)

    if number_of_R_to_be_changed != 0 and flag == 0:
        if ioR[len(ioR)-1] > max:
            max = ioR[len(ioR)-1]
        if (ioR[len(ioR)-1] - number_of_R_to_be_changed) < min:
            min = (ioR[len(ioR)-1] - number_of_R_to_be_changed)

    if number_of_U_to_be_changed != 0 and flag == 0 :
        if ioU[len(ioU)-1] > max:
            max = ioU[len(ioU)-1]
        if (ioU[len(ioU)-1] - number_of_U_to_be_changed) < min:
            min = (ioU[len(ioU)-1] - number_of_U_to_be_changed)

    if number_of_D_to_be_changed != 0 and flag == 0:
        if ioD[len(ioD)-1] > max:
            max = ioD[len(ioD)-1]
        if (ioD[len(ioD)-1] - number_of_D_to_be_changed) < min:
            min = (ioD[len(ioD)-1] - number_of_D_to_be_changed)

    if flag == 0:
        print(max-min+1)