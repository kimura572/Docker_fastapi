from fastapi import APIRouter


from api.routers import task, done

router = APIRouter()




@router.put("tasks/{task_id}/done", response_model=None)
async def mark_task_as_done(task_id: int):
  return


@router.delete("tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int):
  return