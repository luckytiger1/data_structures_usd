from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, nextElem in enumerate(text):
        # print(f'{nextElem}, {i}')
        if nextElem in "([{":
            opening_brackets_stack.append([nextElem, i + 1])

        if nextElem in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            top = opening_brackets_stack.pop()[0]
            # print(f'top: {top}, nextElem: {nextElem}')
            if (top == '[' and nextElem != ']') or (top == '{' and nextElem != '}') or (top == '(' and nextElem != ')'):
                return i + 1
    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0][1]
        # for i, elem in enumerate(opening_brackets_stack):
        #     if elem in "([{)]}":
        #         return text.index(elem) + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch is not None:
        print(mismatch)
    else:
        print("Success")


if __name__ == "__main__":
    main()
