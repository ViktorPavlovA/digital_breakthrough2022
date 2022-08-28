# Код решения кейса Ростелеком

**Решение представленно командой "Цикличность действий"**

## "Разработка модели машинного обучения для предсказания склонности клиента к покупке услуги на основе предоставленных и открытых данных"

0. [model](#model)
1. [Preprocessing_script](#Preprocessing_script)
2. [Parsing_script](#Parsing_script)
3. [Info](#info)
4. [Pred](#Pred) 
5. [Person](#Person)

**>model**

В данной папке находится скрипт (xgboost_nn.ipynb) для обучения ансамбля моделей машинного обучения, а также ее параметры.

1. XGboost
2. Простая модель нейронных сетей
3. Кластеризация на основе K-means

**>Preprocessing_script**

В данной папке находятся скрипты для предварительной обработки данных и получения новых фич

Основная идея была:
1. Создать таблицу hex_grace для гексагонов на основе тренировочной таблицы
2. Выполнить джойн с таблицей теста для подстановки данных из таблицы hex_grace
3. Выделение новых фич с использование K-means

**>Parsing_script**

В папке находятся скрипты для парсинга сайтов

**>Pred**

Топ предсказанных 1 и 0.

Так же для удобства находится в корне - "Цикличность действий.csv"



**>info**

В папке графики и диаграммы, которые дают представление о модели 

**>Person**

Информация об участниках: 


Анастасия Тимошина <anastasiia.41297@gmail.com>

Богдан Барабанщиков <boltik1993@gmail.com>

Павлов Виктор <viktor.pavlov.1998@list.ru> (https://github.com/ViktorPavlovA)


















