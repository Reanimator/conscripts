def get_inductees(names, birthday_years, genders):
    """
    Функция для отпределения военнообязанных
    :param names: список имен студентов
    :param birthday_years: список годов рождения
    :param genders: список полов студентов
    :return: кортеж листов, 0 - военнообязанные, 1 - неопределенные
    """
    conscripts = []
    uncertain = []
    for name, birthday_year, gender in zip(names, birthday_years, genders):
        if gender != "Female" and birthday_year is None or gender is None:
            uncertain.append(name)
        elif gender == "Male" and 2003 >= birthday_year >= 1991:
            conscripts.append(name)
    return conscripts, uncertain


if __name__ == "__main__":
    names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
    birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
    genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]
    print(get_inductees(names, birthday_years, genders))
