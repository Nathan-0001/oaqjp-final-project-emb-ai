from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector('I am glad this happened')
        dominant_emotion = result1.get('dominant_emotion')
        self.assertEqual(dominant_emotion, 'joy')

if __name__ == "__main__":
    unittest.main()