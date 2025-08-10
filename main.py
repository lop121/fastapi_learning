from fastapi import FastAPI, BackgroundTasks
import time
import asyncio

app = FastAPI()


def sync_task():
    time.sleep(3)
    print("Отправлен email")


async def async_task():
    await asyncio.sleep(3)
    print("Сделан запрос в сторонний API")


@app.post("/")
async def some_route(bg_tasks: BackgroundTasks):
    # asyncio.create_task(async_task())
    bg_tasks.add_task(sync_task)
    return {"access": True}
