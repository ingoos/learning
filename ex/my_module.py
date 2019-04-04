def sum(*args):
    result = 0
    for i in args:
        result = result + i
    return result
    
if __name__ == "__main__":
    print(sum(1,2,3))
    