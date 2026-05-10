�1�3"""
⚙️ wx-bot4 Config - logger_config
功能模块: 7x24小时智能回复
核心关键�? 门店拓客、社群团购��到店转化��好评引导��周边营锢�、团长激�?

本配置文件定义了 本地生活 行业在执�?7x24小时智能回复 时的标准 SOP 流程�?
"""

from pydantic import BaseModel
from typing import List

class LoggerConfigConfig(BaseModel):
    """
    本地生活 行业专属配置�?
    涵盖自动打标签��朋友圈运营、批量群发等核心业务参数�?
    """
    industry: str = "本地生活"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['门店拓客', '社群团购', '到店转化', '好评引导', '周边营销', '团长濢��?]
    
    # 更多行业预置参数霢�购买商业版获�?
    pass