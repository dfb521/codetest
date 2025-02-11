import re
from datetime import datetime

def reg_search(text, regex_list):
    result = []
    
    for regex_dict in regex_list:
        match_dict = {}
        for key, pattern in regex_dict.items():
            if pattern == '*自定义*':
                if key == '标的证券':
                    stock_code_pattern = r'股票代码：(\d{6}\.\w{2})'
                    match = re.search(stock_code_pattern, text)
                    if match:
                        match_dict[key] = match.group(1)
                elif key == '换股期限':
                    date_range_pattern = r'(\d{4}年\d{1,2}月\d{1,2}日)至(\d{4}年\d{1,2}月\d{1,2}日)'
                    match = re.search(date_range_pattern, text)
                    if match:
                        start_date = datetime.strptime(match.group(1), '%Y年%m月%d日').strftime('%Y-%m-%d')
                        end_date = datetime.strptime(match.group(2), '%Y年%m月%d日').strftime('%Y-%m-%d')
                        match_dict[key] = [start_date, end_date]
            else:
                matches = re.findall(pattern, text)
                if matches:
                    match_dict[key] = matches
        
        if match_dict:
            result.append(match_dict)
    
    return result