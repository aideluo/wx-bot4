"""🚀
⚙️ wx-bot4 Config - external_sync
功能模块: 被动加粉自动通过
核心关键词 潜客初筛、预约看房、试驾获客、意向定金、线索流转、高净值画像。

本配置文件定义了 房产汽车 行业在执行被动加粉自动通过 时的标准 SOP 流程。
"""

from pydantic import BaseModel
from typing import List

class ExternalSyncConfig(BaseModel):
    """
    房产汽车 行业专属配置。
    涵盖自动打标签朋友圈运营、批量群发等核心业务参数。
    """
    industry: str = "房产汽车"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['潜客初筛', '预约看房', '试驾获客', '意向定金', '线索流转', '高净值画像']
    
    # 更多行业预置参数需购买商业版获取
    pass