.. _Iterators:

*********
Iterators
*********


Protocol
========
* ``__iter__(self) -> self``
* ``__next__(self) -> raise StopIteration``


Mechanism
=========

For loop
--------
.. code-block:: python
    :caption: For loop

    DATA = [1, 2, 3]

    for current in DATA:
        print(current)

Intuitive implementation of the ``for`` loop
--------------------------------------------
.. code-block:: python
    :caption: Intuitive implementation of the ``for`` loop

    DATA = [1, 2, 3]

    iterator = DATA.__iter__()

    try:
        current = iterator.__next__()
        print(current)

        current = iterator.__next__()
        print(current)

        current = iterator.__next__()
        print(current)

        current = iterator.__next__()
        print(current)
    except StopIteration:
        pass


Iterating over objects
======================

Iterating sequences
-------------------
.. code-block:: python

    for number in [1, 2, 3]:
        print(number)

    # 1
    # 2
    # 3

.. code-block:: python

    for key, value in [('a',1), ('b',2), ('c',3)]:
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3

Iterating over ``dict``
-----------------------
.. code-block:: python

    DATA = {'a': 1, 'b': 2, 'c': 3}

    for element in DATA:
        print(element)

    # a
    # b
    # c

.. code-block:: python

    for key, value in DATA.items():
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3

Iterating over ``str``
----------------------
.. code-block:: python

    for character in 'hello':
        print(character)

    # h
    # e
    # l
    # l
    # o


Own Implementation
==================
.. code-block:: python

    class Parking:
        def __init__(self):
            self._parked_cars = list()

        def park(self, car):
            self._parked_cars.append(car)

        def __iter__(self):
            self._current_element = 0
            return self

        def __next__(self):
            if self._current_element >= len(self._parked_cars):
                raise StopIteration

            result = self._parked_cars[self._current_element]
            self._current_element += 1
            return result


    parking = Parking()
    parking.park('Mercedes')
    parking.park('Maluch')
    parking.park('Toyota')


    for car in parking:
        print(car)

    # Mercedes
    # Maluch
    # Toyota


``itertools``
=============

``chain()``
-----------
.. code-block:: python

    keys = ['a', 'b', 'c']
    values = [1, 2, 3]

    for x in chain(keys, values):
        print(x)

    # a
    # b
    # c
    # 1
    # 2
    # 3

.. code-block:: python

    from itertools import chain


    class Character:
        def __init__(self, *values):
            self.values = values
            self._iter_index = 0

        def __iter__(self):
            self._iter_index = 0
            return self

        def __next__(self):
            if self._iter_index >= len(self.values):
                raise StopIteration

            element = self.values[self._iter_index]
            self._iter_index += 1
            return element


    class Number:
        def __init__(self, *values):
            self.values = values
            self._iter_index = 0

        def __iter__(self):
            self._iter_index = 0
            return self

        def __next__(self):
            if self._iter_index >= len(self.values):
                raise StopIteration

            element = self.values[self._iter_index]
            self._iter_index += 1
            return element


    chars = Character('a', 'b', 'c')
    nums = Number(1, 2, 3)

    print(chain(chars, nums))
    # <itertools.chain object at 0x1008ca0f0>

    print(list(chain(chars, nums)))
    # [1, 2, 3, 'a', 'b', 'c']

    for x in chain(chars, nums):
        print(x)

    # a
    # b
    # c
    # 1
    # 2
    # 3

``cycle()``
-----------
.. code-block:: python

    from itertools import cycle

    DATA = ['even', 'odd']

    for x in cycle(DATA):
        print(x)

    # even
    # odd
    # even
    # odd
    # even
    # ...

.. code-block:: python

    from itertools import cycle

    DATA = ['even', 'odd']

    for i, status in enumerate(cycle(DATA)):
        print(i, status)

        if i == 3:
            break

    # 0, even
    # 1, odd
    # 2, even
    # 3, odd


Assignments
===========

Protocol Iterator Usage
-----------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/protocol_iterator_usage.py`

:English:
    #. Write own implementation of a ``range()`` function
    #. Use iterator protocol
    #. Arguments: start, stop, step
    #. How to implement passing only stop argument?

:Polish:
    #. Zaimplementuj własne rozwiązanie ``range()``
    #. Use iterator protocol
    #. Argumenty: początek, koniec, krok
    #. Jak zaimplementować możliwość podawania tylko końca?

Protocol Iterator Implementation
--------------------------------
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/protocol_iterator_implementation.py`

:English:
    #. Use data from "Input" section (see below)
    #. Modify classes to implement iterator
    #. Iterate over object using ``for`` loop
    #. Print data
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj data z sekcji "Input" (patrz poniżej)
    #. Zmodyfikuj klasy aby zaimplementować protokół iterator
    #. Iteruj po obiekcie używając pętli ``for``
    #. Wypisz dane
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        from dataclasses import dataclass


        @dataclass
        class Astronaut:
            first_name: str
            last_name: str
            missions: tuple = ()

        @dataclass
        class Mission:
            year: int
            name: str


        twardowski = Astronaut('Jan', 'Twardowski', missions=(
            Mission(1969, 'Apollo 11'),
            Mission(2024, 'Artemis 3'),
            Mission(2035, 'Ares 3'),
        ))

:Output:
    .. code-block:: python

        Mission(year=1969, name='Apollo 11')
        Mission(year=2024, name='Artemis 3')
        Mission(year=2035, name='Ares 3')
