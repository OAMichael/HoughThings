## Программы, связанные с преобразованием Хафа

#### Программа `HT.py` выполняет преобразование Хафа данной картинки, используя билбиотеку cv2 (OpenCV), и выводит два изображения: изначальное и на котором найдены прямые линии.
Принимает на вход в качестве argv[1] путь к изображению, на котором нужно найти прямые.

#### Программа `FHT.py` является собственной реализацией быстрого преобразования Хафа. Для сравнения, обычное работает за O(n^3), а быстрое - за O(n^2 log(n)). Выводит изначальную картинку, картину Хафа-образа и изначальное изображение, на котором зафиксированы прямые.
Принимает на вход в качестве argv[1] путь к изображению, быстрое преобразование Хафа которого нужно сделать. Изображение должно быть квадратного 2^k * 2^k размера.

#### Программа `DyadicPatterns.py` строит на белом изображении черный диадический паттерн - приближение геометрической прямой, задаваемое рекурсивно.
Принимает на вход через `input()` значения k и t. Это - целочисленные значения размера изображения (2^k) в пикселях и значение наклона прямой соответственно. Можно ввести в качестве параметра командной строки флаг `-l`, `-L` или `--large`, чтобы изображение получилось увеличенным в 8 раз, чтобы видеть каждый "новый пиксель" лучше (теперь это квадрат 8 * 8 пикселей).