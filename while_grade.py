Done = True
count = 0
while Done:
    score = input(f'Enter score value #{count+1} : ')

    if score != "-1":
        Mark = float(score)

        if Mark >= 0 and Mark <=100:
            Grade = ""
            count += 1

            if Mark >= 80:
                Grade = "A"
            elif Mark >= 70:
                Grade = "B"
            elif Mark >= 60:
                Grade = "C"
            elif Mark >= 50:
                Grade = "D"
            else:
                Grade = "F"
            
            print(f"Score is {Mark}, get {Grade}")

        else:

            print("Score out of range, input again.")
    elif score == "-1":
        # Done = False
        break

print("Exit Program...")
