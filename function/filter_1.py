from functools import reduce
def check_function(num):
    if (num>=70 and num<=100):
        return True
    return False
def map_check(num):
    return num+10
def addition(num1,num2):
    return num1+num2


def main():
    num=[23,3456,76,97,78,90]
    filter_result=tuple(filter(check_function,num))
    print('FilterResult',filter_result)
    map_result=list(map(map_check,filter_result))
    print('MapResult',map_result)
    reduce_result=reduce(addition,map_result)
    print('ReduceResult',reduce_result)
if __name__=="__main__":
    main()