from DataBaseApi.DB.repositories.stop_work_repositories import StopWorkRepository
from DataBaseApi.DB.schemas.stop_work_schemas import StopWorkAddSchema, StopWorkGetResponse, StopWorkPostResponse, \
    StopWorkAddManySchema, StopWorkPostManyResponse, StopWorkPutResponse, StopWorkUpdateSchema, StopWorkGetSchema
from DataBaseApi.DB.services.stop_work_service import StopWorkService
from DataBaseApi.DB.utils.UnitOfWork import UnitOfWork
from DataBaseApi.DB.DB_manager import async_session_maker
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=['BasicUrls'])


@router.get("/stop_work/", response_model=StopWorkGetResponse)
async def get_all():
    async with UnitOfWork(async_session_maker) as uow:
        response_by_db = await StopWorkService(StopWorkRepository(uow.session)).get_all()

    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': response_by_db}
    return {'response_by_db': False}


@router.post("/stop_work/get_many", response_model=StopWorkGetResponse)
async def get_all(filters: StopWorkGetSchema | None):
    async with UnitOfWork(async_session_maker) as uow:
        response_by_db = await StopWorkService(StopWorkRepository(uow.session)).find_many(filters)

    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': response_by_db}
    return {'response_by_db': False}


@router.post("/stop_work/", response_model=StopWorkPostResponse)
async def add_one(user_data: StopWorkAddSchema):
    async with UnitOfWork(async_session_maker) as uow:
        response_by_db = await StopWorkService(StopWorkRepository(uow.session)).add_one(user_data)
        await uow.commit()

    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': response_by_db.id}
    return {'response_by_db': False}


@router.post("/stop_work/add_many", response_model=StopWorkPostManyResponse)
async def add_many(user_data: StopWorkAddManySchema):
    async with UnitOfWork(async_session_maker) as uow:
        response_by_db = await StopWorkService(StopWorkRepository(uow.session)).add_many(user_data)
        await uow.commit()

    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': [obj.id for obj in response_by_db]}
    return {'response_by_db': False}


@router.put("/stop_work/", response_model=StopWorkPutResponse)
async def update(user_data: StopWorkUpdateSchema):
    async with UnitOfWork(async_session_maker) as uow:
        response_by_db = await StopWorkService(StopWorkRepository(uow.session)).update(user_data)
        await uow.commit()

    if response_by_db is False:
        raise HTTPException(status_code=500, detail="Database error")
    if response_by_db:
        return {'response_by_db': {"object id": [obj[0] for obj in response_by_db]}}
    return {'response_by_db': False}

