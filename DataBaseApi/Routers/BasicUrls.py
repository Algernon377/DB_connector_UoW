from DataBaseApi.DB.repositories.stop_work_repositories import StopWorkRepository
from DataBaseApi.DB.repositories.users_repositories import UsersRepository
from DataBaseApi.DB.schemas.stop_work_schemas import StopWorkAddSchema
from DataBaseApi.DB.schemas.users_schemas import UsersSchema, UsersAddSchema
from DataBaseApi.DB.services.stop_work_service import StopWorkService
from DataBaseApi.DB.services.users_service import UsersService
from DataBaseApi.DB.utils.UnitOfWork import UnitOfWork
from DataBaseApi.schemas.schemas_BasicUrls import TableName, RequestGet, ResponseGet, RequestSet, ResponseSet
from DataBaseApi.schemas.schemas_BasicUrls import RequestUpdate, ResponseUpdate, RequestSetMany, ResponseSetMany
from DataBaseApi.DB.DB_manager import DB_connector, async_session_maker
from fastapi import APIRouter, HTTPException


router = APIRouter(tags=['BasicUrls'])

@router.get("/get_all/", response_model=ResponseGet)
async def basic_get():
    response_by_db = await StopWorkService(StopWorkRepository).get()
    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': response_by_db}
    return {'response_by_db': False}


@router.post("/add_one/", response_model=ResponseGet)
async def basic_get(user_data: StopWorkAddSchema):
    async with UnitOfWork(async_session_maker) as uow:
        response_by_db = await StopWorkService(StopWorkRepository(uow.session)).add(user_data)
        await uow.commit()
    # response_by_db = await StopWorkService(StopWorkRepository).add(user_data)
    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': [(response_by_db,)]}
    return {'response_by_db': False}


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







