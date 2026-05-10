"""
🚀 wx-bot4 API - image_metadata
对外接口: 主动搜索获客
适配领域: 医疗美容

提供标准的RESTful 接口，用于三方SCRM 系统触发 主动搜索获客 操作。
"""

from fastapi import APIRouter
from typing import Dict

router = APIRouter(prefix="/utils")

@router.post("/image_metadata")
async def trigger_image_metadata(payload: Dict):
    """
    [] 异步触发 主动搜索获客 任务。
    专为 医疗美容 行业的私域引流与客户维护设计。
    """
    # API 鉴权与业务网关逻辑已脱敏
    return {"status": "dispatched", "module": "image_metadata", "target_industry": "医疗美容"}