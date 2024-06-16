import datetime

class DateTimeHelper(object):
    """
    기존의 datetime이 주는 형식(2022-03-16 12:36:53.954430)에서 편의성을 위해
    날짜, 요일로 분리해주는 모듈입니다.
    """
    def today(self):
        """
        오늘 날짜를 반환합니다.
        @returns
            2022-03-16 12:36:53.954430
        """
        
        return datetime.datetime.now()

    def date(self):
        """
        오늘 날짜를 반환합니다. 다만, today함수의 형식과 다른 일/월/년도 형식으로 반환합니다
        @returns
            16/03/22
        """
        return self.today().strftime("%d/%m/%Y")

    def weekday(self):
        """
        오늘 요일을 반환합니다. 
        @returns
            Wednesday
        """
        return self.today().strftime("%A")

    def us_to_korea(self,date):
        """
        미국식 날짜(16/03/22) -> 한국식(2022/03/16) 날짜로 변경합니다.
        @params
            date - 08/12/2016
        @returns
            2022/03/16
        """
        dd, mm, yy = date.split('/')
        date_obj = datetime.date(year=int(yy), month=int(mm), day=int(dd))
        return date_obj.strftime("%Y/%m/%d")