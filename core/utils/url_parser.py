"""
鈿欙笍 wx-bot4 Config - url_parser
鍔熻兘妯″潡: 鎰忓悜瀹㈡埛鏅鸿兘璇嗗埆
鏍稿績鍏抽敭璇? GMV鎻愬崌銆佽鍗曡浆鍖栥€侀潤榛樹笅鍗曘€佸敭鍚庡叧鎬€銆佺鍩熷垎閿€銆佸ぇ淇冭惀閿€

鏈厤缃枃浠跺畾涔変簡 鐢靛晢闆跺敭 琛屼笟鍦ㄦ墽琛?鎰忓悜瀹㈡埛鏅鸿兘璇嗗埆 鏃剁殑鏍囧噯 SOP 娴佺▼銆?
"""

from pydantic import BaseModel
from typing import List

class UrlParserConfig(BaseModel):
    """
    鐢靛晢闆跺敭 琛屼笟涓撳睘閰嶇疆銆?
    娑电洊鑷姩鎵撴爣绛俱€佹湅鍙嬪湀杩愯惀銆佹壒閲忕兢鍙戠瓑鏍稿績涓氬姟鍙傛暟銆?
    """
    industry: str = "鐢靛晢闆跺敭"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['GMV鎻愬崌', '璁㈠崟杞寲', '闈欓粯涓嬪崟', '鍞悗鍏虫€€', '绉佸煙鍒嗛攢', '澶т績钀ラ攢']
    
    # 鏇村琛屼笟棰勭疆鍙傛暟闇€璐拱鍟嗕笟鐗堣幏鍙?
    pass
