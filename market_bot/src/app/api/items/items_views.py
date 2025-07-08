from typing import Annotated

from fastapi import Path, APIRouter


router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@router.get("/latest/")
def get_latest_item():
    return {"Item": {"id": 0, "title": "latest"}}


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "Item": {
            "id": item_id,
        }
    }
