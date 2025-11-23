import argparse
from module1 import (
    load_csv,
    list_elements_page,
    get_element_by_id,
    search_elements_by_name,
    count_element,
    state_percentage_all,
    state_percentage_by_name
)

def paginate(data, page_size=20):
    page = 1
    while True:
        page_data = list_elements_page(data, page, page_size)
        if not page_data:
            print("End of list.")
            break

        print(f"\n--- Page {page} ---")
        for item in page_data:
            print(item)

        cmd = input("\nPress Enter for next page, or 'q' to quit: ")
        if cmd.lower() == 'q':
            break
        page += 1


def main():
    parser = argparse.ArgumentParser(description="CSV Inventory CLI")
    parser.add_argument("file", help="Path to CSV file")
    parser.add_argument("--list", action="store_true", help="Show items paginated")
    parser.add_argument("--get", type=str, help="Get item by ID")
    parser.add_argument("--search", type=str, help="Search items by name")
    parser.add_argument("--count", type=str, help="Count items by name")
    parser.add_argument("--state_all", action="store_true", help="Show state percentages for all items")
    parser.add_argument("--state_name", type=str, help="Show state percentages for a specific item name")
    parser.add_argument("--page_size", type=int, default=20, help="Page size for pagination")
    
    args = parser.parse_args()

    try:
        data = load_csv(args.file)
    except Exception as e:
        print("Error reading file:", e)
        return

    if args.list:
        paginate(data, args.page_size)
    elif args.get:
        item = get_element_by_id(data, args.get)
        print(item if item else "Item not found")
    elif args.search:
        results = search_elements_by_name(data, args.search)
        for r in results:
            print(r)
        if not results:
            print("No items found")
    elif args.count:
        total = count_element(data, 'name', args.count)
        print(f"Total quantity of '{args.count}': {total}")
    elif args.state_all:
        percentages = state_percentage_all(data)
        for state, perc in percentages.items():
            print(f"{state}: {perc}%")
    elif args.state_name:
        percentages = state_percentage_by_name(data, args.state_name)
        if not percentages:
            print("No items found with that name")
        else:
            for state, perc in percentages.items():
                print(f"{state}: {perc}%")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

