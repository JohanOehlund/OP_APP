import re


class ValidityChecker(object):

    @staticmethod
    def not_null(k_data: str) -> bool:
        if k_data is None:
            raise TypeError('Personal code is None')
        return True

    def is_personal_code(self, k_data: str) -> bool:
        nr_regex = '^[0-9]{8}-[0-9]{4}$'
        per_nr_match = re.search(nr_regex, k_data.strip())
        if per_nr_match:
            pr_nr = per_nr_match.group()
            control_nr = int(pr_nr[-1])
            modified_pr_nr = list(map(int, pr_nr[2:-1].replace('-', '')))
            i = 0
            calculated_sum = 0
            for tmp_nr in modified_pr_nr:
                if i % 2 == 0:
                    tmp_calc = tmp_nr * 2
                    tmp_sum = tmp_calc if tmp_calc < 10 else int(str(tmp_calc)[0]) + int(str(tmp_calc)[1])
                else:
                    tmp_sum = tmp_nr
                calculated_sum += tmp_sum
                i += 1
            result = (10 - (calculated_sum % 10)) % 10
            if result == control_nr:
                return True
            raise SyntaxError('Personal code is not valid: {}'.format(k_data))
        else:
            raise SyntaxError('Invalid personal code syntax: {}, should be YYYYMMDD-XXXX'.format(k_data))
