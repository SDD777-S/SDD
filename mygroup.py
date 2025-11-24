groupmates = [
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Анна",
        "surname": "Васильева",
        "exams": ["Математика", "Физика", "Химия"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Мария",
        "surname": "Соколова",
        "exams": ["Биология", "География", "Литература"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Дмитрий",
        "surname": "Морозов",
        "exams": ["Английский", "Экономика", "Право"],
        "marks": [3, 4, 5]
    },
]

def print_students(students):
    """Выводит список студентов в виде таблицы."""
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(10),
            str(student["exams"]).ljust(30),
            str(student["marks"]).ljust(20)
        )


def filter_by_average_mark(students, threshold):
    filtered = []
    for student in students:
        # Вычисляем средний балл
        avg_mark = sum(student["marks"]) / len(student["marks"])
        # Если средний балл выше или равен порогу — добавляем в результат
        if avg_mark > threshold:
            filtered.append(student)
    return filtered

# Основной код программы
if __name__ == "__main__":
    # Спрашиваем у пользователя порог среднего балла
    try:
        threshold = float(input("Введите минимальный средний балл для фильтрации: "))
    except ValueError:
        print("Ошибка: введите число (например, 4.0 или 3.5)!")
    else:
        # Фильтруем студентов
        filtered_students = filter_by_average_mark(groupmates, threshold)
        
        # Выводим результат
        if filtered_students:
            print(f"\nСтуденты со средним баллом > {threshold}:")
            print_students(filtered_students)
        else:
            print(f"Нет студентов со средним баллом > {threshold}.")
