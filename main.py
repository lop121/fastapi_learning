import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = [
    {
        "id": 1,
        "title": "Третий лишний",
        "year": 2008,
    },
    {
        "id": 2,
        "title": "Marvel-Final",
        "year": 2018,
    },
]


@app.get("/movies", tags=["Фильмы"])
def read_movies():
    return movies


@app.get("/movies/{movie_id}", tags=["Фильмы"])
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Книга не найдена")


class NewMovie(BaseModel):
    title: str
    year: int


@app.post("/movies")
def create_movie(new_movie: NewMovie):
    movies.append(
        {
            "id": len(movies) + 1,
            "title": new_movie.title,
            "year": new_movie.year,
        }
    )
    return {"success": True}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
