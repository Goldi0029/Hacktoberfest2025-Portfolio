total_jumping_jacks = 100
set_size = 10
completed = 0

print("\nStarting workout: 100 Jumping Jacks (10 per set)\n")

for i in range(1, (total_jumping_jacks // set_size) + 1):
    completed += set_size
    print(f"Set {i} done! Total completed: {completed}")

    if completed >= total_jumping_jacks:
        print(" Congratulations! You completed the workout!")
        break

    tired = input("Are you tired? (yes/no): ").strip().lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            print(f"{total_jumping_jacks - completed} jumping jacks remaining.\n")
    else:
        print(f"{total_jumping_jacks - completed} jumping jacks remaining.\n")
