# # # from numpy import*
# # # # a=[3,2,6,5,8,9,6]
# # # # b=array(a)
# # # # print(b)
# # # a = array([range(i,i+5) for i in [2, 4, 6]])
# # # print(a)

# # # from gettext import npgettext
# # # from numpy import *
# # # # a = random.randint(0, 10, (3, 3))
# # # # b=any(a>2)

# # # # # # a=eye(3)
# # # # # print(a)
# # # # # print(b)
# # # # a =arange(9).reshape(3,3)
# # # # b =arange(9).reshape(3,3)
# # # # c = 2*b
# # # # d = isclose(a,b,rtol = 0.1)
# # # # e = isclose(a,c,rtol = 0.1)
# # # # print(a)
# # # # # print('-------------------------')
# # # # # print(b)
# # # # # print('-------------------------')
# # # # # print(c)
# # # # # print('-------------------------')
# # # # # print(d)
# # # # # print('-------------------------')
# # # # # print(e)
# # # # a =arange(4).reshape(2,2)
# # # # b =2*arange(4).reshape(2,2)
# # # # c = vstack((a,b))
# # # # print(a)
# # # # print('-------------------------')
# # # # print(b)
# # # # print('-------------------------')
# # # # print(c)
# # # # a =arange(4).reshape(2,2)
# # # # b =2*arange(4).reshape(2,2)
# # # # c = hstack((a,b))
# # # # print(a)
# # # # print('-------------------------')
# # # # print(b)
# # # # print('-------------------------')
# # # # print(c)
# # # # a=random.randint(1,20,size=16).reshape(4,4)
# # # # b=linalg.inv(a)
# # # # # c=dot(a,b)
# # # # # print(a)
# # # # # print(b)
# # # # # print(c)
# # # # a=loadtxt('"E:\Documents\ASU\COURSES\ML & DL\python\EX codes\mtrs.text"')
# # # # print(a)
# # # from numpy import *
# # # # Polynomial = polynomial.Polynomial
# # # # X= np.array([0,20,40,60,80,100,120,140,160,180])
# # # # Y= np.array([10,9,8,7,6,5,4,3,2,1])
# # # # points,stats = Polynomial.fit(X,Y,1,full=True)
# # # # print(points)
# # # a = poly1d((-7))
# # # b = poly1d((-7,2))
# # # c = poly1d((-7,2,1))
# # # d = poly1d((-7,2,1,3))
# # # e = poly1d((-7,2,1,3,6))
# # # print(a)
# # # print('-------------------------')
# # # print(b)
# # # print('-------------------------')
# # # print(c)
# # # print('-------------------------')
# # # print(e)

# # from numpy import*
# # a=poly1d((5,6,3,2))
# # b=a(2)
# # print(a)
# # c=polyder(a)
# # d=polyint(a)

# # print(b)
# # print(c)
# # print(d)


# # from numpy import*
# # # x=datetime64('2015-07-3',dtype=datetime64)
# # # print(x)
# # print(datetime64)
# rom numpy import *
# x = datetime64('2015-07-04')
# print(x)
# print('-------------------------')


from pandas import *
d=Series([2,6,5,65])
d.plot(kind='pie')
