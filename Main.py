from ValidityChecker import ValidityChecker


def main():
    personal_codes = ['19780202-2389', '19780202-2381', '197802022389',
                      '780202-2389', '7802022389', '19820411-2380', '123d222', ' 197802 02-2389 ']
    v_checker = ValidityChecker()
    # To test the not null method
    try:
        v_checker.not_null(None)
    except TypeError as e:
        print(e)

    # running through each personal code in the personal_codes list.
    for p_code in personal_codes:
        try:
            v_checker.not_null(k_data=p_code)
            tmp_result = v_checker.is_personal_code(k_data=p_code)
            print('Personal code: {} is valid: {}'.format(p_code, tmp_result))
        except SyntaxError as e:
            print(e)
        except TypeError as e:
            print(e)


if __name__ == "__main__":
    main()
