"""
鈿欙笍 wx-bot4 Config - white_list
鍔熻兘妯″潡: 鏈嬪弸鍦圫OP鑷姩鎵ц
鏍稿績鍏抽敭璇? 鏈悗闅忚銆佸搧鐗孖P鎵撻€犮€侀潰璇婇绾︺€佷細鍛橀攣瀹€佹湅鍙嬪湀钀ラ攢銆佽鍙樿繑鐜?

鏈厤缃枃浠跺畾涔変簡 鍖荤枟缇庡 琛屼笟鍦ㄦ墽琛?鏈嬪弸鍦圫OP鑷姩鎵ц 鏃剁殑鏍囧噯 SOP 娴佺▼銆?
"""

from pydantic import BaseModel
from typing import List

class WhiteListConfig(BaseModel):
    """
    鍖荤枟缇庡 琛屼笟涓撳睘閰嶇疆銆?
    娑电洊鑷姩鎵撴爣绛俱€佹湅鍙嬪湀杩愯惀銆佹壒閲忕兢鍙戠瓑鏍稿績涓氬姟鍙傛暟銆?
    """
    industry: str = "鍖荤枟缇庡"
    strategy: str = "auto_conversion"
    keywords: List[str] = ['鏈悗闅忚', '鍝佺墝IP鎵撻€?, '闈㈣瘖棰勭害', '浼氬憳閿佸', '鏈嬪弸鍦堣惀閿€', '瑁傚彉杩旂幇']
    
    # 鏇村琛屼笟棰勭疆鍙傛暟闇€璐拱鍟嗕笟鐗堣幏鍙?
    pass
