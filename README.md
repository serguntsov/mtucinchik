# [mtucinchik - телеграмм бот для знакомств](https://t.me/mtucinchik)
- Перед запуском рекомендуется установить файл с зависимостями:
```Bash
    pip install -r requirements.txt
```

- Встаьте токен вашего телеграм бота
```Python
    bot = telebot.TeleBot("YOUR TOKEN")
```

- Измените обязательную подписку на ваш канал.<br/>
Вам необходимо найти в коде `-1001720626187` и заменить на id своего канала.<br/>
Чтобы узнать id своего канала перешлите любое сообщение из канала боту [getmyid_bot](https://t.me/getmyid_bot)<br/>
По аналогии замените `https://t.me/mtucinchik` на ссылку своего канала.

## Кратко о работе с ботом
После отправки `/start` бот требует от вас подписки на канал. После оформления подписки, вы можете зарегистрировать свою анкету.
Если, посмотрев свою анкету, вы заметили ошибку, отправив `/start` вы можете зарегистрироваться заново или изменить некоторые данные о себе.<br/>
У админов есть доступ к меню `/admin` чтобы стать админом в боте, нужно быть создателем или админом канала. Пока что в админ панеле есть только рассылка (сообщение / картинка / картинка + текст)

- Оценка анкет<br/>
Вы поставили лайк понравившейся анкете, создателю данной анкеты придет сообщение, что его/её оценили. Если при повторном оценивании вы получите сообщение:
```Python
    'Вы ранее ставили лайк данной анкете. Пока не получили обратного ответа от пользователя! Ожидайте!'
```
то стоит подождать. После взаимной оценки оба пользователя получают сообщение с анкетой и @username пользователя (если у пользователя отсутствует @username, то перейти к нему в профиль будет невозможно)<br/>
Бот в зависимости от своей популярности будет дорабатываться, добавится функция остановки оценки вашей анкеты, телеграм-бот с чатом для общения/знакомства. Дополнится админ панель, добавится функция остановки кода и еще что-то...