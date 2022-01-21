def main():
    # 🚨 Don't change the code below 👇
    student_heights = input("Input a list of student heights ").split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    # 🚨 Don't change the code above 👆


    #Write your code below this row 👇
    #Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

    sum_height = 0
    student_count = 0

    for height in student_heights:
        sum_height += height
        student_count += 1

    height_average = round(sum_height/student_count)

    print(height_average)



if __name__ == '__main__':
    main()