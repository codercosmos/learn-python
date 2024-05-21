import random 
from matplotlib import pyplot as plt
 
days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

week_temp = []

for i in range(7):
    num=random.randint(30,50)
    F=(9/5)*num+32
    print(F)
    week_temp.append(F)
    

plt.plot(days, week_temp)

plt.xlabel('Week Days')

plt.ylabel('Temperature (°F)')

plt.title('Weekly Temperature Trends')

plt.show()



print(week_temp)

