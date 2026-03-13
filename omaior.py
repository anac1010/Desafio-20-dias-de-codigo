a,b,c = map(int, input().split())
maiorab = (a+b+abs(a-b))//2
maiorfinal = (maiorab+c+abs(maiorab-c))//2

print(f"{maiorfinal} eh o maior")