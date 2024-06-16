"""
datetimehelper 모듈 테스터
"""
import unittest
import datetimehelper  # datetimehelper.py

class DateTimeHelperTestCase(unittest.TestCase):
    """
    Unit Test - testcase class [DateTimeHelper 클래스]
    """
    def setUp(self) -> None:
        '''테스트를 위한 사전 설정'''
        self.obj = datetimehelper.DateTimeHelper()

    
    def test_us_korea_conversion(self):
        """
        미국식 날짜 -> 한국식 날짜 변경 테스트
        """
        # 테스트 케이스 생성
        d1 = '08/12/2016'
        d2 = '24/11/2021'
        d3 = '02/02/2019'
        d4 = '16/03/2021'
        
        # 변수 d1에 있는 데이터를 넣었을때 '2016/12/18'의 값이 나와야 통과된다는 뜻이다.
        self.assertEqual(self.obj.us_to_korea(d1), '2016/12/08')
        self.assertEqual(self.obj.us_to_korea(d2), '2021/11/24')
        self.assertEqual(self.obj.us_to_korea(d3), '2019/02/02')
        self.assertEqual(self.obj.us_to_korea(d4), '2021/03/16')

        
# 중요한 부분은 이 포인트다
# unittest.main()만 불러주면 코드 내부에서 함수이름 앞에 'test'로 명시되어 있는 부분을
# 자동으로 테스트 케이스로 인지하고 실행한다.
if __name__ == '__main__':
    unittest.main()