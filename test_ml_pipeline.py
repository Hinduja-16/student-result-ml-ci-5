import unittest
from pathlib import Path

class TestMLPipeline(unittest.TestCase):
    def test_model_exists(self):
        self.assertTrue(Path("student_result_model.pkl").exists())

    def test_metrics_exist(self):
        self.assertTrue(Path("metrics.json").exists())

if __name__ == "__main__":
    unittest.main()
