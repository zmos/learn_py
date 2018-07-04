import sys

if __name__=='__main__':
    try:
        wage=int(sys.argv[1])
    except ValueError:
        print("Parameter error")
    wage=wage-3500
    if wage <= 0:
        result=0.00
    elif wage <= 1500 :
        result = wage*0.03
    elif wage <= 4500 :
        result = wage*0.10-105
    elif wage <= 9000 :
        result = wage*0.20-555
    elif wage <= 35000 :
        result = wage*0.25-1005
    elif wage <= 55000 :
        result = wage*0.30-2755
    elif wage <= 80000 :
        result = wage*0.35-5505
    else: 
        result = wage*0.45-13505
    print(format(result,".2f"))
