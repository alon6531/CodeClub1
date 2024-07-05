import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py n")
        sys.exit(1)

    n = int(sys.argv[1])

    with open("C:\\Users\\PC\\PycharmProjects\\CodeClub\\AdvancedPython_Dir\\text.txt") as f:
        text = f.read()
        text = text.replace('\n', ' ')

        words_temp = text.split(" ")
        words = []

        for word in words_temp:
            temp = ''

            for i in range(len(word)):
                c = word[i]
                temp += c if c.isalpha() else ''

            if temp != '':
                words.append(temp)

        f.close()

    words_count = {}

    for word in words:
        before = 0
        if word in words_count:
            before = words_count[word]

        temp = lambda x: 1 if x else 0
        words_count[word] = temp(word in words_count) + before

    words_count = dict(sorted(words_count.items(), key=lambda item: item[1], reverse=True))
    words_count = list(words_count.keys())

    if n < len(words_count) + 1:
        for i in range(0, n):
            print(words_count[i])
    else:
        print("n is too big")


if __name__ == '__main__':
    main()