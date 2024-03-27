def add_flight(flights):
    # Функция для добавления рейса
    destination = input("Введите пункт назначения рейса: ")
    flight_number = input("Введите номер рейса: ")
    plane_type = input("Введите тип самолета: ")
    flights.append({"destination": destination, "flight_number": flight_number, "plane_type": plane_type})
    # Сортировка списка рейсов по номеру рейса
    flights.sort(key=lambda x: x["flight_number"])
    print("Рейс успешно добавлен.")

def list_flights(flights):
    # Функция для вывода списка рейсов
    print("Список всех рейсов:")
    for flight in flights:
        print(f"Номер рейса: {flight['flight_number']}, Пункт назначения: {flight['destination']}, Тип самолета: {flight['plane_type']}")

def select_flights_destination(flights):
    # Функция для выбора рейсов по пункту назначения
    destination = input("Введите название пункта назначения для поиска рейсов: ")
    flights_to_destination = [flight for flight in flights if flight["destination"] == destination]
    if flights_to_destination:
        print(f"Рейсы в пункт назначения '{destination}':")
        for flight in flights_to_destination:
            print(f"Номер рейса: {flight['flight_number']}, Тип самолета: {flight['plane_type']}")
    else:
        print(f"Нет рейсов в пункт назначения '{destination}'.")

def help_menu():
    # Функция для вывода справки
    print("Список команд:")
    print("add - добавить рейс;")
    print("list - вывести список всех рейсов;")
    print("select - выбрать рейсы по пункту назначения;")
    print("help - вывести справку;")
    print("exit - завершить программу.")

if __name__ == "__main__":
    # Основная часть программы
    flights = []
    while True:
        command = input("Введите команду (add/list/select/help/exit): ").lower()
        if command == 'add':
            add_flight(flights)
        elif command == 'list':
            list_flights(flights)
        elif command == 'select':
            select_flights_destination(flights)
        elif command == 'help':
            help_menu()
        elif command == 'exit':
            print("Программа завершена.")
            break
        else:
            print("Неправильная команда. Введите 'help' для получения справки.")
class Flight:
    def __init__(self, destination, flight_number, plane_type):
        self.destination = destination
        self.flight_number = flight_number
        self.plane_type = plane_type

def print_flights_destination(flights, destination):
    flights_to_destination = [flight for flight in flights if flight.destination == destination]
    if flights_to_destination:
        print(f"Рейсы в пункт назначения '{destination}':")
        for flight in flights_to_destination:
            print(f"Номер рейса: {flight.flight_number}, Тип самолета: {flight.plane_type}")
    else:
        print(f"Нет рейсов в пункт назначения '{destination}'.")