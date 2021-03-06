.. _Loop While:

**********
Loop While
**********


Syntax
======
.. highlights::
    * Continue execution when argument is ``True``
    * Stops if argument is ``False``

.. code-block:: python
    :caption: ``while`` loop generic syntax
    :force:

    while <condition>:
        <do something>


Convention
==========
* The longer the loop scope, the longer the variable name should be
* Avoid one letters if scope is longer than one line
* Generic names:

    * ``i`` - for loop counter
    * ``abort`` - for abort flags
    * ``abort_flag`` - for abort flags


Use Cases
=========
.. code-block:: python
    :caption: Never ending loop. Used in servers to wait forever for incoming connections

    while True:
        print('hello')

.. code-block:: python
    :caption: Stop conditions

    i = 0

    while i < 3:
        print(i)
        i += 1

    # 0
    # 1
    # 2

.. code-block:: python
    :caption: Iterating over sequence. Better idea for this is to use ``for`` loop. ``for`` loop supports Iterators. ``len()`` must write all ``numbers`` to memory, to calculate its length

    i = 0
    data = ['a', 'b', 'c']

    while i < len(data):
        print(i, data[i])
        i += 1

    # 0 'a'
    # 1 'b'
    # 2 'c'

.. code-block:: python
    :caption: Exit flag. Exit flag pattern is useful if you have for example multi-threaded application

    print('Ignition sequence started')
    abort = False
    i = 10

    while not abort:
        print(i)
        i -= 1

        if i == 6:
            print('Fuel leak detected. Abort, Abort, Abort!')
            abort = True

    # Ignition sequence started
    # 10
    # 9
    # 8
    # 7
    # Fuel leak detected. Abort, Abort, Abort!


Force Exit the Loop
===================
.. code-block:: python
    :caption: Force exit the loop using ``break`` keyword

    print('Ignition sequence started')
    i = 10

    while True:
        print(i)
        i -= 1

        if i == 6:
            print('Fuel leak detected. Abort, Abort, Abort!')
            break

    # Ignition sequence started
    # 10
    # 9
    # 8
    # 7
    # Fuel leak detected. Abort, Abort, Abort!

.. code-block:: python
    :caption: Exiting the loop using ``break`` keyword

    while True:
        number = input('Type number: ')

        if not number:
            # if user hit enter
            # without typing a number
            break


Force Skip Iteration
====================
.. highlights::
    * if ``continue`` is encountered, it will jump to next loop iteration

.. code-block:: python
    :caption: Force skip iteration using ``continue`` keyword

    all_astronauts = ['Mark Watney', 'Jan Twardowski', 'Melissa Lewis', 'José Jiménez']
    assigned_to_mission = ['Mark Watney', 'Melissa Lewis']
    i = 0

    while i < len(all_astronauts):
        name = all_astronauts[i]
        i += 1

        if name not in assigned_to_mission:
            continue

        print(name)

    # Mark Watney
    # Melissa Lewis

.. code-block:: python
    :caption: Force skip iteration using ``continue`` keyword

    i = 0

    while i < 10:
        print(i, end=', ')
        i += 1

        if i % 3:
            continue

        print(end='\n')

    # 0, 1, 2,
    # 3, 4, 5,
    # 6, 7, 8,
    # 9,


Assignments
===========

Example
-------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_while_example.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create ``result: List[int]``
    #. Use ``while`` to iterate over ``DATA``
    #. Convert all elements of ``DATA`` to ``int``
    #. Converted values add to ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz ``result: List[int]``
    #. Użyj ``while`` do iterowania po ``DATA``
    #. Przekonwertuj wszystkie elementy ``DATA`` do ``int``
    #. Przekonwertowane wartości dodaj do ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = ['1', '2', '3']

:Output:
    .. code-block:: python

        result: List[int]
        # [1, 2, 3]

:Solution:
    .. literalinclude:: solution/loop_while_example.py
        :language: python

Loop For Substitute
-------------------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_while_substitute.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define ``result: list``
    #. Use ``while`` to iterate over ``DATA``
    #. If letter is in ``PL_ASCII`` then use conversion value as letter
    #. Add letter to ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj ``while`` do iteracji po ``DATA``
    #. Jeżeli litera jest w ``PL_ASCII`` to użyj przekonwertowanej wartości jako litera
    #. Dodaj literę do ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        PL_ASCII = {
            'ą': 'a',
            'ć': 'c',
            'ę': 'e',
            'ł': 'l',
            'ń': 'n',
            'ó': 'o',
            'ś': 's',
            'ż': 'z',
            'ź': 'z',
        }

        DATA = 'zażółć gęślą jaźń'

:Output:
    .. code-block:: python

        result: str
        # 'zazolc gesla jazn'

Loop While Convert
------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_while_convert.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create ``result: List[int]``
    #. Use ``while`` to iterate over ``DATA``
    #. Convert all elements of ``DATA`` to ``int``
    #. Converted values add to ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz ``result: List[int]``
    #. Użyj ``while`` do iterowania po ``DATA``
    #. Przekonwertuj wszystkie elementy ``DATA`` do ``int``
    #. Przekonwertowane wartości dodaj do ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = (2, 3, 3.5, 4, 4.5, 5)

:Output:
    .. code-block:: python

        result: List[int]
        # [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]

:The whys and wherefores:
    * Reading user input
    * Input validation
    * Type casting
    * Sequences
    * Using while loop
    * Breaking loop
    * Using built-in functions

:Hints:
    * ``input(...)``
    * ``mean = sum(...) / len(...)``

Loop While Input
----------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/loop_while_input.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``while`` Create ``grade_scale: List[float]`` from ``DATA`` (convert values to ``float``)
    #. Using ``input()`` ask user about grade, one at a time
    #. User will type only valid ``int`` or ``float``
    #. To iterate use only ``while`` loop
    #. If grade is on a new grade scale - add it to report card
    #. If grade is not on a new grade scale - print "Grade is not allowed" and continue input
    #. If user pressed Enter key, end inserting data
    #. At the end, print calculated mean
    #. Test case when report list is empty

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Używając ``while`` stwórz ``grade_scale: List[float]`` z ``DATA`` (przekonwertuj wartości do ``float``)
    #. Do iterowania użyj tylko pętli ``while``
    #. Używając ``input()`` poproś użytkownika o ocenę, jedną na raz
    #. Użytkownik poda tylko poprawne ``int`` lub ``float``
    #. Jeżeli ocena jest w ``grade_scale`` - dodaj ją do dzienniczka
    #. Jeżeli oceny nie ma w ``grade_scale`` - wyświetl "Grade is not allowed" i kontynuuj wpisywanie
    #. Jeżeli użytkownik wcisnął Enter, zakończ wprowadzanie danych
    #. Na zakończenie wyświetl wyliczoną dla dzienniczka średnią arytmetyczną
    #. Przetestuj przypadek, gdy dzienniczek jest pusty

:Input:
    .. code-block:: python

        DATA = (2, 3, 3.5, 4, 4.5, 5)

:The whys and wherefores:
    * Reading user input
    * Input validation
    * Type casting
    * Sequences
    * Using while loop
    * Breaking loop
    * Using built-in functions

:Hints:
    * ``mean = sum(...) / len(...)``
