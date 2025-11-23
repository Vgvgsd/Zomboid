def state_percentage_all(data, state_column='state'):
    """
    Return a dictionary with percentage of each state across all items.
    Example: {'Mint': 20, 'Good': 35, ...}
    """
    from collections import Counter
    total = len(data)
    if total == 0:
        return {}

    counter = Counter(row.get(state_column, 'Unknown') for row in data)
    percentages = {state: round(count / total * 100, 2) for state, count in counter.items()}
    return percentages


def state_percentage_by_name(data, name, name_column='name', state_column='state'):
    """
    Return percentage of each state for items with a given name.
    """
    filtered = [row for row in data if row.get(name_column, '').lower() == name.lower()]
    return state_percentage_all(filtered, state_column)








def load_csv(file_path):
    """Load CSV into a list of dictionaries without using csv module."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        if not lines:
            return data

        headers = lines[0].split(',')
        for line in lines[1:]:
            values = line.split(',')
            if len(values) != len(headers):
                continue  # пропускаем некорректные строки
            row = dict(zip(headers, values))
            data.append(row)
    return data


def list_elements_page(data, page=1, page_size=20):
    """Return a page of elements."""
    start = (page - 1) * page_size
    end = start + page_size
    return data[start:end]


def get_element_by_id(data, element_id, id_column='id'):
    """Return element with the given ID."""
    for row in data:
        if row.get(id_column) == str(element_id):
            return row
    return None


def search_elements_by_name(data, name, name_column='name'):
    """Return list of elements that match the name."""
    results = []
    for row in data:
        if name.lower() in row.get(name_column, '').lower():
            results.append(row)
    return results


def count_element(data, column_name, element_name, quantity_column='quantity'):
    """Return the total quantity of a specific element."""
    total = 0
    for row in data:
        if row[column_name] == element_name:
            total += int(row.get(quantity_column, 0))
    return total
