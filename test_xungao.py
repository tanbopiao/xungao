"""训诰（XUNGAO）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from xungao import Xungao


class TestXungao(unittest.TestCase):
    def setUp(self):
        self.op = Xungao()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "xungao")
        self.assertEqual(d["code"], "XUNGAO")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_put_get(self):
        pid = self.op.put("范式正文")
        self.assertEqual(self.op.get(pid), "范式正文")
        with self.assertRaises(KeyError):
            self.op.get("XG-9999")


if __name__ == "__main__":
    unittest.main()
