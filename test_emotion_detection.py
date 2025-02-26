import unittest
from EmotionDetection import emotion_detection as ed 

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        test_data = [\
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear") ]

        test_num = 0
        for statement, dominant_emotion in test_data:
            test_num += 1
            print( f"Test # {test_num}")
            self.assertEqual(ed.emotion_detector(statement)['dominant_emotion'], dominant_emotion)

if __name__ == '__main__':
    unittest.main()
