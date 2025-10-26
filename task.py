# Визначення класу Teacher
class Teacher:

    def __init__(self, first_name, last_name, age, email, can_teach_subjects=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.assigned_subjects = []
        self.can_teach_subjects = can_teach_subjects if can_teach_subjects else []


def create_schedule(subjects, teachers):
    # Зберігатиме обрані підмножини
    chosen_teachers = []
    # Непокриті елементи з subjects
    uncovered_subjects = subjects.copy()

    # Поки є непокриті елементи
    while uncovered_subjects:
        # Знайдемо підмножину, яка покриває найбільшу кількість непокритих елементів
        best_teacher = max(
            teachers,
            key=lambda teacher: (len(teacher.can_teach_subjects & uncovered_subjects)),
        )
        # Предмети, які цей викладач може покрити зараз
        covered_now = best_teacher.can_teach_subjects & uncovered_subjects

        # Додаємо викладача до обраних
        best_teacher.assigned_subjects = covered_now
        chosen_teachers.append(best_teacher)

        # Видаляємо покриті предмети
        uncovered_subjects -= covered_now

    return chosen_teachers


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher(
            "Марія",
            "Петренко",
            38,
            "m.petrenko@example.com",
            {"Хімія"},
        ),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія",
            "Шевченко",
            29,
            "n.shevchenko@example.com",
            {"Біологія", "Хімія"},
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher(
            "Олена",
            "Гриценко",
            42,
            "o.grytsenko@example.com",
            {"Біологія"},
        ),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"Викладає предмети: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
