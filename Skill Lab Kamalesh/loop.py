total = 0
for i in range(1, 11):
    total+= i

print("Sum =", total)


#while loop
num = 0
while num < 11:
    print(num, end=" ")
    num+=1

    

# For loop: print and count student scores
scores = [85, 92, 78, 96, 88]
total = 0

for score in scores:
    print("Score:", score)
    total += score

average = total / len(scores)
print("Average:", average)

# While loop: repeatedly ask for a valid score
score = -1

while score < 0 or score > 100:
    score = int(input("Enter a score from 0 to 100: "))
    if score < 0 or score > 100:
        print("Invalid score. Try again.")

print("Valid score:", score)