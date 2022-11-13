#1
numbers = []
def input_list():
    x=input()
    if x!='':
       y=float(x)
       numbers.append(y)
       input_list()
    else:
        tot=0
        for number in numbers:
            tot=tot+number
            print(number,tot)
input_list()

#2
def check_monotonic_sequence(sequence):
    seq=[]
    for i in sequence:
        seq.append(int(i))
    x=0
    count1=0
    count2=0
    count3=0
    for s in range(len(seq)-1):
        if seq[x+1]> seq[x]:
            count1+=1
        elif seq[x+1]==seq[x]:
            count2+=1
        else :
            count3+=1

        x=x+1
    if count1==len(seq)-1 :
        print(True,True,False,False)
    elif (count1<len(seq)-1) and count2!=0 and  count3==0 :
        print(True,False,False,False)
    elif count3==len(seq)-1 :
        print(False,False,True,True)
    elif (count3 < len(seq) - 1) and count2 != 0 and count1 == 0:
        print(False,False,True,False)
    else:
        print(False,False,False,False)

check_monotonic_sequence ( [1, 0, -1, 1])


#3

def primes_generator(n):
    q=[]
    p=[]
    s=[]
    r = range(2, 100)

    while len(s)<=n :
        for i in range(3,100):
           if len(p)<=100:
                for j in range (2,i):
                    if i%j==0:
                       q.append(i)
                [p.append(x) for x in q if x not in p]

        [s.append(y) for y in r if y not in p ]

    print(s[0:n+1])

primes_generator(9)

#4

def is_empty_vecotr(vec_lst):
     for v in vec_list :
         if len(v)==0:
             return True
         else:
             return False

#5

def orthogonal(vec_1, vec_2):
    vec_3 = [0, 0, 0, 0]
    for x in range(len(vec_1)):
        vec_3[x]=vec_1[x]*vec_2[x]
    print(vec_3)
    if vec_3==[0,0,0,0]:
       print("orthogonal")
    else:
       print("not orthogonal")


calc_the_inner_product([1,2,3,9],[1,1,-1,0])




