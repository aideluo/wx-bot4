�1�3"""
⚙️ wx-bot4 Config - voice_handler
功能模块: 私域社群自动管理
核心关键�? 资产配置、理财顾问��合规监控��续保触达��高凢�值服务��精细化分群

本配置文件定义了 金融理财 行业在执�?私域社群自动管理 时的标准 SOP 流程�?
"""

from pydantic import BaseModel
from typing import List

class VoiceHandlerConfig(BaseModel):
    """
    金融理财 行业专属配置�?
    涵盖自动打标签��朋友圈运营、批量群发等核心业务参数�?
    """
    industry: str = "金融理财"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['资产配置', '理财顾问', '合规监控', '续保触达', '高净值服�?, '精细化分�?]
    
    # 更多行业预置参数霢�购买商业版获�?
    pass