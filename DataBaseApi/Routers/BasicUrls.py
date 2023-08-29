from DataBaseApi.schemes.schemes_BasicUrls import TableName, RequestGet, ResponseGet, RequestSet, ResponseSet
from DataBaseApi.schemes.schemes_BasicUrls import RequestUpdate, ResponseUpdate, RequestSetMany, ResponseSetMany
from DataBaseApi.DB.DB_manager import DB_connector
from fastapi import APIRouter, HTTPException


router = APIRouter(tags=['BasicUrls'])


@router.post("/get/{name_table}", response_model=ResponseGet)
async def basic_get(name_table: TableName, get_dict: RequestGet):
    get_dict_for_db = dict(get_dict)
    name_tabl = name_table.value

    response_by_db = DB_connector.get(name_table=name_tabl, **get_dict_for_db )
    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': response_by_db}
    return {'response_by_db': False}


@router.post("/set/{name_table}", response_model=ResponseSet)
async def basic_set(name_table: TableName, post_dict: RequestSet):
    set_dict_for_db = dict(post_dict)
    name_tabl = name_table.value

    response_by_db = DB_connector.set(name_table=name_tabl, **set_dict_for_db )
    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': response_by_db}
    return {'response_by_db': False}


@router.post("/set_many/{name_table}", response_model=ResponseSetMany)
async def basic_set_many(name_table: TableName, set_many_list: RequestSetMany):
    set_many_dict_for_db = dict(set_many_list)
    name_tabl = name_table.value

    response_by_db = DB_connector.set(name_table=name_tabl, **set_many_dict_for_db )
    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': response_by_db}
    return {'response_by_db': False}


@router.post("/update/{name_table}", response_model=ResponseUpdate)
async def basic_update(name_table: TableName, put_dict: RequestUpdate):
    put_dict_for_db = dict(put_dict)
    name_tabl = name_table.value

    response_by_db = DB_connector.update(name_table=name_tabl, **put_dict_for_db )
    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': response_by_db}
    return {'response_by_db': False}







