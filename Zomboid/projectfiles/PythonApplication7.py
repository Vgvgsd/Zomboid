from module1 import load_csv, list_elements_page, get_element_by_id, search_elements_by_name, count_element

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
    file_path = input("Enter path to CSV file: ")
    try:
        data = load_csv(file_path)
    except Exception as e:
        print("Error reading file:", e)
        return

    if not data:
        print("CSV is empty or incorrectly formatted.")
        return

    while True:
        print("\nOptions:")
        print("1. Show items (paginated)")
        print("2. Get item by ID")
        print("3. Search items by name")
        print("4. Count item by name")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            paginate(data)
        elif choice == '2':
            element_id = input("Enter ID: ")
            item = get_element_by_id(data, element_id)
            if item:
                print(item)
            else:
                print("Item not found.")
        elif choice == '3':
            name = input("Enter name to search: ")
            results = search_elements_by_name(data, name)
            if results:
                for r in results:
                    print(r)
            else:
                print("No items found.")
        elif choice == '4':
            name = input("Enter name to count: ")
            total = count_element(data, 'name', name)
            print(f"Total quantity of '{name}': {total}")
        elif choice == '5':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
