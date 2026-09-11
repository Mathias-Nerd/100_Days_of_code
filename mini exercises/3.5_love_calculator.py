#100 Days of code with python
#Author: Mathias Nerd
#LOve calculator

# RULES:
# 1. Combine both names -> lowercase
# 2. Count letters of TRUE (t,r,u,e) in combined names = first digit
# 3. Count letters of LOVE (l,o,v,e) in combined names = second digit
# 4. Final Score = int(str(TRUE_count) + str(LOVE_count))
# 5. <10 or >90 = coke and mentos, 
# 40-50 = alright together, 
# else = score
#Taking name input
name1 = input("Enter your name: ").lower()
name2 = input("Enter the name of your crush: ").lower()

#Combining names
combined_name = name1 + name2

t_count = combined_name.count("t")
r_count = combined_name.count("r")
u_count = combined_name.count("u")
e_count = combined_name.count("e")
l_count = combined_name.count("l")
o_count = combined_name.count("o")
v_count = combined_name.count("v")

num1 = t_count + r_count + u_count + e_count
num2 = l_count + o_count + v_count + e_count

answer = str(num1) + str(num2)

print(f"Your score is {answer}{", you go together like coke and mentos." if int(answer) < 10 or int(answer) > 90 else ", you are alright together." if int(answer) >= 40 or int(answer) <= 50 else "."}")