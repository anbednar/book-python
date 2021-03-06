.. _OOP Methods:

*******
Methods
*******


Rationale
=========
.. highlights::
    * Methods are functions in the class
    * First argument is always instance (``self``)
    * While calling function you never pass ``self``
    * Prevents copy-paste code
    * Improves readability
    * Improves refactoring
    * Decomposes bigger problem into smaller chunks

.. glossary::

    method
        Function inside the class which takes ``self`` as a first argument.

.. code-block:: python

    point_x = 1
    point_y = 2
    point_z = 3

    print(point_x, point_y, point_z)
    # 1 2 3


.. code-block:: python

    class Point:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def get_coordinates(self):
            return self.x, self.y, self.z

        def to_string(self):
            print(f'Point(x={self.x}, y={self.y}, z={self.z})')


    point = Point(x=1, y=2, z=3)

    print(point.x)      # 1
    print(point.y)      # 2
    print(point.z)      # 3

    point.get_coordinates()
    # (1, 2, 3)

    point.to_string()
    # Point(x=1, y=2, z=3)


Methods Without Arguments
=========================
.. code-block:: python
    :caption: Methods without arguments

    class Astronaut:
        def say_hello(self):
            print('My name... José Jiménez')


    jose = Astronaut()
    jose.say_hello()
    # My name... José Jiménez


Methods With Required Argument
==============================
.. code-block:: python
    :caption: Methods with required argument

    class Astronaut:
        def say_hello(self, name):
            print(f'My name... {name}')


    jose = Astronaut()

    jose.say_hello(name='José Jiménez')
    # My name... José Jiménez

    jose.say_hello('José Jiménez')
    # My name... José Jiménez

    jose.say_hello()
    # TypeError: say_hello() missing 1 required positional argument: 'name'


Methods With Optional Argument
==============================
.. code-block:: python
    :caption: Methods with arguments with default value

    class Astronaut:
        def say_hello(self, name='Unknown'):
            print(f'My name... {name}')


    jose = Astronaut()

    jose.say_hello(name='José Jiménez')
    # My name... José Jiménez

    jose.say_hello('José Jiménez')
    # My name... José Jiménez

    jose.say_hello()
    # My name... Unknown


Methods Accessing Fields
========================
.. code-block:: python
    :caption: Methods Accessing Fields

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print(f'My name... {self.name}')


    jose = Astronaut('José Jiménez')
    jose.say_hello()
    # My name... José Jiménez

.. code-block:: python
    :caption: ``self.name`` must be defined before accessing.

    class Astronaut:
        def say_hello(self):
            print(f'My name... {self.name}')


    jose = Astronaut()
    jose.say_hello()
    # AttributeError: 'Astronaut' object has no attribute 'name'


Methods Calling Other Methods
=============================
.. code-block:: python
    :caption: Methods Calling Other Methods

    class Astronaut:
        def get_name(self):
            return 'José Jiménez'

        def say_hello(self):
            name = self.get_name()
            print(f'My name... {name}')


    jose = Astronaut()
    jose.say_hello()
    # My name... José Jiménez

.. code-block:: python
    :caption: Methods calling other methods

    class Iris:
        def __init__(self):
            self.sepal_length = 5.1
            self.sepal_width = 3.5
            self.petal_length = 1.4
            self.petal_width = 0.2

        def sepal_area(self):
            return self.sepal_length * self.sepal_width

        def petal_area(self):
            return self.petal_length * self.petal_width

        def total_area(self):
            return self.sepal_area() + self.petal_area()


    flower = Iris()
    print(flower.total_area())
    # Total area: 18.13

.. code-block:: python
    :caption: Since Python 3.7 there is a ``@dataclass`` decorator, which automatically generates ``__init__()`` arguments and fields. More information in :ref:`OOP Dataclass`.

    from dataclasses import dataclass


    @dataclass
    class Iris:
        sepal_length: float = 5.8
        sepal_width: float = 2.7
        petal_length: float = 5.1
        petal_width: float = 1.9
        species: str = 'Iris'

        def sepal_area(self):
            return self.sepal_length * self.sepal_width

        def petal_area(self):
            return self.petal_length * self.petal_width

        def total_area(self):
            return self.sepal_area() + self.petal_area()


    flower = Iris()
    print(flower.total_area())
    # Total area: 18.13


