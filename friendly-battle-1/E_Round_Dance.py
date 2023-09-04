for _ in range(int(input())):
  n=int(input())
  a=list(map(int,input().split()))
  s=set()
  for i in range(n):
    x,y=sorted([i,a[i]-1])
    s.add((x,y))
  p=[-1]*n
  def find(x):
    if p[x]<0:return x
    p[x]=find(p[x])
    return p[x]
  closed=0
  for a,b in s:
    a=find(a)
    b=find(b)
    if a==b:
        closed+=1
    else:
      p[a]+=p[b]
      p[b]=a
  cmps=0
  for i in range(n):
    if find(i)==i:cmps+=1
  open=cmps-closed
  if open==0:
      print(closed,closed)
  else:
      print(closed+1,closed+open)