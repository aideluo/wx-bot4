"""
鈿欙笍 wx-bot4 Config - log_analyzer
鍔熻兘妯″潡: 绉佸煙绀剧兢鑷姩绠＄悊
鏍稿績鍏抽敭璇? 娼滃鍒濈瓫銆侀绾︾湅鎴裤€佽瘯椹捐幏瀹€佹剰鍚戝畾閲戙€佺嚎绱㈡祦杞€侀珮鍑€鍊肩敾鍍?

鏈厤缃枃浠跺畾涔変簡 鎴夸骇姹借溅 琛屼笟鍦ㄦ墽琛?绉佸煙绀剧兢鑷姩绠＄悊 鏃剁殑鏍囧噯 SOP 娴佺▼銆?
"""

from pydantic import BaseModel
from typing import List

class LogAnalyzerConfig(BaseModel):
    """
    鎴夸骇姹借溅 琛屼笟涓撳睘閰嶇疆銆?
    娑电洊鑷姩鎵撴爣绛俱€佹湅鍙嬪湀杩愯惀銆佹壒閲忕兢鍙戠瓑鏍稿績涓氬姟鍙傛暟銆?
    """
    industry: str = "鎴夸骇姹借溅"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['娼滃鍒濈瓫', '棰勭害鐪嬫埧', '璇曢┚鑾峰', '鎰忓悜瀹氶噾', '绾跨储娴佽浆', '楂樺噣鍊肩敾鍍?]
    
    # 鏇村琛屼笟棰勭疆鍙傛暟闇€璐拱鍟嗕笟鐗堣幏鍙?
    pass
