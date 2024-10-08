Добрый день, прикрепляю тестовое задание.


Техническое задание для позиции бэкенд разработчика Python (FastAPI)

### Цель:
Создать веб-сервис на основе FastAPI, который включает в себя функциональность для генерации и обработки UUID, а также интеграцию с RabbitMQ для обработки сообщений. Код должен быть покрыт тестами и обернут в Docker.

### Задачи:
1. Реализовать GET эндпоинт /generate-uuid, который генерирует и возвращает случайный UUID.
2. Реализовать проверку заголовков в запросе с использованием зависимости (Depends):
    - Если в заголовке присутствует "зеленый флаг" (X-Flag: green), то выводить в логи сгенерированный UUID и информацию о зеленом флаге.
    - Если в заголовке присутствует "красный флаг" (X-Flag: red), то отправлять информацию об этом UUID и красном флаге в RabbitMQ.
3. Реализовать консумера RabbitMQ, который будет читать сообщения из очереди и, если получает красный флаг, выводить этот флаг в логи.
4. Покрыть весь функционал тестами.
5. Обернуть приложение в Docker.

### Подробное описание задач:

#### 1. Реализация эндпоинта /generate-uuid
- Эндпоинт должен генерировать случайный UUID.
- Возвращать UUID в формате JSON.

#### 2. Проверка заголовков с использованием зависимости (Depends)
- Если header запроса к ендпоинту содержит "зеленый флаг" (X-Flag: green):
  - Логировать UUID и информацию о зеленом флаге.
- Если header содержит "красный флаг" (X-Flag: red):
  - Отправлять UUID и информацию о красном флаге в RabbitMQ.

#### 3. Реализация RabbitMQ
- Продюсер и консумер должны быть реализованы в том же приложении. 
- Продюсер должен отправлять сообщения в очередь RabbitMQ, если оно содержит “красный флаг”. 
- Консумер должен считывать сообщения из очереди RabbitMQ.
- Если сообщение содержит "красный флаг", логировать эту информацию.

#### 4. Тестирование
- Покрыть тестами функциональность генерации UUID.
- Покрыть тестами обработку заголовков.

#### 5. Docker
- Создать Dockerfile для приложения.
- Настроить Docker Compose для поднятия сервиса FastAPI и RabbitMQ.

### Ожидаемый результат:
- Репозиторий с исходным кодом приложения.
- Dockerfile и docker-compose.yml для развертывания приложения.
- Документация по запуску и тестированию приложения.

Дедлайн 9:00 22.07.24