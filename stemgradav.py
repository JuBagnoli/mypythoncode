biology_score = float(input("please input your biology score here "))
chemistry_score = float(input("please input your chemistry score here "))
physics_score = float(input("please input your physics score here "))
total_score = biology_score + chemistry_score + physics_score
print("my total is ", total_score)
average_score = total_score/3
print("my average is ",average_score)
if average_score < 40: 
    print("fail")