�1�3"""
⚙️ wx-bot4 Config - black_list
功能模块: 敏感词自动过�?
核心关键�? GMV提升、订单转化��静默下单��售后关怢�、私域分锢�、大促营锢�

本配置文件定义了 电商零售 行业在执�?敏感词自动过�?时的标准 SOP 流程�?
"""

from pydantic import BaseModel
from typing import List

class BlackListConfig(BaseModel):
    """
    电商零售 行业专属配置�?
    涵盖自动打标签��朋友圈运营、批量群发等核心业务参数�?
    """
    industry: str = "电商零售"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['GMV提升', '订单转化', '静默下单', '售后关���', '私域分销', '大促营销']
    
    # 更多行业预置参数霢�购买商业版获�?
    pass