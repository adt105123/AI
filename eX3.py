
# coding: utf-8

# In[3]:


BMI = 0
height = int (input("請輸入身高 (cm):"))
weight = int (input("請輸入體重 (kg):"))

BMI = (weight) / ((height/100)*(height/100))
print ("BMI = %f\n" % (BMI))

if BMI < 18.5:
    print("你過瘦了!")
if BMI >=18.5 and BMI <24:
    print("體重標準!")
if BMI >= 24:
    print("體重過重!")

