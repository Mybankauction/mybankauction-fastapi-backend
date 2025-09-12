from urllib import request
from typing import Optional
from fastapi import APIRouter
from fastapi.params import Query
from starlette.responses import JSONResponse
from controller.property_controller import get_properties,filter_properties

property_router = APIRouter()


@property_router.get('/properties')
async def get_property(page:int=Query(1,ge=1)):
    result = await get_properties(page=page)
    return JSONResponse(result)

@property_router.get('/filtered.properties')
async def get_filtered_property(
    auction_id: Optional[str] = Query(default=None),
    state: str = Query(default="Karnataka"),
    city: Optional[str] = Query(default=None),
    area: Optional[str] = Query(default=None),
    property_type: Optional[str] = Query(default=None),
    auction_start_date: Optional[str] = Query(default=None),
    auction_end_date: Optional[str] = Query(default=None),
    min_price: Optional[int] = Query(default=None),
    max_price: Optional[int] = Query(default=None),
    page: Optional[int] = Query(default=1),
):
    filters = {"auction_id":auction_id,"state":state,"city":city,"area":area,"property_type":property_type,"auction_start_date":auction_start_date,"auction_end_date":auction_end_date,"min_price":min_price,"max_price":max_price}

    result  = await filter_properties(filters,page)
    return JSONResponse(content=result)