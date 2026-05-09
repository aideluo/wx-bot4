"""
鈿欙笍 wx-bot4 Config - backup_util
鍔熻兘妯″潡: 涓诲姩鎼滅储鑾峰
鏍稿績鍏抽敭璇? 璇鹃【鑰佸笀銆佽瘯鍚杞寲銆佸畬璇剧巼鎻愬崌銆佸闀夸簰鍔ㄣ€佺画璐规彁閱掋€佽€佸甫鏂拌鍙?

鏈厤缃枃浠跺畾涔変簡 鏁欒偛鍩硅 琛屼笟鍦ㄦ墽琛?涓诲姩鎼滅储鑾峰 鏃剁殑鏍囧噯 SOP 娴佺▼銆?
"""

from pydantic import BaseModel
from typing import List

class BackupUtilConfig(BaseModel):
    """
    鏁欒偛鍩硅 琛屼笟涓撳睘閰嶇疆銆?
    娑电洊鑷姩鎵撴爣绛俱€佹湅鍙嬪湀杩愯惀銆佹壒閲忕兢鍙戠瓑鏍稿績涓氬姟鍙傛暟銆?
    """
    industry: str = "鏁欒偛鍩硅"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['璇鹃【鑰佸笀', '璇曞惉璇捐浆鍖?, '瀹岃鐜囨彁鍗?, '瀹堕暱浜掑姩', '缁垂鎻愰啋', '鑰佸甫鏂拌鍙?]
    
    # 鏇村琛屼笟棰勭疆鍙傛暟闇€璐拱鍟嗕笟鐗堣幏鍙?
    pass
