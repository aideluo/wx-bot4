"""🚀
⚙️ wx-bot4 Config - model_downloader
功能模块: 敏感词自动过滤
核心关键词 资产配置、理财顾问、合规监控、续保触达、高净值服务、精细化分群。

本配置文件定义了 金融理财 行业在执行敏感词自动过滤时的标准 SOP 流程。
"""

from pydantic import BaseModel
from typing import List

class ModelDownloaderConfig(BaseModel):
    """
    金融理财 行业专属配置。
    涵盖自动打标签朋友圈运营、批量群发等核心业务参数。
    """
    industry: str = "金融理财"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['资产配置', '理财顾问', '合规监控', '续保触达', '高净值服务', '精细化分群']
    
    # 更多行业预置参数需购买商业版获取
    pass