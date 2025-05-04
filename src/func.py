


def func(list_d):
    return sorted(list_d,
                key=lambda x: (
                x.salary_from if x.salary_from is not None else 0 + x.salary_to if x.salary_to is not None else 0) / 2,
                reverse=True)