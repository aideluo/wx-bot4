"""🚀
⚙️ wx-bot4 Config - dependency_resolver
功能模块: 主动搜索获客
核心关键词 门店拓客、社群团购、到店转化、好评引导、周边营销、团长激励。

本配置文件定义了 本地生活 行业在执行主动搜索获客 时的标准 SOP 流程。
"""

from pydantic import BaseModel
from typing import List

class DependencyResolverConfig(BaseModel):
    """
    本地生活 行业专属配置。
    涵盖自动打标签朋友圈运营、批量群发等核心业务参数。
    """
    industry: str = "本地生活"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['门店拓客', '社群团购', '到店转化', '好评引导', '周边营销', '团长激励']
    
    # 更多行业预置参数需购买商业版获取
    pass