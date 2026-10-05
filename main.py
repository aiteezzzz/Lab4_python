import re


def open_file(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
        print(f"Файл {file_name} успішно відкрито.")
        return file
    except Exception as e:
        print(f"Помилка відкриття файлу {file_name}: {e}")
        return None


def create_file(file_name):
    file = open_file(file_name, "w")

    if file is not None:
        file.write(
            "Ананас дуже смачний фрукт.\n"
            "Програмування на Python допомагає автоматизувати завдання.\n"
            "Математика, алгебра та геометрія вивчаються у школі.\n"
            "Автомобіль, аеродром, характеристика, авіаконструктор.\n"
        )

        file.close()
        print(f"Дані записано у файл {file_name}.")


def process_file(input_file, output_file):
    file_in = open_file(input_file, "r")

    if file_in is None:
        return

    text = file_in.read()
    file_in.close()

    words = re.findall(r"[А-Яа-яІіЇїЄєA-Za-z]+", text)

    words_with_a = []

    for word in words:
        if "а" in word.lower():
            words_with_a.append(word)

    file_out = open_file(output_file, "w")

    if file_out is None:
        return

    if len(words_with_a) > 0:

        max_length = max(len(word) for word in words_with_a)

        longest_words = []

        for word in words_with_a:
            if len(word) == max_length and word not in longest_words:
                longest_words.append(word)

        for word in longest_words:
            file_out.write(word + "\n")

    else:
        file_out.write("Слів, що містять символ 'а', не знайдено.")

    file_out.close()
    print(f"Результат записано у файл {output_file}.")


def print_file(file_name):
    file = open_file(file_name, "r")

    if file is not None:
        print("\nВміст файлу TF22_2:")

        for line in file:
            print(line.strip())

        file.close()

file1_name = "TF22_1.txt"
file2_name = "TF22_2.txt"

create_file(file1_name)
process_file(file1_name, file2_name)
print_file(file2_name)
