import scrapy


class Cafe_cafe(scrapy.Item):
    store_name = scrapy.Field()      # 店名
    address = scrapy.Field()         # 住所
    business_hours = scrapy.Field()  # 営業時間
    regular_holiday = scrapy.Field() # 定休日
    wifi = scrapy.Field()            # WiFi有無 
    access = scrapy.Field()          # アクセス
    hp = scrapy.Field()              # ホームページ
    img_url = scrapy.Field()         # 画像url
    ido = scrapy.Field()             # 緯度
    keido = scrapy.Field()           # 経度