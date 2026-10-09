
def calculate_total(m1, m2, m3):
    return m1 + m2 + m3


def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


def check_result(mark):
    if mark >= 40:
        return "Pass"
    else:
        return "Fail"
