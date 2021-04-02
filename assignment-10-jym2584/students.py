def make_student(id, name): # O(c)
    # ID, Name, Credits, GPA
    data_list = [id, name, 0, 0]
    return data_list

def add_student(population, id, name): # O(n)
    population[id] = make_student(id, name)

def get_student(population, id): # O(n)
    return population[id]

def add_credits(population, id, credits): # O(n)
    student = get_student(population, id)
    #credits_init = student[2]
    student[2] += credits
    #print("Added ", credits," credits to ",student[1],". (Had: ", credits_init," | Has: ",get_credits(population,id),")", sep="")
    return student

def get_credits(population, id):
    student = get_student(population, id)
    #print(student[1],"'s credits: ", student[2], sep = "")
    return student[2]

def main():
    #main_make_student()
    population = {}
    add_student(population, "1a", "Bruce")
    add_student(population, "1b", "Bobby")
    add_student(population, "1c", "John")
    add_student(population, "1d", "Jane")

    print(get_student(population, '1b'))
    print(add_credits(population, '1c', 10))
    print(get_credits(population, '1c'))
    print(population)

if __name__ == "__main__":
    main()