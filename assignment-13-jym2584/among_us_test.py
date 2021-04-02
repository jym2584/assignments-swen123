from among_us_core import *
import random

def test_task(capsys):
    name = "Fix Wiring"
    location = "Electrical"

    task = Task(name, location)
    print(task)
    captured_out = capsys.readouterr().out
    assert "Fix Wiring in Electrical" == captured_out.strip()

def test_create_tasks(capsys):
    lists = "[Align Engine Output in Upper Engine, " \
        "Align Engine Output in Lower Engine, " \
        "Calibrate Distributor in Electrical, " \
        "Chart Course in Navigation, " \
        "Clean O2 Filter in O2, " \
        "Clear Asteroids in Weapons, " \
        "Divert Power in Communications, " \
        "Divert Power in Electrical, " \
        "Divert Power in Lower Engine, " \
        "Divert Power in Navigation, " \
        "Divert Power in O2, " \
        "Divert Power in Reactor, " \
        "Divert Power in Security, " \
        "Divert Power in Shields, " \
        "Divert Power in Upper Engine, " \
        "Empty Chute in O2, " \
        "Empty Chute in Storage, " \
        "Empty Garbage in Storage, " \
        "Fix Wiring in Admin, " \
        "Fix Wiring in Electrical, " \
        "Fix Wiring in Navigation, " \
        "Fix Wiring in Security, " \
        "Fix Wiring in Storage, " \
        "Fuel Engines in Lower Engine, " \
        "Fuel Engines in Storage, " \
        "Fuel Engines in Upper Engine, " \
        "Inspect Sample in MedBay, " \
        "Prime Shields in Shields, " \
        "Stabilize Steering in Navigation, " \
        "Start Reactor in Reactor, " \
        "Submit Scan in MedBay, " \
        "Swipe Card in Admin, " \
        "Unlock Manifolds in Reactor, " \
        "Upload Data in Admin, " \
        "Upload Data in Communications, " \
        "Upload Data in Electrical, " \
        "Upload Data in Navigation, " \
        "Upload Data in Weapons]"
    
    task_list = create_tasks()
    print(task_list)

    captured_out = capsys.readouterr().out
    assert lists == captured_out.strip()

def test_crewmate():
    random.seed(1)
    tasks_list = create_tasks()

    purple = Crewmate("Purple")

    # Testing that there is 2 tasks on our crewmate
    purple.assign_task(tasks_list[random.randint(0, len(tasks_list))])
    purple.assign_task(tasks_list[random.randint(0, len(tasks_list))])
    assert "[Divert Power in Lower Engine, Upload Data in Navigation]" == str(purple.get_tasks())
    
    # Testing that there is now 1 task on our crewmate
    purple.next_task()
    assert "[Divert Power in Lower Engine]" == str(purple.get_tasks())

    # Testing everything else
    assert "Purple" == purple.get_color()
    assert False == purple.is_murdered()

def test_ship():
    #setup
    tasks_list = create_tasks()
    locations = set()

    for task in tasks_list:
        locations.add(task.get_location())
    
    #invoke
    the_ship = Ship(tasks_list)

    #assert
    assert locations == the_ship.get_locations()
    assert tasks_list == the_ship.get_tasks()

def test_create_crewmates():
    tasks_list = create_tasks()
    the_ship = Ship(tasks_list)
    
    crewmates = the_ship.create_crewmates()

    assert len(crewmates) == 10

def test_add_tasks():
    random.seed(1)
    tasks_list = create_tasks()
    the_ship = Ship(tasks_list)
    
    crewmates = the_ship.add_tasks()

    assert str(crewmates[0].get_tasks()) == "[Swipe Card in Admin]"

def test_create_imposters():
    tasks_list = create_tasks()
    the_ship = Ship(tasks_list) 
    value = 1
    crewmates = the_ship.create_imposters(value)
    
    assert crewmates[0].is_imposter() == True


def test_cafeteria(capsys):
    random.seed(1)
    tasks_list = create_tasks()
    the_ship = Ship(tasks_list)
    value = 1
    
    the_ship.cafeteria(value)
    captured_out = capsys.readouterr().out
    assert captured_out.strip().split("\n")[-13] == 'The crew has made it!'