"""
datetimehelper 모듈 테스터
"""
import datetime
import unittest
from unittest.mock import patch
import datetimehelper


class DateTimeHelperTestCase(unittest.TestCase):
    """
    Unit Test - testcase class [DateTimeHelper 클래스]
    """
    def setUp(self) -> None:
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
        self.assertEqual(self.obj.us_to_korea(d1), '2016/12/08')
        self.assertEqual(self.obj.us_to_korea(d2), '2021/11/24')
        self.assertEqual(self.obj.us_to_korea(d3), '2019/02/02')
        self.assertEqual(self.obj.us_to_korea(d4), '2021/03/16')
    
    def test_date(self):
        """
        datetimehelper.py > today() 메소드 테스트
        DateTimeHelper의 today 메서드가 호출될 때 유저가 설정한 test_data값을 반환하도록 가짜 메서드를 설정
        """

        # 테스트를 위한 날짜를 지정해서 만들어줍니다.
        test_date = datetime.datetime(year=2022,month=2,day=10)

        # patch를 통해 today() 메소드에 내가 지정한 날짜를 넣고 테스를 진행합니다.
        #                   객체, 객채의 메소드 명,   테스트용 데이터 
        with patch.object(self.obj, 'today', return_value=test_date):
            response = self.obj.date()
            self.assertEqual(response, '10/02/2022')
            
    def test_weekday(self):
        """
        datetimehelper.py > weekday() 메소드 테스트
        """
        
        # 테스트를 위한 날짜를 지정해서 만들어줍니다.
        test_date = datetime.datetime(year=2022,month=2,day=10)

        # self.obj = datetimehelper.DateTimeHelper()에 있는 today메소드에 테스트를 원하는 데이터를 넣고 테스트를 진행합니다.
        with patch.object(self.obj, 'today', return_value=test_date):
            response = self.obj.weekday()
            self.assertEqual(response, 'Thursday')

    
if __name__ == '__main__':
    unittest.main()