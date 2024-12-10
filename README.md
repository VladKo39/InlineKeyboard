# Домашнее задание по теме "Инлайн клавиатуры".
______________
## Цель:
научится создавать *Inline* клавиатуры и кнопки на них в ***Telegram-bot***.

## Задача "Ещё больше выбора":
Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.

Создайте клавиатуру **`InlineKeyboardMarkup`** с 2 кнопками **`InlineKeyboardButton`**:
>1. С текстом **`'Рассчитать норму калорий'`** и callback_data='calories'
>2. С текстом **`'Формулы расчёта'`** и **`callback_data='formulas'`**

Создайте новую функцию **main_menu(message)**, которая:

>1. Будет обёрнута в декоратор ***`@message_handler`***, срабатывающий при передаче текста **`'Рассчитать'`**.
>2. Сама функция будет присылать ранее созданное **Inline** меню и текст **`'Выберите опцию:`**'

Создайте новую функцию **get_formulas(call)**, которая:

>1. Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
>2. Будет присылать сообщение с формулой Миффлина-Сан Жеора.

Измените функцию **set_age** и декоратор для неё:
>1. Декоратор смените на **`@callback_query_handler`**, который будет реагировать на текст **`'calories'`**.
Теперь функция принимает не **`message`**, а **`call`**. Доступ к сообщению будет следующим - **`call.message`**.

По итогу получится следующий алгоритм:

>1. Вводится команда **`/start`**
>2. На эту команду присылается обычное меню: **`'Рассчитать'`** и **`'Информация'`**.
>3. В ответ на кнопку **`'Рассчитать'`** присылается **Inline** меню: **`'Рассчитать норму калорий'`** и **`'Формулы расчёта'`**
>4. По **Inline** кнопке **`'Формулы расчёта'`** присылается сообщение с формулой.
>5. По **Inline** кнопке **`'Рассчитать норму калорий'`** начинает работать машина состояний по цепочке.

## Пример результата выполнения программы:
![image](https://github.com/user-attachments/assets/fe4ff0c0-f193-44f4-a304-b47829b55fe3)
![image](https://github.com/user-attachments/assets/36d2302d-72d9-4a8f-8c17-f938780661fd)

**Примечания:**
При отправке вашего кода на **GitHub** ***не забудьте убрать ключ*** для подключения к вашему боту!
**Файл module_13_6.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.**
