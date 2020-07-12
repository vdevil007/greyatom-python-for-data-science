# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
#Code starts here
census = np.concatenate((new_record,data),axis=0)
print(census)
age = np.array(census[0:,0])
print(age)
max_age = np.max(age)
min_age = np.min(age)
age_mean = age.mean()
age_std = np.std(age)
print(max_age,min_age,age_mean,age_std, sep='\n')
race = np.array(census[0:,2])

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

print(len_0,len_1,len_2,len_3,len_4)

minority_race = min(len_0,len_1,len_2,len_3,len_4)
print(minority_race)

senior_citizens =census[census[:,0]>60]
#working_hours_sum = 0

working_hours = np.array(senior_citizens[0:,6])
working_hours_sum= np.sum(working_hours)
#for i in range(0,len(senior_citizens)):
 #   working_hours_sum = working_hours_sum + senior_citizens[i][6]

print(working_hours_sum)
print(len(senior_citizens))

avg_working_hours = np.mean(working_hours)
print(avg_working_hours)

high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high = np.mean(np.array(high[0:,7]))
avg_pay_low = np.mean(np.array(low[0:,7]))

if(avg_pay_high>avg_pay_low):
    print("yaa good edu mean good pay")
else:
    print("no good edu don mean good pay")





