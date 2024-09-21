# SRART
print("ortal's olympics")
cnt: int = 0
sum: int = 0
highest_score: int = 0
y = False
new_world_rec = 0
name = ""
for i in range(7):
    res = float(input("enter your result:"))
    if res > 5.80:
        sum += res
        cnt += 1
    if res > 6.23:
        name = input("you have set a new world record! \nenter your name:")
        new_world_rec = res
        y = True
    if res > highest_score:
        highest_score = res

all_res_avg = sum / cnt
print("the avrege of the olympics:", all_res_avg, "m")
print("the highest score of the olympics is:", highest_score, "m")
if y:
    print("the new world record in ortal's olympics is:", new_world_rec, "m", "by:", name)
else:
    print(None)
# END
