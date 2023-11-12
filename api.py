from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import users, posts


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("event", "startup")
#     from utils.database.db import init_db
#     app.state.db = await init_db()
#     yield
#     print("event", "shutdown")
#     app.state.db.client.close()
#     print("[+] Closed to database successfully.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("event", "startup")
    from utils.database.db import init_db
    await init_db()
    yield


def create_app(lifespan=lifespan) -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    return app


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", reload=True)

app = create_app()

app.include_router(users.router)
app.include_router(posts.router)


@app.get('/')
def read_route():
    return {"msg": "Hello world"}
