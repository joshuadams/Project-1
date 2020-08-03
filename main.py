for i in range(4):
  print('Hello Cool World!')   
  
x = 14
if x == 15:
  print(x) 
elif x ==14:
  print(x)
else:
  print("It's not 15")



book = {
    'homogenous':'of the same kind',
    'escapade' : 'exciting adventure',
    'military' : 'serves our country'
  }
print(book.get('homogenous'))
print(book.get('escapade'))