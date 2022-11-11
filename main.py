import typing as t
from dataclasses import dataclass


@dataclass(frozen = True)
class ZusSession:
    username: str
    password: str


def authenticate(username: str, password: str) -> t.Optional[ZusSession]:
    if username == 'niedzwiedz' and password == 'niedzwiedz123':
        return ZusSession(username, password)
    return None


def main():
    username = input('username:')
    password = input('password:')
    session = authenticate(username, password)
    if session is None:
        raise Exception('Wrong credentials')
    print(session)


if __name__ == '__main__':
    main()