from start import cin
from NKA.parser_to_dict import parser


def main():
    # stt = cin()
    dic = parser('ab(a|b)')

    print(dic)


if __name__ == '__main__':
    main()
