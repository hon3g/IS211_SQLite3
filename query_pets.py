import sqlite3


def main(person_id):
    con = sqlite3.connect('pets.db')
    cur = con.cursor()

    cur.execute(f'''
        SELECT first_name, last_name, person.age, name, breed, pet.age
        FROM person
        INNER JOIN person_pet
        ON person.id = person_pet.person_id
        INNER JOIN pet
        ON person_pet.pet_id = pet.id
        WHERE person.id == {person_id}
    ''')
    try:
        first_name, last_name, person_age, name, breed, pet_age = cur.fetchone()
    except TypeError:
        return '404'

    con.commit()
    con.close()
    return f'{first_name} {last_name}, {person_age} years old',\
           f'{first_name} {last_name} owned {name}, a {breed}, that was {pet_age} years old'


if __name__ == '__main__':
    while True:
        try:
            person_id = int(input("Input a person's ID number: "))
        except ValueError:
            print('Only accept an integer', end='\n\n')
            continue

        if person_id == -1:
            break
        elif main(person_id) == '404':
            print("Not found. Try again. '-1' to exit.", end='\n\n')
        else:
            person_data, pet_data = main(person_id)
            print(person_data)
            print(pet_data, end='\n\n')
