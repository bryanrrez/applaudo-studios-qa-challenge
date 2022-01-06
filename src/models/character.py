
from dataclasses import dataclass

@dataclass
class Character:
    char_id: int
    name: str
    birthday: str
    occupation: list
    img: str
    status: str
    nickname: str
    appearance: list
    portrayed: str
    category: str
    better_call_saul_appearance: list

    @classmethod
    def from_dict(cls, data):
        return cls(
            char_id=data['char_id'],
            name=data['name'],
            birthday=data['birthday'],
            occupation=data['occupation'],
            img=data['img'],
            status=data['status'],
            nickname=data['nickname'],
            appearance=data['appearance'],
            portrayed=data['portrayed'],
            category=data['category'],
            better_call_saul_appearance=data['better_call_saul_appearance']
        )