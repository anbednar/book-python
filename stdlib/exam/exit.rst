.. _Stdlib Exam:

***********
Stdlib Exam
***********


Label encoder
=============
* Complexity level: medium
* Lines of code to write: 13 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/loop_label_encoder.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define:

        * ``features: List[tuple]`` - measurements
        * ``labels: List[int]`` - species

    #. Separate header from data
    #. To encode and decode ``labels`` (species) we need ``label_encoder: Dict[int, str]``:

        * key - id (incremented integer value)
        * value - species name

    #. ``label_encoder`` must be generated from ``DATA``
    #. For each row add appropriate data to ``features``, ``labels`` and ``label_encoder``
    #. Print ``features``, ``labels`` and ``label_encoder``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj:

        * ``features: List[tuple]`` - pomiary
        * ``labels: List[int]`` - gatunki
        * ``label_encoder: Dict[int, str]`` - słownik podmiany nazw gatunków

    #. Odseparuj nagłówek od danych
    #. Aby móc zakodować i odkodować ``labels`` (gatunki) potrzebny jest ``label_encoder: Dict[int, str]``:

        * key - identyfikator (kolejna liczba rzeczywista)
        * value - nazwa gatunku

    #. ``label_encoder`` musi być wygenerowany z ``DATA``
    #. Dla każdego wiersza dodawaj odpowiednie dane do ``feature``, ``labels`` i ``label_encoder``
    #. Wypisz ``feature``, ``labels`` i ``label_encoder``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        from typing import List, Dict


        features: List[tuple] = [
            (5.8, 2.7, 5.1, 1.9),
            (5.1, 3.5, 1.4, 0.2),
            (5.7, 2.8, 4.1, 1.3),
            (6.3, 2.9, 5.6, 1.8),
            (6.4, 3.2, 4.5, 1.5),
            (4.7, 3.2, 1.3, 0.2), ...]

        labels: List[int] = [0, 1, 2, 1, 2, 0, ...]

        label_encoder: Dict[int, str] = {
            0: 'virginica',
            1: 'setosa',
            2: 'versicolor'}


:The whys and wherefores:
    * ``dict`` lookups
    * Dynamic ``dict`` generating
    * ``dict`` reversal


Relational Files Database
=========================
* Complexity level: medium
* Lines of code to write: 100-150 lines
* Estimated time of completion: 60 min
* Solution: :download:`solution/exam.py`

:English:
    #. Use data from "Input" section (see below)
    #. Save listings content to files:

        * ``etc_passwd.txt`` - :numref:`code-exam-etc-passwd`
        * ``etc_shadow.txt`` - :numref:`code-exam-etc-shadow`
        * ``etc_group.txt`` - :numref:`code-exam-etc-group`

    #. Copy also comments and empty lines
    #. Parse files and convert it to ``result: List[dict]``
    #. Return list of users with ``UID`` greater than 1000
    #. User dict should contains data collected from all files
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz treści listingów do plików:

        * ``etc_passwd.txt`` - :numref:`code-exam-etc-passwd`
        * ``etc_shadow.txt`` - :numref:`code-exam-etc-shadow`
        * ``etc_group.txt`` - :numref:`code-exam-etc-group`

    #. Skopiuj również komentarze i puste linie
    #. Sparsuj plik i przedstaw go w formacie ``result: List[dict]``
    #. Zwróć listę użytkowników, których ``UID`` jest większy niż 1000
    #. Dict użytkownika powinien zawierać dane z wszystkich plików
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. literalinclude:: data/etc-passwd.txt
        :name: code-exam-etc-passwd
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/passwd``

    .. literalinclude:: data/etc-shadow.txt
        :name: code-exam-etc-shadow
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/shadow``

    .. literalinclude:: data/etc-group.txt
        :name: code-exam-etc-group
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/group``

:Output:
    .. code-block:: python

        result: List[dict] = [
            {
                'username': 'twardowski',
                'uid': 1001,
                'gid': 1001,
                'home': '/home/twardowski',
                'shell': '/bin/bash',
                'algorithm': 'SHA-512',
                'password': 'tgfvvFWJJ5...k4kijuhE50',
                'salt': 'P9zn0KwR',
                'groups': {'astronauts', 'sysadmin'},
                'last_changed': datetime.date(2015, 7, 16),
                'locked': False,
            },
            ...
        ]

:The whys and wherefores:
    * :ref:`Basic Types`
    * :ref:`Basic Sequences`
    * :ref:`Basic Control Flow`
    * :ref:`Basic Loops`
    * :ref:`Basic Files`
    * :ref:`Datetime and Timezones`
