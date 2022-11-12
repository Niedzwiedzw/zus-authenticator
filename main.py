import typing as t
from dataclasses import dataclass
import json


@dataclass(frozen = True)
class ZusSession:
    username: str
    password: str

def authenticate(username: str, 
                 password: str, 
                 users:t.Dict[str, str]) -> t.Optional[ZusSession]:
    if users.get(username) is not None and users.get(username) == password:
        return ZusSession(username, password)
    return None

def load_users(path:str) -> t.Dict[str, str]:
    with open(path, "r") as f:
        return json.load(f)


def main():
    username = input('username:')
    password = input('password:')
    users = load_users("./accounts.json")
    session = authenticate(username, password, users)
    if session is None:
        raise Exception('Wrong credentials')
    print(session)


if __name__ == '__main__':
    main()