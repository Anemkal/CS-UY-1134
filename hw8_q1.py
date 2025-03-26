"""Author: Anemka Lydia Legbara')
print('Assignment: HW8 - Question 1')
print('Date due: April 4, 11:59pm')
print('I pledge that I have completed this assignment without collaborating')
print('with anyone else, in conformance with the NYU School of Engineering')
print('Policies and Procedures on Academic Misconduct.')"""
def find_longest_word_in_file(file_path):
    longest = ""

    try:
        file = open(file_path, 'r')
    except FileNotFoundError:
        print('file not found')
        return ''


    for line in file:
        word = ""
        line = line.strip()
        line += " "
        for char in line:

            if char.isalnum():
                word += char
            else:
                if len(word) > len(longest):
                    longest = word
                word = ""
    file.close()
    return longest


def replace_substr_in_file(file_path, target_substr, replacement_word):


    try:
        file = open(file_path, 'r')
    except FileNotFoundError:
        print('file not found')
        return
    contents = file.read()
    file.close()
    new_contents = contents.replace(target_substr, replacement_word)
    file = open(file_path, 'w')
    file.write(new_contents)
    file.close()


def count_word_occurrences_in_file(file_path, target_word):
    try:
        file = open(file_path, 'r')
    except FileNotFoundError:
        print('file not found')
        return ''
    content = file.read()
    count = 0
    word = ''
    for char in content:
        if char.isalnum():
            word += char
        else:
            if word == target_word:
                count += 1
            word = ""
    if word == target_word:
        count += 1
    return count


def main():
    input_file = "input.txt"

    print(f"Longest word in the file: {find_longest_word_in_file(input_file)}")
    target_word = "test"
    replacement_word = "exam"
    replace_substr_in_file(input_file, target_word, replacement_word)
    print(f'Replaced "{target_word}" with "{replacement_word}" in the file.')
    word_to_count = "exam"
    word_occurrences = count_word_occurrences_in_file(input_file, word_to_count)
    print(f'Occurrences of "{word_to_count}" in the file: {word_occurrences}')


main()
