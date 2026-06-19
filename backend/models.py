from pydantic import BaseModel

class ResumeRequest(BaseModel):
    name: str
    education: str
    skills: str
    projects: str