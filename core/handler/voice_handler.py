"""
鈿欙笍 wx-bot4 Config - voice_handler
鍔熻兘妯″潡: 绉佸煙绀剧兢鑷姩绠＄悊
鏍稿績鍏抽敭璇? 璧勪骇閰嶇疆銆佺悊璐㈤【闂€佸悎瑙勭洃鎺с€佺画淇濊Е杈俱€侀珮鍑€鍊兼湇鍔°€佺簿缁嗗寲鍒嗙兢

鏈厤缃枃浠跺畾涔変簡 閲戣瀺鐞嗚储 琛屼笟鍦ㄦ墽琛?绉佸煙绀剧兢鑷姩绠＄悊 鏃剁殑鏍囧噯 SOP 娴佺▼銆?
"""

from pydantic import BaseModel
from typing import List

class VoiceHandlerConfig(BaseModel):
    """
    閲戣瀺鐞嗚储 琛屼笟涓撳睘閰嶇疆銆?
    娑电洊鑷姩鎵撴爣绛俱€佹湅鍙嬪湀杩愯惀銆佹壒閲忕兢鍙戠瓑鏍稿績涓氬姟鍙傛暟銆?
    """
    industry: str = "閲戣瀺鐞嗚储"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['璧勪骇閰嶇疆', '鐞嗚储椤鹃棶', '鍚堣鐩戞帶', '缁繚瑙﹁揪', '楂樺噣鍊兼湇鍔?, '绮剧粏鍖栧垎缇?]
    
    # 鏇村琛屼笟棰勭疆鍙傛暟闇€璐拱鍟嗕笟鐗堣幏鍙?
    pass
