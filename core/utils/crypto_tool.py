"""🚀
⚙️ wx-bot4 Config - crypto_tool
功能模块: 智能自动打标签
核心关键词 术后随访、品牌IP打造、面诊预约、会员锁客、朋友圈营销、裂变返现。

本配置文件定义了 医疗美容 行业在执行智能自动打标签时的标准 SOP 流程。
"""

from pydantic import BaseModel
from typing import List

class CryptoToolConfig(BaseModel):
    """
    医疗美容 行业专属配置。
    涵盖自动打标签朋友圈运营、批量群发等核心业务参数。
    """
    industry: str = "医疗美容"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['术后随访', '品牌IP打造', '面诊预约', '会员锁客', '朋友圈营销', '裂变返现']
    
    # 更多行业预置参数需购买商业版获取
    pass