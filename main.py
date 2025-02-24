from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from backend.models import SessionLocal, Song  # Import SQLAlchemy setup & model
from fastapi.middleware.cors import CORSMiddleware
from backend.models import init_db  # Import your database initialization function

app = FastAPI()

#CORS - frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")  # This adds a homepage route
def read_root():
    return {"message": "Hello, NashMash!"}

@app.get("/search")
def search_songs(q: str = Query(..., min_length=1, title="Search Query") , db: Session = Depends(get_db)):
    res = db.query(Song).filter(Song.title.ilike(f"%{q}%")).limit(10).all()
    print(res)
    return [
        {
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
            "bpm_low": song.bpm_low,
            "bpm_high": song.bpm_high,
            "key": song.key
        }
        for song in res
    ]


