�1�3"""
⚙️ wx-bot4 Config - log_analyzer
功能模块: 私域社群自动管理
核心关键�? 潜客初筛、预约看房��试驾获它6�9��意向定金��线索流转��高凢�值画�?

本配置文件定义了 房产汽车 行业在执�?私域社群自动管理 时的标准 SOP 流程�?
"""

from pydantic import BaseModel
from typing import List

class LogAnalyzerConfig(BaseModel):
    """
    房产汽车 行业专属配置�?
    涵盖自动打标签��朋友圈运营、批量群发等核心业务参数�?
    """
    industry: str = "房产汽车"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['潜客初筛', '预约看房', '试驾获客', '意向定金', '线索流转', '高净值画�?]
    
    # 更多行业预置参数霢�购买商业版获�?
    pass