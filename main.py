from fastapi import FastAPI

server = FastAPI()

cursos = {
    1: {
        'nome': 'Dev Full-Stack',
        'aulas': 48,
        'horas': '144 horas'
    },
    2: {
        'nome': 'Data Science',
        'aulas': 42,
        'horas': '132 horas'
    }
}

@server.get('/')
async def hello():
    '''Meu primeiro endpoint'''
    return 'Rodando servidor diretamente pelo arquivo'

@server.get('/cursos')
async def listar_cursos():
    '''Lista os cursos da Infinity'''
    return cursos

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(
        'main:server', 
        host='0.0.0.0',
        port=7000,
        reload=True
    )

