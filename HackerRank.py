if __name__ == '__main__':
    n = int(input())

num = []
for i in range(1,n+1):
    num.append(i)
print("".join([str(j) for j in num]))