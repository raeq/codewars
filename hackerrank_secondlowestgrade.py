if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    vals = student_marks[query_name]
    avg = sum(vals) / len(vals)

    print(f"{avg:.2f}")
