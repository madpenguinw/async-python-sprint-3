
# Numerical values:
PORT: int = 8000
HOST: str = '127.0.0.1'
MAXLENGTH: int = 20

# Commands:
PRIVATE: str = '@'
DISCONNECT: str = '/disconnect'
REGISTRATION: str = '/register'
AUTHORIZATION: str = '/authorize'
CREATE: str = '/create '
JOIN: str = '/join '
CHAT: str = '/chat '
CHATS: str = '/chats'
YES: str = '/yes'
NO: str = '/no'

# Text
GREETING: str = (
    '\n<Добро пожаловать на сервер!> \n'
    f'<Введите "{REGISTRATION}" для регистрации или '
    f'"{AUTHORIZATION}" для авторизации> \n'
)

RULES: str = (
    '<Правила:>'
    '<1 - Введите сообщение и оно отправится в общий чат> \n'
    '<2 - Чтобы отправить личное сообщение, напишите '
    f'"{PRIVATE}имя_пользователя" и через пробел введите свое сообщение> \n'
    f'<3 - Чтобы создать чат, введите "{CREATE} <название_чата>"> \n'
    f'<4 - Чтобы запросить доступ к чату, введите "{JOIN} <название_чата>"> \n'
    f'<5 - Чтобы подключиться к нему, введите "{CHAT} <название_чата>"> \n'
    f'<6 - Чтобы узнать список своих чатов, введите "{CHATS}"> \n'
    f'<7 - Чтобы отключиться от сервера введите "{DISCONNECT}"> \n'
)

WRONG_COMMAND: str = '\n<Введена неверная команда>  \n'
RETRY: str = '<Повторите попытку> \n'

USERNAME: str = '\n<Пользователь с ником '
NOT_REGISTERED: str = ' не зарегистрирован на сервере>'

LOGIN: str = '\n<Введите свой логин>'
PASSWORD: str = '\n<Введите свой пароль>'
SUCCESSFULLY_REGISTERED: str = '\n<Вы были успешно зарегестрированы> \n'
SUCCESSFULLY_AUTHORIZED: str = '\n<Вы были успешно авторизованы> \n'

AUTHORIZATION_FAILED: str = (
    '\n<Данные введены неверно> \n'
    f'<Введите "{REGISTRATION}", чтобы зарегестрироваться> \n'
    '<Или введите любое другое значение, чтобы повторить попытку> \n'
)

REGISTRATION_FAILED: str = (
    '\n<Пользователь с таким именем уже зарегистрирован> \n'
    f'<Введите "{AUTHORIZATION}", чтобы зарегестрироваться> \n'
    '<Или введите любое другое значение, чтобы повторить попытку> \n'
)

EMPTY_HISTORY: str = '\n<История чата пуста> \n'
HISTORY: str = '\n<История чата загружена> \n\n'

REGISTERED: str = '\n<Регистрация прошла успешно> \n'
AUTHORIZED: str = '\n<Регистрация прошла успешно> \n'
PASSWORED_CHANGED: str = '\n<Пароль успешно изменен> \n'

ME: str = 'Я'

CHAT_EXIST: str = (
    '\n<Чат с данным названием уже существует>\n'
    '<Вы можете: \n>'
    f'<1 - запросить к нему доступ, введя "{JOIN} <название_чата>"> \n'
    f'<2 - подключиться к нему, введя "{CHAT} <название_чата>"> \n'
    f'<3 - узнать список своих чатов, введя "{CHATS}"> \n'
    '<4 - Ввести любое другое сообщения. Оно отправится в общий чат> \n'
)

CHAT_CREATED: str = '<Чат был успешно создан>'

ALREADY_IN_CHAT: str = '<Вы уже состоите в этом чате>'

CHAT_NOT_EXIST: str = '<Данный чат не существует>'

ADD_TO_CHAT: str = f'<Введите "{YES}" или "{NO}", чтобы ' \
    'разрешить/запретить добавление пользователя в чат> \n'

ADMIN_OFFLINE: str = '<Администратор чата сейчас оффлайн ' \
    'и не может принять запрос на добавление>'

ADDED_TO_CHAT: str = '<Вы были успешно добавлены в чат>'

JOIN_REFUSED: str = '<Вам было отказано в присоединении к чату>'
