def represent(data):
    w = 10

    def print_dir_name():
        print(f"\n{'DIRECTORY':^{w + 4}}{str(data['path']):<{40}}")
        print('-' * 95)

    def print_header():
        print(f"{'Language':^{w + 4}}{'File':^{w}}{'%':^{w}}"
              f"{'Code':^{w}}{'%':^{w}}"
              f"{'Comments':^{w}}{'%':^{w}}"
              f"{'Empty':^{w}}{'%':^{w}}")
        print('-' * 95)

    def print_row(files_type, file, code, comments, empty):
        print_row.count += 1

        file_percent = file / data['all_files']

        if code != 0:
            code_percent = code / data['total_code']
        else:
            code_percent = 0

        if comments != 0:
            comments_percent = comments / data['total_comments']
        else:
            comments_percent = 0

        if empty != 0:
            empty_percent = empty / data['total_empty']
        else:
            empty_percent = 0

        print(f"{print_row.count:>{3}}.{files_type:<{w}}{file:^{w}}{file_percent:^{w}.2%}"
              f"{code:^{w}}{code_percent:^{w}.1%}"
              f"{comments:^{w}}{comments_percent:^{w}.1%}"
              f"{empty:^{w}}{empty_percent:^{w}.1%}")

    print_row.count = 0

    def python_files_structure():
        code = data['python_code_files']
        test = data['python_test_files']
        all = data['python_files']
        print(f"{'PYTHON FILES':^{95}}")
        print('-' * 95)
        print(f"{'.py files':^{w * 3}}{'_test.py files':^{w * 3}}{'all files':^{w * 3}}\n"
              f"{code:^{w * 3}}{test:^{w * 3}}{all:^{w * 3}}\n"
              f"{code / all:^{w * 3}.1%}{test / all:^{w * 3}.1%}{'100%':^{w * 3}}\n")

    def print_ten_biggest_files(file_name, lst):
        print(f"{f'TEN BIGGEST {file_name} FILES':^{95}}")
        print('-' * 95)
        print(
            f"{'FILE NAME':^{35}}"
            f"{'CODE':^{10}}{'%':^{5}}"
            f"{'COMMENTS':^{10}}{'%':^{5}}"
            f"{'EMPTY':^{10}}{'%':^{5}}"
            f"{'TOTAL':^{15}}")
        print('-' * 95)

        count = 0
        for code, comments, empty, total, name in lst:
            count += 1
            print(f"{count:>{3}}.{name:<{31}}"
                  f"{code:^{10}}{code / total:<{5}.1%}"
                  f"{comments:^{10}}{comments / total:<{5}.1%}"
                  f"{empty:^{10}}{empty / total:<{5}.1%}"
                  f"{total:^{15}}")

    def print_no_files():
        print(f"{'THERE IS NOT ANY FILE IN PROJECT':^{90}}")

    def print_sum_total():
        print(f"\n{'Sum total':^{w + 4}}{data['all_files']:^{10}}"
              f"{'100%':^{w}}{data['code_lines_in_python_files']:^{w}}"
              f"{'':^{w}}{data['comment_lines_in_python_files']:^{w}}"
              f"{'':^{w}}{data['empty_lines_in_python_files']:^{w}}\n")

    if data['path']:
        print_dir_name()
        if data['all_files']:
            print_header()
        else:
            print_no_files()

    if data['python_files']:
        print_row('Python', data['python_files'], data['code_lines_in_python_files'],
                  data['comment_lines_in_python_files'], data['empty_lines_in_python_files'])
    if data['txt_files']:
        print_row('Only text', data['txt_files'], 0, 0, 0)
    if data['md_files']:
        print_row('Markdown', data['md_files'], 0, 0, 0)
    if data['html_files']:
        print_row('HTML', data['html_files'], 0, 0, 0)
    if data['css_files']:
        print_row('CSS', data['css_files'], 0, 0, 0)
    if data['zip_files']:
        print_row('ZIP', data['zip_files'], 0, 0, 0)

    print_sum_total()

    if data['python_files']:
        python_files_structure()

    if data['python_ten_biggest_by_code_lines']:
        print_ten_biggest_files('PYTHON', data['python_ten_biggest_by_code_lines'])
