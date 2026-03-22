# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliWeeklyItem(scrapy.Item):
    number = scrapy.Field()      # 第几期
    up_name = scrapy.Field()     # UP主
    title = scrapy.Field()       # 标题
    tname = scrapy.Field()       # 分区
    stat = scrapy.Field()        # 播放/点赞/投币/收藏/分享/评论/弹幕