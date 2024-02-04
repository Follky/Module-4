def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_dict = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": int(cat_data[2])
                }
                cats_info.append(cat_dict)

    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cats_info