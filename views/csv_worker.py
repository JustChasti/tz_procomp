# python system libs
# external libs
from fastapi import APIRouter, UploadFile, Depends
from fastapi.responses import JSONResponse
# project import
from models.csv_import import CsvFile
from models.user_models import UserAuthModel


csv_worker_router = APIRouter()


@csv_worker_router.post('/add-task', response_class=JSONResponse)
async def add_new_task(file: UploadFile, user: UserAuthModel = Depends()):
    print(user.acess_token)
    print(user.user_id)
    csv_file = CsvFile(file, user)
    return {'success': True, 'info': f'file id {csv_file.id}'}
