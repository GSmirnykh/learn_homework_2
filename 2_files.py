"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as file_input:
        content = file_input.read()
        print(len(content))
        print(len(content.split()))
        replace_symbals = content.replace('.', '!')
        print(replace_symbals)
    
    with open('referat2.txt', 'w', encoding='utf-8') as file_output:
        file_output.write(replace_symbals)


if __name__ == "__main__":
    main()
