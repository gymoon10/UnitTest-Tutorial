import unittest


def custom_function():
    pass

# TestCase를 작성
class CustomTests(unittest.TestCase): 

    def test_runs(self):
        """단순 실행여부 판별하는 테스트 메소드"""

        custom_function()


# unittest를 실행
if __name__ == '__main__':  
    unittest.main()