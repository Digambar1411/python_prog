
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in grades:
        if i<38:
            print(i)
            # return i
        elif (((i//5)+1)*5-i < 3):
            print(((i//5)+1)*5)
            # return ((i//5)+1)*5
        else:
            print(i)
            # return i

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    