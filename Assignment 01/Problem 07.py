user_input = int(input())

if user_input % 2 == 0 and user_input % 5 == 0:
    print("multiple of 2 and 5 both")
elif user_input % 2 == 0 or user_input % 5 == 0:
    print(user_input)
else:
    print("Not a multiple")
