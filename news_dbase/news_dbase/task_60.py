# Доработайте своё новостное приложение:
#
# Сделайте новую страничку с адресом /news/, на которой должен выводиться список всех новостей.
# Сделайте отдельную страничку для конкретной новости по адресу /news/<id новости>.
# Все странички должны быть частью основного шаблона default.html.

# Измените внешний вид страницы /news/:
#
# Выводите новости в следующем виде — заголовок, дата публикации в формате день.месяц.год, затем первые 20 слов текста статьи. Можно вывести как списком, так и таблицей. Новости должны выводиться в порядке от более свежей к старой.
# Сверху страницы должно быть выведено количество всех новостей (используется фильтр news|length).
# По ссылке /news/<id новости> должна выводиться детальная информация о новости.
# Заголовок, дата публикации в формате день.месяц.год и полный текст статьи.


#
# Иногда в новостях попадаются такие страсти, что диву даёшься. Некоторые фразы поражают воображение. Чтобы вдруг случайно не шокировать читателей вашего портала, забыв вырезать какие-то неприятные высказывания, напишите фильтр, который будет убирать всю нецензурную брань в содержании и названии статей. После этого примените его в шаблоне.
# Так как это учебный проект, сделаем допущение, что все слова, которые нужно цензурировать, начинаются с верхнего или нижнего регистра. Остальные буквы слов могут быть только в нижнем регистре.
# Например, если мы считаем слово «редиска» ругательством, то из предложения «Нехороший человек — редиска!» после применения фильтра должно получиться «Нехороший человек — р******!»
# Дополнительно попробуйте сделать проверку, чтобы фильтр цензурирования применялся только к переменным строкового типа. Иными словами, если фильтр применяется не к строке, разработчик получает ошибку.
# В ходе работы с модулем вы должны были выполнить следующие задания:
#
#
#
# Создать новую страницу с адресом /news/, на которой должен выводиться список всех новостей.
# Вывести все статьи в виде заголовка, даты публикации и первых 20 символов текста.
# Новости должны выводиться в порядке от более свежей к самой старой.
# Сделать отдельную страницу для полной информации о статье /news/<id новости>.
# На этой странице должна быть вся информация о статье. Название, текст и дата загрузки в формате день.месяц.год.
#
# Написать собственный фильтр censor, который заменяет буквы нежелательных слов в заголовках и текстах статей на символ «*».
#
# Все новые страницы должны использовать шаблон default.html как основу.
#
