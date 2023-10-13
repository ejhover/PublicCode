# 10 minutes
def total_time(fname, employee):
    hours={}
    try:
        with open(fname) as hourlist:
            for i in hourlist.read().split("\n"):
                try:
                    hours[i.split()[0]]=hours[i.split()[0]]+float(i.split()[1])
                except:
                    hours[i.split()[0]]=float(i.split()[1])
        return hours[employee] if employee in hours.keys() else 0
    except:
        return -1
#20 min
def most_populous(year, region):
    ans=[]
    with open('cities.csv') as cities:
        for i in [i.strip().split(",") for i in cities.readlines()]:
            if year==i[0] and region==i[4]:
                ans.append(i[1])
    return ans
#  min
def stasis(jump_year, jump_city):
    ans=0
    with open('fixed_cities.csv', 'w') as newfile:
        with open('cities.csv', 'r') as cities:
            cities.readline()
            for i in [i.split(",") for i in cities.read().split("\n")[:-1]]:
                if int(i[0])>=int(jump_year) and i[1]==jump_city:
                    i[3]=str(int(i[3])+3)
                    newfile.write(",".join(i))
                    newfile.write("\n")
                    ans+=1
                else:
                    newfile.write(",".join(i))
                    newfile.write("\n")
    return ans


print(most_populous('1500', 'East Asia'))