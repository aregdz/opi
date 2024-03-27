from flights_package import add_flight, list_flights, print_flights_destination, help_menu

if __name__ == "__main__":
    flights = []
    while True:
        command = input("Введите команду (add/list/select/help/exit): ").lower()
        if command == 'add':
            add_flight(flights)
        elif command == 'list':
            list_flights(flights)
        elif command == 'select':
            destination = input("Введите название пункта назначения для поиска рейсов: ")
            print_flights_destination(flights, destination)
        elif command == 'help':
            help_menu()
        elif command == 'exit':
            print("Программа завершена.")
            break
        else:
            print("Неправильная команда. Введите 'help' для получения справки.")
