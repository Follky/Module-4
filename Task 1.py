def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            num_developers = 0

            for line in file:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total_salary += salary
                num_developers += 1
            average_salary = total_salary / num_developers if num_developers > 0 else 0
            return total_salary, average_salary

    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None