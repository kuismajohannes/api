from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from database.models import Player
from database.models import Event
from database.models import PlayerCreate
from database.database import players


app = FastAPI()

## Get Players
@app.get("/players")
async def get_players():
    return [{"id": player.id, "name": player.name} for player in players]

## Get Player
@app.get("/players/{id}")
async def get_player(id: int):
    player = next((p for p in players if p.id == id), None)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

## Get player Events
@app.get("/players/{id}/events")
async def get_player_events(id: int):
    player = next((p for p in players if p.id == id), None)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player.events

## Create Player
@app.post("/players")
async def create_player(player: PlayerCreate):
    # Set the player id
    player_id = len(players) + 1
    player_obj = Player(id=player_id, name=player.name)
    players.append(player_obj)
    return JSONResponse(content=player_obj.dict(), status_code=201)

## Add Event to Player
@app.post("/players/{id}/events", status_code=201)
async def add_event_to_player(id: int, event: Event):
    player = next((p for p in players if p.id == id), None)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    event.id = len(player.events) + 1
    player.events.append(event)
    return player

## Get all Events
@app.get("/events")
async def get_all_events():
    all_events = []
    for player in players:
        all_events.extend(player.events)
    return all_events
