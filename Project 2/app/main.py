from fastapi import FastAPI, HTTPException
import json
import random

app = FastAPI()

# Load personas
with open("app/personas.json") as f:
    personas = json.load(f)

@app.get("/")
def root():
    return {"message": "Persona Feedback App is running"}

@app.get("/personas")
def get_personas():
    return personas

@app.get("/feedback/{persona_id}")
def get_feedback(persona_id: int):
    if persona_id >= len(personas):
        raise HTTPException(status_code=404, detail="Persona not found")
    persona = personas[persona_id]
    # Simulate feedback generation
    feedback = f"{persona['name']} says: '{random.choice(persona['opinions'])}'"
    return {"feedback": feedback}
