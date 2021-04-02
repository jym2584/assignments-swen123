import droids
import node_queue
import random
import node_stack
import array_queue

def unload_shipment(filename, belt):
    with open(filename) as parts_list:
        for part in parts_list:
            part = part.strip()
            belt.enqueue(part)

def install_part(droid, my_belt, their_belt):
    if not my_belt.is_empty():
        part = my_belt.dequeue()
    
        if droid.need_parts(part):
            droid.install(part)
        else:
            their_belt.enqueue(part)
    
    return droid.is_complete()

def assemble_droids(worker_belt, coworker_belt):
    cargo_ship = set()
    shipping_container = node_stack.Stack()

    p_droid = droids.Droid("Protcol Droid C" + str(random.randint(0,10000)), droids.PROTOCOL)
    a_droid = droids.Droid("Astromech Droid R" + str(random.randint(0,10000)), droids.ASTROMECH)
    while not worker_belt.is_empty() or not coworker_belt.is_empty():
        
        if install_part(p_droid, worker_belt, coworker_belt):
            print(p_droid)
            shipping_container.push(p_droid)
            if shipping_container.size() == 5:
                cargo_ship.add(shipping_container)
                shipping_container = node_stack.Stack()
            p_droid = droids.Droid("Protcol Droid C" + str(random.randint(0,10000)), droids.PROTOCOL)
        
        if install_part(a_droid, coworker_belt, worker_belt):
            print(a_droid)
            shipping_container.push(a_droid)
            if shipping_container.size() == 5:
                cargo_ship.add(shipping_container)
                shipping_container = node_stack.Stack()
            a_droid = droids.Droid("Astromech Droid R" + str(random.randint(0,10000)), droids.ASTROMECH)
    
    return cargo_ship

def main():
    belt = array_queue.Queue()
    belt2 = array_queue.Queue()
    #droid = droids.Droid("C2-BA", droids.ASTROMECH)
    filename = "data/parts_0005_0005.txt"
    unload_shipment(filename, belt)
    ship = assemble_droids(belt, belt2)
    print(ship)



if __name__ == "__main__":
    main()