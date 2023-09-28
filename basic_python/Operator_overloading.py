# Nạp chồng toán tử cho 2 vector
# 1.2 2.3 4.5 3.5 4.6
# 2.1 2.2 2.3 2.5 3.6
class Vector:
  def __init__(self, point):
    self.point=point
  
  def __add__(self, other):
    if(len(self.point)!=len(other.point)):
      print("Size Error!")
    else:
      tong=[]
      for i in range(len(self.point)):
        tong.append(self.point[i]+other.point[i])
      return tong
  
  def __sub__(self, other):
    if(len(self.point)!=len(other.point)):
      print("Size Error!")
    else:
      hieu=[]
      for i in range(len(self.point)):
        hieu.append(self.point[i]-other.point[i])
      return hieu
    
  def __mul__(self, other):
    if(len(self.point)!=len(other.point)):
      print("Size Error!")
    else:
      tich=0
      for i in range(len(self.point)):
        tich+=self.point[i]*other.point[i]
      return tich
    
  def __eq__(self, other):
    if(len(self.point)!=len(other.point)):
      print("Size Error!")
    else:
      for i in range(len(self.point)):
        if(self.point[i]!=other.point[i]):
          return False
      return True

a=input().split()
b=input().split()
x=list(map(lambda i: float(i), a))
y=list(map(lambda i: float(i), b))

vector1=Vector(x)
vector2=Vector(y)

print(vector1+vector2)
print(vector1-vector2)
print(vector1*vector2)
print(vector1==vector2)
