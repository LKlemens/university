DYNAMIC-GENERAL-KNAPSAC
=======================
**Dane:**

  :math:`P_{i,(m_i,c_i)}`, i = 1,2,3...,n;

  gdzie :math:`P_i` – przedmiot,

  :math:`m_i` – masa i-tego przedmiotu,

  :math:`c_i` – cena i-tego przedmiotu

  :math:`M_max` – nośność (pojemność) plecaka.

**Wyniki**

  Tablica wartości :math:`P_{i,j}` najlepszych upakowań plecaka o pojemności `j` rzeczami
  rodzajów od 1 do i; dla i=1,2,….,n oraz j=1,2,… :math:`M_max`.

  Tablica :math:`Q_{i,j}` skojarzona z :math:`P_{i,j}` rzeczy :math:`P_i` pakowanych do plecaka w ostatnim ruchu.

  1) {Ustalenie wartości początkowych tablic P i Q rozszerzonych dla ujednolicenia
  obliczeń o wiersze i kolumny zerowe.}

  2) Dla kolejnych rzeczy i=1,2,…,n wykonaj krok 3.

  3) Dla kolejnych pojemności plecaka j=1,2,… Mmax wykonaj krok 4.

  4) Jeśli j >= :math:`m_i`
  {Czyli pojemność plecaka jest wystarczająca, by pomieścić rzecz i}

  oraz :math:`P_{i-1,j} < P_{i,j-m_i} + c_i` to przypisz :math:`P_{i,j} = P_{i,j-m_i} + c_i`
  oraz :math:`Q_{i,j} = i`,

  a w przeciwnym razie pozostaw wartości z poprzedniego wiersza.
  czyli przepisz :math:`P_{i,j} = P_{i-1,j}` oraz :math:`Q_{i,j} = Q_{i-1,j}`


Algorytm jest z http://www-users.mat.uni.torun.pl/~henkej/knapsack.pdf,
z tym że na stronie w punkcie 4 jest błąd, który uwzględniłem w implementacji algorytmu.

orginał: ... to przypisz :math:`P_{i-1,j} = P_{i,j-m_i} + c_i`

wersja poprawiona: ... to przypisz :math:`P_{i,j} = P_{i,j-m_i} + c_i`
