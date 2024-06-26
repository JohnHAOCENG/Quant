"""
《邢不行-2019新版|Python股票量化投资课程》
author: 邢不行/西蒙斯
微信: xingbuxing0807

# 课程内容
- pandas中的时间处理
"""
import pandas as pd  # 将pandas作为第三方库导入，我们一般为pandas取一个别名叫做pd

pd.set_option('expand_frame_repr', False)  # 当列太多时清楚展示

# =====导入数据
df = pd.read_csv(
    r'C:\Users\AA\Desktop\Mytrading\Trading\XBX Quant\data\a_stock_201903.csv',
    encoding='gbk',
    # skiprows=1
)

# ===== 时间处理

# print(df['交易日期'])
# print(df.at[0, '交易日期'])
# print(type(df.at[0, '交易日期']))
df['交易日期'] = pd.to_datetime(df['交易日期'])  # 将交易日期由字符串改为时间变量
# print(df.at[0, '交易日期'])
# print(type(df.at[0, '交易日期']))

# print(pd.to_datetime('1999年1月11日'))  # pd.to_datetime函数：将字符串转变为时间变量

print(df['交易日期'].dt.year)
print(df['交易日期'].dt.is_month_start)
print(df['交易日期'] + pd.Timedelta(hours= 1))

# print(df['交易日期'])
# print(df['交易日期'].dt.year)  # 输出这个日期的年份。相应的month是月份，day是天数，还有hour, minute, second
# print(df['交易日期'].dt.week)  # 这一天是一年当中的第几周
# print(df['交易日期'].dt.dayofyear)  # 这一天是一年当中的第几天
# print(df['交易日期'].dt.dayofweek)  # 这一天是这一周当中的第几天，0代表星期一
# print(df['交易日期'].dt.weekday)  # 和上面函数相同，更加常用
# print(df['交易日期'].dt.days_in_month)  # 这一天所在月份有多少天
# print(df['交易日期'].dt.is_month_end)  # 这一天是否是该月的开头，是否存在is_month_end？
# print(df['交易日期'] + pd.Timedelta(days=1))  # 增加一天，Timedelta用于表示时间差数据，[weeks, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds]
# print((df['交易日期'] + pd.Timedelta(days=1)) - df['交易日期'])  # 增加一天然后再减去今天的日期
