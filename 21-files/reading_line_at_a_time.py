line_number = 0
with open('favorite-people.txt', encoding='utf-8') as a_file:
    for a_line in a_file:
        line_number += 1
        # The format specifier {:>4} means “print this argument right-justified within 4 spaces.”
        print('{:>4} {}'.format(line_number, a_line.rstrip()))