"""训诰（XUNGAO）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_put_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.put(None)

    def test_get_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.get(None)


if __name__ == "__main__":
    unittest.main()
