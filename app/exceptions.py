from fastapi import HTTPException, status


IncorrectEmailOrPswException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверные данные, повторите ещё раз"
)

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует"
)

TokenExpireException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Текущий токен истёк"
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Текущий токен истёк"
)

IncorrectTokenFormatExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Некорректный формат токена"
)

UserNotPresentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED
)

RoleAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Роль c таким названием уже существует"
)