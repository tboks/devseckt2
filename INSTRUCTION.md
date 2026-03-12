1. Создайте репозиторий на GitHub
2. Склонируйте его на компьютер
3. Скопируйте все файлы из шаблона
4. Сделайте commit и push
```bash```
git add .
git commit -m "feat: initial commit with CI/CD template"
git push origin main



Настройка секретов

Перейдите в Settings → Secrets and variables → Actions и добавьте:
-"DOCKERHUB_USERNAME" - Ваш логин Docker Hub
-"DOCKERHUB_TOKEN" - hub.docker.com → Security
-"TELEGRAM_CHAT_ID" - ID канала (см. ниже)
-"TELEGRAM_TOKEN" - @BotFather в Telegram

Как получить TELEGRAM_CHAT_ID:
1.Откройте @BotFather, создайте бота: /newbot
2.Создайте канал, добавьте бота как администратора
3.Отправьте сообщение в канал
4.Откройте: https://api.telegram.org/bot<ТОКЕН>/getUpdates
5.Найдите "chat":{"id":-123456789



Тестирование пайплайна

1.Создайте ветку:
```bash```
git checkout -b feature/test-feature

2.Внесите изменения в код

3.Сделайте commit

Создайте Pull Request на GitHub
Смотрите вкладку Actions
