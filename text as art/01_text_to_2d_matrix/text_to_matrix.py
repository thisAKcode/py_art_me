# python3
# function receives text and a length of the string
THIS_INPT = "THISAKCODE"

set_of_nice = [
    "YOURCODENAMEISMILO",
    "PERPENDECULARDRILL",
    "EASYPEASYHELL",
    "WALLOFSHAMEONYOU",
]


def text_to_mtrx(input_text, line_length):

    for i in range(len(input_text)):
        if i % line_length == 0:  # mod div returns remainder
            sub = input_text[i : i + line_length]
            lst = []
            for j in sub:
                lst.append(j)
            print(" ".join(lst))


(text_to_mtrx(THIS_INPT, 3))

for i in set_of_nice:
    text_to_mtrx(i, 4)
