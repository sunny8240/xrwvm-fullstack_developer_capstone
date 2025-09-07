from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {
            "name": "NISSAN",
            "description": "Great cars. Japanese technology"
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology"
        },
        {
            "name": "Audi",
            "description": "Great cars. German technology"
        },
        {
            "name": "Kia",
            "description": "Great cars. Korean technology"
        },
        {
            "name": "Toyota",
            "description": "Great cars. Japanese technology"
        }
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
<<<<<<< HEAD
            CarMake.objects.create(
                name=data["name"],
                description=data["description"]
            )
=======
            CarMake.objects.create(name=data["name"], description=data["description"])
>>>>>>> b6bf7fc ("Flake8 Updated")
        )

    car_model_data = [
        {
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[0]
=======
            "car_make": car_make_instances[0],
>>>>>>> b6bf7fc ("Flake8 Updated")
        },
        {
            "name": "Qashqai",
            "type": "SUV",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[0]
=======
            "car_make": car_make_instances[0],
>>>>>>> b6bf7fc ("Flake8 Updated")
        },
        {
            "name": "XTRAIL",
            "type": "SUV",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[0]
=======
            "car_make": car_make_instances[0],
>>>>>>> b6bf7fc ("Flake8 Updated")
        },
        {
            "name": "A-Class",
            "type": "SUV",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[1]
=======
            "car_make": car_make_instances[1],
>>>>>>> b6bf7fc ("Flake8 Updated")
        },
        {
            "name": "C-Class",
            "type": "SUV",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[1]
=======
            "car_make": car_make_instances[1],
>>>>>>> b6bf7fc ("Flake8 Updated")
        },
        {
            "name": "E-Class",
            "type": "SUV",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[1]
        },
        {
            "name": "A4",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2]
        },
        {
            "name": "A5",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2]
        },
        {
            "name": "A6",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2]
        },
=======
            "car_make": car_make_instances[1],
        },
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
>>>>>>> b6bf7fc ("Flake8 Updated")
        {
            "name": "Sorrento",
            "type": "SUV",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[3]
=======
            "car_make": car_make_instances[3],
>>>>>>> b6bf7fc ("Flake8 Updated")
        },
        {
            "name": "Carnival",
            "type": "SUV",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[3]
=======
            "car_make": car_make_instances[3],
>>>>>>> b6bf7fc ("Flake8 Updated")
        },
        {
            "name": "Cerato",
            "type": "Sedan",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[3]
=======
            "car_make": car_make_instances[3],
>>>>>>> b6bf7fc ("Flake8 Updated")
        },
        {
            "name": "Corolla",
            "type": "Sedan",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[4]
=======
            "car_make": car_make_instances[4],
>>>>>>> b6bf7fc ("Flake8 Updated")
        },
        {
            "name": "Camry",
            "type": "Sedan",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[4]
=======
            "car_make": car_make_instances[4],
>>>>>>> b6bf7fc ("Flake8 Updated")
        },
        {
            "name": "Kluger",
            "type": "SUV",
            "year": 2023,
<<<<<<< HEAD
            "car_make": car_make_instances[4]
        }
=======
            "car_make": car_make_instances[4],
        },
>>>>>>> b6bf7fc ("Flake8 Updated")
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            car_make=data["car_make"],
            type=data["type"],
            year=data["year"]
        )
