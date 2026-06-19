from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import ResumeRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }

@app.post("/generate-resume")
def generate_resume(data: ResumeRequest):
    resume = f"""
Name: {data.name}

Education:
{data.education}

Skills:
{data.skills}

Projects:
{data.projects}
"""
    return {
        "resume": resume
    }