Examples
========
* Documentation: https://atlassian-python-api.readthedocs.io
* Source Code: https://github.com/atlassian-api/atlassian-python-api
* Examples: https://github.com/atlassian-api/atlassian-python-api/tree/master/examples

.. code-block:: console

    $ pip install atlassian-python-api

.. code-block:: python

    from atlassian import Jira

    jira = Jira(
        url='http://localhost:8080',
        username='admin',
        password='admin')

    JQL = 'project = DEMO AND status IN ("To Do", "In Progress") ORDER BY issuekey'

    result = jira.jql(JQL)
    print(result)

.. code-block:: python

    from atlassian import Confluence

    confluence = Confluence(
        url='http://localhost:8090',
        username='admin',
        password='admin')

    result = confluence.create_page(
        space='DEMO',
        title='This is the title',
        body='This is the body. You can use <strong>HTML tags</strong>!')

    print(result)


Assignments
===========

OOP Method Sequence
-------------------
* Complexity level: easy
* Lines of code to write: 18 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/oop_method_sequence.py`

:English:
    #. Create class ``Iris`` with ``features: List[float]`` and ``label: str`` attributes
    #. For each row in ``DATA`` create ``Iris`` instance with row values
    #. Set class attributes at the initialization from positional arguments
    #. Create method which sums values of all ``features``
    #. Print species name and a sum method result
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz klasę ``Iris`` z atrybutami ``features: List[float]`` i ``label: str``
    #. Dla każdego wiersza w ``DATA`` twórz instancję ``Iris`` z danymi z wiersza
    #. Ustaw atrybuty klasy przy iniclalizacji z argumentów pozycyjnych
    #. Stwórz metodę sumującą wartości wszystkich ``features``
    #. Wyisz nazwę gatunku i wynik metody sumującej
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
        ]

:Output:
    .. code-block:: text

        setosa 9.4
        versicolor 16.299999999999997
        virginica 19.3

OOP Methods
-----------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/oop_method_nested.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define class ``Iris``
    #. ``Iris`` has:

        * "Sepal length" type ``float``
        * "Sepal width" type ``float``
        * "Petal length" type ``float``
        * "Petal width" type ``float``
        * "Species" type ``str``

    #. ``Iris`` can:

        * Return number of ``float`` type attributes
        * Return list of all ``float`` type attributes
        * Return sum of values of all ``float`` type attributes
        * Return mean of all ``float`` type attributes

    #. Use values from ``self.__dict__`` to check for type or length
    #. Create ``setosa`` object with attributes set at the initialization
    #. Create ``virginica`` object with attributes set at the initialization
    #. Print sum, mean and name of each objects
    #. Do not use ``@dataclass``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj klasę ``Iris``
    #. ``Iris`` ma:

        * "Sepal length" typu ``float``
        * "Sepal width" typu ``float``
        * "Petal length" typu ``float``
        * "Petal width" typu ``float``
        * "Species" typu ``str``

    #. ``Iris`` może:

        * Zwrócić liczbę pól typu ``float``
        * Zwrócić listę wartości wszystkich pól typu ``float``
        * Zwrócić sumę wartości pól typu ``float``
        * Zwrócić średnią arytmetyczną wartość pól typu ``float``

    #. Użyj wartości ``self.__dict__`` do sprawdzania typu lub długości
    #. Stwórz obiekt ``setosa`` z atrybutami ustawionymi przy inicjalizacji
    #. Stwórz obiekt ``virginica`` z atrybutami ustawionymi przy inicjalizacji
    #. Wypisz sumę, średnią oraz nazwę każdego z obiektów
    #. Nie używaj ``@dataclass``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
        virginica = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

:Output:
    .. code-block:: text

        total=10.20 mean=2.55 setosa
        total=15.50 mean=3.88 virginica
