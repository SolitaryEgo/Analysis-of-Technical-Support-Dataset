import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line, Bar, Scatter

df = pd.read_csv('./Technical Support Dataset.csv')
print(df.head())
print(df.isna().sum())
print(df.describe(include='all'))

# 将 'Created time' 转换为 datetime 类型
df['Created time'] = pd.to_datetime(df['Created time'])

# 按日、周、月分组统计票量
daily_counts = df.groupby(df['Created time'].dt.date).size()
weekly_counts = df.groupby(df['Created time'].dt.to_period('W')).size()
monthly_counts = df.groupby(df['Created time'].dt.to_period('M')).size()

# 提取月份
df['Month'] = df['Created time'].dt.to_period('M')

# 绘制每日票量图表
daily_chart = Line()
daily_chart.add_xaxis(daily_counts.index.astype(str).tolist())
daily_chart.add_yaxis("Daily Tickets", daily_counts.tolist())

daily_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="Daily Ticket Volume"),
    xaxis_opts=opts.AxisOpts(name="Date", type_="category", axislabel_opts=opts.LabelOpts(rotate=45)),
    yaxis_opts=opts.AxisOpts(name="Number of Tickets"),
)

daily_chart.render('daily_ticket_volume.html')

# 绘制每周票量图表
weekly_chart = Line()
weekly_chart.add_xaxis(weekly_counts.index.astype(str).tolist())
weekly_chart.add_yaxis("Weekly Tickets", weekly_counts.tolist())

weekly_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="Weekly Ticket Volume"),
    xaxis_opts=opts.AxisOpts(name="Week", type_="category"),
    yaxis_opts=opts.AxisOpts(name="Number of Tickets"),
)

weekly_chart.render('weekly_ticket_volume.html')

# 绘制每月票量图表
monthly_chart = Line()
monthly_chart.add_xaxis(monthly_counts.index.astype(str).tolist())
monthly_chart.add_yaxis("Monthly Tickets", monthly_counts.tolist())

monthly_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="Monthly Ticket Volume"),
    xaxis_opts=opts.AxisOpts(name="Month", type_="category"),
    yaxis_opts=opts.AxisOpts(name="Number of Tickets"),
)

monthly_chart.render('monthly_ticket_volume.html')

# 按小时统计票量
df['Hour'] = df['Created time'].dt.hour
hourly_counts = df.groupby('Hour').size()

# 绘制高峰时间图表
peak_time_chart = Line()
peak_time_chart.add_xaxis(hourly_counts.index.astype(str).tolist())
peak_time_chart.add_yaxis("Hourly Tickets", hourly_counts.tolist())

peak_time_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="Ticket Volume by Hour"),
    xaxis_opts=opts.AxisOpts(name="Hour", type_="category"),
    yaxis_opts=opts.AxisOpts(name="Number of Tickets"),
)

peak_time_chart.render('peak_time.html')

# 按月份和主题分组，统计票据数量
topic_trends = df.groupby(['Month', 'Topic']).size().unstack(fill_value=0)

# Trends of Ticket Topics Over Time
line_chart = Line()
line_chart.add_xaxis(topic_trends.index.astype(str).tolist())
for topic in topic_trends.columns:
    line_chart.add_yaxis(topic, topic_trends[topic].tolist(), is_smooth=True, symbol="circle")

line_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="Trends of Ticket Topics Over Time"),
    xaxis_opts=opts.AxisOpts(name="Month", type_="category", axislabel_opts=opts.LabelOpts(rotate=45)),
    yaxis_opts=opts.AxisOpts(name="Number of Tickets"),
)

line_chart.render('topic_trends.html')

# Ticket Count by Source
source_summary = df['Source'].value_counts()

bar_chart = Bar()
bar_chart.add_xaxis(source_summary.index.tolist())
bar_chart.add_yaxis("Ticket Count", source_summary.tolist(), color='lightgreen')

bar_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="Ticket Count by Source"),
    xaxis_opts=opts.AxisOpts(name="Source"),
    yaxis_opts=opts.AxisOpts(name="Ticket Count"),
)

bar_chart.render('source_summary.html')

# Ticket Submissions by Location
scatter_chart = Scatter()
scatter_chart.add_xaxis(df['Longitude'].tolist())
scatter_chart.add_yaxis("Ticket Submissions", df['Latitude'].tolist(), symbol_size=10)

scatter_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="Ticket Submissions by Location"),
    xaxis_opts=opts.AxisOpts(name="Longitude"),
    yaxis_opts=opts.AxisOpts(name="Latitude"),
    visualmap_opts=opts.VisualMapOpts(max_=df['Latitude'].max(), min_=df['Latitude'].min())
)

scatter_chart.render('ticket_submissions.html')


