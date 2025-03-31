students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
temp=students.copy()
def top():
    return f'Top Performer:"{max(temp.items(),key=lambda x:x[1])[0]}"'
def avg():
    for i,j in temp.items():
        temp[i]= sum(j)/len(j)
    return f"Average Marks: {temp}"

print(avg())
print(top())
