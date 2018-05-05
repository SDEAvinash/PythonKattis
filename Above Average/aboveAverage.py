import sys

START = 1


def write_above_average(grade_average, sample_set):
    above_average = [int(x) for x in sample_set if int(x) > grade_average and x is not sample_set[0]]
    return percentage(len(above_average), int(sample_set[0]))


def percentage(result, total):
    return round((result / total) * 100, 3)


def calculate_above_average(sample_set, average=0):
    number_of_people = int(sample_set[0])
    for final_grade in range(START, int(number_of_people) + START):
        average += int(sample_set[final_grade])
    grade_average = round((average / number_of_people), 3)
    return write_above_average(grade_average, sample_set)


def read_sample_data():
    output_percentage = []
    f = sys.stdin
    for lines in range(START, int(f.readline()) + START):
        one_set = f.readlines(lines)[0]
        output_percentage.append(str(calculate_above_average(one_set.split())) + "%")
    sys.stdout = open("1.ans", "w", encoding='utf-8')
    print('\n'.join(x for x in output_percentage))


read_sample_data()