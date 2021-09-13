class Stack:
    def __init__(self, list = None):
        if list == None:
          self.items = []
        else:
          self.items = list

    def push(self, data):
         self.items.append(data)

    def pop(self,n):
       if len(self.items) <= 0:
          return "No element in the Stack"
       else:
          return self.items.pop(n)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.items[-1]


def convert_string(string):
    li = list(string.split(","))
    return li


def is_car_dup(list,car):
    if list.count(car) > 0:
        return True
    else:
        return False



print("******** Parking Lot ********")

m, s, o, n = input("Enter max of car,car in soi,operation : ").split()

m, n = int(m), int(n)
car_in_soi = Stack(convert_string((s)))
car_in_soi2 = Stack()



if car_in_soi.size() == 1 and car_in_soi.items[0] == '0':
    car_in_soi.pop(0)
if o == "depart":
    if is_car_dup(car_in_soi.items,str(n)) or car_in_soi.is_empty():
        if car_in_soi.size() == 0:
            print("car {0} cannot depart : Soi Empty".format(n))
            print(list(map(int,car_in_soi.items)))
        else:
            car_in_soi.items.remove(str(n))
            print("car {0} depart ! : Car {0} was remove".format(n))
            print(list(map(int,car_in_soi.items)))
    elif not car_in_soi.size() == 0:
        print("car {0} cannot depart : Dont Have Car {0}".format(n))
        print(list(map(int, car_in_soi.items)))

elif o == "arrive":
    if not is_car_dup(car_in_soi.items,str(n)):
        if car_in_soi.size() >= m:
            print("car {0} cannot arrive : Soi Full".format(n))
            print(list(map(int,car_in_soi.items)))
        else:
            car_in_soi.push(str(n))
            print("car {0} arrive! : Add Car {0}".format(n))
            print(list(map(int,car_in_soi.items)))
    else:
        print("car {0} already in soi ".format(n))
        print(list(map(int,car_in_soi.items)))