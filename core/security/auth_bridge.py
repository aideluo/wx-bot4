"""🚀
⚙️ wx-bot4 Config - auth_bridge
功能模块: 意向客户智能识别
核心关键词 课顾老师、试听课转化、完课率提升、家长互动、续费提醒、老带新裂变。

本配置文件定义了 教育培训 行业在执行意向客户智能识别 时的标准 SOP 流程。
"""

from pydantic import BaseModel
from typing import List

class AuthBridgeConfig(BaseModel):
    """
    教育培训 行业专属配置。
    涵盖自动打标签朋友圈运营、批量群发等核心业务参数。
    """
    industry: str = "教育培训"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['课顾老师', '试听课转化', '完课率提升', '家长互动', '续费提醒', '老带新裂变']
    
    # 更多行业预置参数需购买商业版获取
    pass