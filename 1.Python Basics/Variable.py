name = "Yasin" #string
age = 20 #int
cgpa = 5.00 #flaot
is_student = True #bool


print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

course = "Python's course for Shibloo"
print(course[0]) #-> p
print(course[-1]) #-> o
print(course[0:3]) #-> Pyt
print(course[1:4]) #-> yth
print(course[:5]) #-> Python
print(course[:]) #-> Python's course for Shibloo
another = course[:]
print(another) #-> Python's course for Shibloo