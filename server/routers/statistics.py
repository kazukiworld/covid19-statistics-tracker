from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
import httpx

router = APIRouter()


class Country(BaseModel):
    country: str


@router.get("/api/covid-statistics")
async def covid_statistics():
    url = "https://covid-19.dataflowkit.com/v1"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # raises an exception for non-2xx responses
    except httpx.HTTPStatusError as err:
        raise HTTPException(status_code=400, detail="Bad request") from err
    except httpx.RequestError as err:
        raise HTTPException(status_code=500, detail="Server error") from err

    return response.json()
