hello = """
В этом боте ты можешь пользоваться ChatGPT и не только бесплатно и без лимита
/new - начать новый диалог
"""
promt = """
Ипспользуй Markdown форматирование: *Жирный текст*, _Текст курсивом_,  __Подчеркнутый текст__, ```
Большой фрагмент кода/code>
```, [Гиперссылка](https://www.example.com/). Отвечай на русском языке, не используй MAthJax
"""
promt_gemini = """
Не используй никакое форматирование, отвечай на русском языке. Также не используй MathJax
"""
changelog = """
История обновлений:
 <b>0.1</b>
 - Сделана основа бота

 <b>0.2</b>
 - Добавлен редактор фото
 - Возврат ChatGPT Search
 - Незначительные исправления

<b>0.3</b>
 - Добавлена Gemini 2.5 со стримингом ответа
 - Изменены кнопки
 - Исправления ошибок, связанных с редактором

<a href="https://github.com/swtomas/chatgptbot">Подробнее на GitHub</a> 
"""