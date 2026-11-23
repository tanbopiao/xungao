"""训诰（XUNGAO）· 元提示范式库

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：元提示范式库。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Xungao:
    """训诰（XUNGAO）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "XUNGAO"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.prompts = {}
        self._seq = 0

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "xungao",
            "cn": "训诰",
            "code": self.CODE,
            "duty": "元提示范式库",
            "mingwen": "先王之辞，垂范立言",
            "anchor": self.ANCHOR,
        }

    def put(self, prompt):
        """垂范立言：范式入库。"""
        self._seq += 1
        pid = "XG-%04d" % self._seq
        self.prompts[pid] = prompt
        self.events.append({"event": "put", "prompt_id": pid})
        return pid

    def get(self, prompt_id):
        """按号取范。"""
        if prompt_id not in self.prompts:
            raise KeyError("无此范式： %s" % prompt_id)
        self.events.append({"event": "get", "prompt_id": prompt_id})
        return self.prompts[prompt_id]
