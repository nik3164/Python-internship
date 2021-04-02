import matplotlib.pyplot as plt

d = {}
eligible_male = {}
non_eligible_male = {}
eligible_female = {}
non_eligible_female = {}
year = 2021
Eligible_male = 0
Non_eligible_male = 0
Eligible_female = 0
Non_eligible_female = 0
f = open("Matrimony_info.csv", 'r')
data = f.read()
for line in data.split("\n"):
    (key, val) = line.split(",")
    d[int(key)] = str(val)
    # print(type(year), type(key))
    if val == 'M':
        if (year - int(key)) >= 21:
            eligible_male[int(key)] = str(val)
            Eligible_male = Eligible_male + 1
        else:
            non_eligible_male[int(key)] = str(val)
            Non_eligible_male = Non_eligible_male + 1
    elif val == 'F':
        if (year - int(key)) >= 18:
            eligible_female[int(key)] = str(val)
            Eligible_female = Eligible_female + 1
        else:
            non_eligible_female[int(key)] = str(val)
            Non_eligible_female = Non_eligible_female + 1
    else:
        print("No data Found...!")

plt.title("Matrimony Data")
plt.xlabel("Eligibility")
plt.ylabel("Count")
plt.bar("Eligible Male", Eligible_male)
plt.bar("Non Eligible Male", Non_eligible_male)
plt.bar("Eligible Female", Eligible_female)
plt.bar("Non Eligible female", Non_eligible_female)
plt.show()
