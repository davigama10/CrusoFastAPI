from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Response
from typing import Dict, List, Optional, Any
from fastapi import Path, Query, Header, Depends

from time import sleep

from models import Curso, cursos


def fake_db():
    try:
        print('Abrindo conexão com o banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com o banco de dados...')
        sleep(1)


app = FastAPI(
    title='API de cursos da geek university!!',
    version='0.0.1',
    description='Uma API para estudo do FastAPI!'
    )





@app.get('/cursos', 
        description='Rota que retorna todos os cursos cadastrados',
        summary='retorna todos os cursos',
        response_model=List[Curso],
        response_description='Cursos encontrados com sucesso!')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(title='ID do curso', description='Deve ser um valor entre 1 e 2', gt=0, lt=3), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado.")


@app.post('/cursos', status_code=status.HTTP_201_CREATED,
          response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com esse id {curso_id}.')


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com esse id {curso_id}.')
    

@app.get('/calculadora')
async def calcular(a: int = Query(gt=10), b: int = Query(default=None), c: Optional[int] = None, x_geek: str = Header(default=None)):
    soma = a + b
    if c:
        soma += c

    print(f'X-GEEK: {x_geek}')
    return soma

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)