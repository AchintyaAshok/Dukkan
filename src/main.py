import json

class Item:
    _name = None
    _price_per_kg = None
    _item_number = None

    def __init__(self, name, item_number, price):
        self._name = name
        self._item_number = item_number
        self._price_per_kg = float(price)

    def to_dict(self):
        return {
            'Name': self._name,
            'Item No.': self._item_number,
            'Price Per Kg.': self._price_per_kg
        }

ALL_ITEMS = {}


def add_item():
    item_name = raw_input('What is the name of the item?\t')
    item_number = input('What is the item #?\t')
    price = raw_input('What is the price per kg of the item?\t')

    item = Item(item_name, item_number, price)
    ALL_ITEMS[item_name.lower()] = item

    print('\n -- Item "{}" was added successfully.'.format(item_name))


def list_items():
    all_items = map(lambda i: i.to_dict(), ALL_ITEMS.values())
    def sort_alpha(item_a, item_b):
        item_a_name = item_a['Name']
        item_b_name = item_b['Name']
        if item_a_name == item_b_name:
            return 0
        elif item_a_name < item_b_name:
            return -1
        else:
            return 1


    all_items.sort(cmp=sort_alpha)

    print(json.dumps(all_items, indent=2))


def find_item():
    original_query = raw_input('What is the name of the item?\t')
    query = original_query.lower()
    if query in ALL_ITEMS:
        print(json.dumps(ALL_ITEMS[query].to_dict(), indent=2))
        return ALL_ITEMS[query]
    else:
        choice = raw_input('No item named "{}" could be found. Try Again? Yes/No'.format(original_query))
        choice = choice.lower()
        if choice == 'yes':
            find_item()


def price_item():
    item = find_item()
    if not item:
        print('No item could be priced.')

    quantity = input('What is its weight?\t')
    quantity = float(quantity)
    price_per_kg = item._price_per_kg
    print('For Weight: {} | Price => {}'.format(quantity, quantity * price_per_kg))


def start():
    while(True):
        print('\n\nPlease choose to list all items or add a new item.')
        print('\t- To list all items, type "list"')
        print('\t- To add a new item, type "add"')
        print('\t- To find an item, type "find"')
        print('\t- To price an item, type "price"')

        user_option = raw_input('\nWhat would you like to do?\t')
        user_option = user_option.lower()
        if user_option not in ['list', 'add', 'find', 'price']:
            print('Unacceptable option. Please choose a correct option.')
        else:
            if user_option == 'list':
                list_items()
            elif user_option == 'add':
                add_item()
            elif user_option == 'find':
                find_item()
            elif user_option == 'price':
                price_item()


if __name__ == '__main__':
    print('Starting Dukkan...')
    start()


