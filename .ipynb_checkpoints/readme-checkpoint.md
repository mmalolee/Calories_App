# Aplikacja przewidująca ilość spalonych kalorii podczas biegu

## Opis problemu

Celem projektu jest stworzenie i wytrenowanie modelu uczenia maszynowego do szacowania liczby spalonych kalorii podczas biegu na podstawie danych fizjologicznych użytkownika. Finalny model został zaimplementowany w aplikacji webowej zbudowanej w technologii **Streamlit**, umożliwiającej użytkownikowi oszacowanie spalonych kalorii na podstawie:

- przewidywanego czasu trwania biegu (w minutach),
- tętna (w uderzeniach na minutę),
- temperatury ciała (°C),
- oraz płci.

## Wykorzystane technologie

- `pathlib`, `joblib` – operacje na ścieżkach, zapis modelu,
- `pandas`, `numpy` – analiza i manipulacja danymi,
- `matplotlib`, `seaborn` – wizualizacje,
- `scikit-learn` – model regresji liniowej, podział danych, metryki,
- `streamlit` – aplikacja webowa.

## Wykorzystane dane

Dane pochodzą z platformy [Kaggle](https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos/data?select=exercise.csv) i zawierają następujące informacje:

- dane na temat badanych (płeć, wiek, wzrost, waga, czas treningu, tętno, temperatura ciała),
- liczby spalonych kalorii.

## Struktura projektu

- calories_app_project
    - models
        - lm_females.pkl
        - lm_males.pkl
    - processed
        - females.csv
        - males.csv
    - raw
        - calories.csv
        - exercises.csv
    - app.py
    - cals.ipynb
    - readme.md
    - requirements.txt

## Uruchamianie aplikacji

- Utwórz środowisko Conda używającego Pythona w wersji 3.11.11.
- Aktywuj środowisko Conda: `conda activate env_name`.
- Zainstaluj wymagane pakiety z pliku `requirements.txt`:
    - `cd ścieżka_do_folderu_z_projektem`
    - `pip install -r requirements.txt`
- Otwórz VSCode.
- Otwórz folder z projektem w VSCode.
- Skrótem klawiszowym *CTRL + Shift + `* otwórz terminal.
- W terminalu uruchom polecenie `streamlit run app.py`.
- Zapisz kod przy pomocy *Ctrl + S*

## Kroki analizy

### 1. Wczytanie i połączenie danych

- Wczytano dane z dwóch plików: `exercise.csv` i `calories.csv`.
- Połączono je po kolumnie `User_ID`.
- Usunięto zbędną kolumnę i sprawdzono typy danych oraz brakujące wartości.

### 2. Przygotowanie danych

- Przekonwertowano kolumny `Duration` i `Heart_Rate` do typu integer.
- Zapoznanie się z unikalnymi wartościami w kolumnie `Gender`.
- Przy pomocy mapy cieplnej zidentyfikowano, że najistotniejsze cechy to:
  - czas trwania treningu (`Duration`),
  - tętno (`Heart_Rate`),
  - temperatura ciała (`Body_Temp`).
- Wykresy rozrzutu wykazały różnice pomiędzy płciami.

### 3. Usuwanie wartości odstających oraz rozdział danych względem płci

- Przy pomocy wykresów pudełkowych wykryto i usunięto wartości odstające w temperaturze ciała (rekordy zawierające wartości poniżej 38.5°C).
- Wybrano cechy oraz wartość docelową wartość przewidywaną.
- Dane rozdzielono na dwie tabele ze względu na płeć i zapisano do oddzielnych plików `.csv`.

### 4. Budowa i trenowanie modeli

- Dane podzielono na zmienne niezależne (`Duration`, `Heart_Rate`, `Body_Temp`) i zmienną zależną (`Calories`) dla każdej płci.
- Dane podzielono na zbiory treningowe i testowe w proporcji 70/30.
- Wytrenowano dwa modele regresji liniowej (dla kobiet i mężczyzn).

### 5. Ocena modeli

- Zbadano współczynniki regresji. 
|                      | Females linear coefficient | Males linear coefficient |
|----------------------|----------------------------|---------------------------|
| Duration         | 6.34                   | 6.73                  |
| Heart_Rate      | 1.75                   | 2.41                  |
| Body_Temp        | -14.15                 | -18.27               |

- Zbadano metryki MAE oraz R².

| Płeć       | Kobiety     | Mężczyźni      |
|------------|---------|---------|
| MAE    | 6.73    | 14.66    |
| R²  | 0.98   | 0.91    |

- Zbadano rozrzuty oraz histogramy reszt.

### 6. Zapis i wdrożenie modelu

- Modele zapisano w formacie `.pkl` przy pomocy `joblib`.
- Wczytano je do aplikacji Streamlit, która pozwala użytkownikowi przewidzieć spalane kalorie na podstawie danych wejściowych.
- Stworzono prosty interfejs umożliwiający użytkownikowi wpisywanie danych.
- W aplikacji nałożono ograniczenia minimalnych wartości wejściowych, by uniknąć błędów lub ujemnych predykcji.

## Wnioski

- Czas treningu miał największy wpływ na ilość spalonych kalorii.
- Model dla kobiet osiągnął lepszą dokładność z powodu mniejszego rozrzutu danych (w odniesieniu do wykorzystanego zestawu danych).
- Wyniki różnią się od realnych ze względu na charakter badanego zjawiska (brak informacji na temat wytrenowania oraz masy mięśniowej badanych).
- Rozrzut reszt układa się w kształt litery U pokazując nieliniowość w danych. Przy dolnych i wysokich wartościach wejściowych model niedoszacowuje wyników.
- Histogram reszt odbiega od normalnego wskazując na większą zmienność błędów.
- Ze względu na specyfikę wykorzystanych danych konieczne było ustalenie dolnych ograniczeń wprowadzanych przez użytkownika wartości w celu zniwelowania możliwości uzyskania ujemnych wyników w aplikacji.

## Możliwe usprawnienia

- Zastosowanie bardziej precyzyjnego modelu regresyjnego, który radzi sobie lepiej z nieliniowościami.
- Zastosowanie walidacji krzyżowej.