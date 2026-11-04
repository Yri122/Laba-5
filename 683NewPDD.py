import sys
import abc
def main():
    y,x = map(int,input().split())
    g,f = map(int,input().split())
    if y == g and f == x:
        print(0)
        return
    elif abs(x - f) + abs(y - g) == 1:
        print(1)
        return
    elif abs(x - f) == 0 or abs(y - g) == 0:
        count = (abs(x - f) + abs(y - g))
        result = (count + (count - 1) * 2) -1
    else:
        count = (abs(x - f) + abs(y - g))
        result = count + ((count - 2) * 2) - 1
    print(result)

if __name__ == '__main__':
    main()