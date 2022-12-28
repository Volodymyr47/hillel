import requests
from datetime import datetime


class ExchangeRate:
    __DATE_FORMATS = ('%d.%m.%Y', '%Y.%m.%d', '%d-%m-%Y', '%Y%m%d', '%d_%m_%Y', '%Y_%m_%d', '%m/%d/%Y')

    def __init__(self, exchange_date=''):
        self.exchange_date = self.__format_date(exchange_date)
        self.link = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?{}&json'.format(f'date={self.exchange_date}')
        self.file_storage = self.get_file_name()

    def get_file_name(self):
        if self.exchange_date:
            file_name = datetime.strptime(self.exchange_date, '%Y%m%d').date().strftime('%d_%m_%Y') + '.txt'
            return file_name
        return 'The file_name was not created. Check your entered date'

    def __format_date(self, date_value):
        if date_value:
            for date_format in self.__class__.__DATE_FORMATS:
                try:
                    formatted_date = datetime.strptime(date_value, date_format).date().strftime('%Y%m%d')
                    return formatted_date
                except Exception:
                    continue
            else:
                print(f'The value of {date_value} is wrong or has a wrong date format. Please, use the correct date format')
        else:
            formatted_date = datetime.now().date().strftime('%Y%m%d')
            return formatted_date

    def has_json_data(self):
        response = requests.get(self.link, '')
        if not response:
            print(f'The unsatisfying status code have gotten. : {response.status_code}')
            return False
        if 'application/json' not in response.headers.get('Content-Type', ''):
            print('The received type of data does not match the format "json"')
            return False
        if len(response.text) <= 6:
            print('The response does not have any content')
            return False
        return True

    def _take_from_json(self):
        if self.has_json_data():
            data_list = requests.get(self.link).json()
            result_list = []
            for data in data_list:
                name = data.get('txt', '')
                abbreviation = data.get('cc', '')
                rate = data.get('rate', '')
                result_list.append([name, abbreviation, str(rate)])
            return result_list

    def saved_to_file(self):
        if self._take_from_json():
            data_list = self._take_from_json()
            if len(data_list) > 1:
                with open(self.file_storage, 'w') as file_storage:
                    for i in range(len(data_list)):
                        print(f'{i+1}. {data_list[i][0]} ({data_list[i][1]}) to UAH: {data_list[i][2]}',
                              file=file_storage)
                    return True
        return False
