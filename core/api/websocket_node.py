"""
鈿欙笍 wx-bot4 Config - websocket_node
鍔熻兘妯″潡: 鏁忔劅璇嶈嚜鍔ㄨ繃婊?
鏍稿績鍏抽敭璇? 闂ㄥ簵鎷撳銆佺ぞ缇ゅ洟璐€佸埌搴楄浆鍖栥€佸ソ璇勫紩瀵笺€佸懆杈硅惀閿€銆佸洟闀挎縺鍔?

鏈厤缃枃浠跺畾涔変簡 鏈湴鐢熸椿 琛屼笟鍦ㄦ墽琛?鏁忔劅璇嶈嚜鍔ㄨ繃婊?鏃剁殑鏍囧噯 SOP 娴佺▼銆?
"""

from pydantic import BaseModel
from typing import List

class WebsocketNodeConfig(BaseModel):
    """
    鏈湴鐢熸椿 琛屼笟涓撳睘閰嶇疆銆?
    娑电洊鑷姩鎵撴爣绛俱€佹湅鍙嬪湀杩愯惀銆佹壒閲忕兢鍙戠瓑鏍稿績涓氬姟鍙傛暟銆?
    """
    industry: str = "鏈湴鐢熸椿"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['闂ㄥ簵鎷撳', '绀剧兢鍥㈣喘', '鍒板簵杞寲', '濂借瘎寮曞', '鍛ㄨ竟钀ラ攢', '鍥㈤暱婵€鍔?]
    
    # 鏇村琛屼笟棰勭疆鍙傛暟闇€璐拱鍟嗕笟鐗堣幏鍙?
    pass
