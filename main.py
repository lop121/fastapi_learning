from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Movies CRUD Demo")

app.add_middleware(CORSMiddleware, allow_origins=["*"])


class Movie(BaseModel):
    name: str
    year: int


movies: List[Movie] = []


@app.post("/movies", response_model=Movie)
def create_movie(movie: Movie):
    movies.append(movie)
    return movie


@app.get("/movies", response_model=List[Movie])
def get_movies():
    return movies


@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    if movie_id < 0 or movie_id >= len(movies):
        raise HTTPException(status_code=404, detail="Movie not found")
    return movies[movie_id]


@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, updated_movie: Movie):
    if movie_id < 0 or movie_id >= len(movies):
        raise HTTPException(status_code=404, detail="Movie not found")
    movies[movie_id] = updated_movie
    return updated_movie


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    if movie_id < 0 or movie_id >= len(movies):
        raise HTTPException(status_code=404, detail="Movie not found")
    deleted = movies.pop(movie_id)
    return {"message": "Movie deleted", "deleted_movie": deleted}
