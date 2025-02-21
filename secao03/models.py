from typing import Optional, List
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O titulo deve ter pelo menos 3 palavras!')
        
        if value.islower():
            raise ValueError('O titulo deve ser capitalizado!')
        return value

cursos: List[Curso] = [
    Curso(id=1, titulo='Programação para leigos', aulas=42, horas=50),
    Curso(id=1, titulo='Algoritmos e logica de programação', aulas=72, horas=150)
]
