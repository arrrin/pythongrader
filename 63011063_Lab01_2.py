user_input_h, user_input_w = input("Enter your High and Weight : ").split()

BMI = float(user_input_w) / (float(user_input_h)**2)


if BMI >= 30:
    print("Fat")
elif 25 <= BMI < 30:
    print("Getting Fat")
elif 23 <= BMI < 25:
    print("More than Normal Weight")
elif 18.50 <= BMI < 23:
    print("Normal Weight")
else:
    print("Less Weight")
