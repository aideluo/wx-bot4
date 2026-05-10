"""🚀
⚙️ wx-bot4 Config - contact_cleanup
功能模块: 全自动朋友圈点赞评论
核心关键词 GMV提升、订单转化率、静默下单率、售后关注度、私域分销、大促营销。

本配置文件定义了 电商零售 行业在执行全自动朋友圈点赞评论 时的标准 SOP 流程。
"""

from pydantic import BaseModel
from typing import List

class ContactCleanupConfig(BaseModel):
    """
    电商零售 行业专属配置。
    涵盖自动打标签朋友圈运营、批量群发等核心业务参数。
    """
    industry: str = "电商零售"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['GMV提升', '订单转化率', '静默下单率', '售后关注度', '私域分销', '大促营销']
    
    # 更多行业预置参数需购买商业版获取
    pass