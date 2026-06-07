def student_dict(s):
         if s>=90 and s<=100:
                  print("A+")
         elif s>=80 and s<90:
                  print("A")
         else:
                  print("D")
d=eval(input("enter dictionary: "))
d1={}
for i in d:
         d1[i]=sum(d[i])/len(d[i])
for j in d1:
         print(j, end=" ")
         student_dict(d1[j])
         

