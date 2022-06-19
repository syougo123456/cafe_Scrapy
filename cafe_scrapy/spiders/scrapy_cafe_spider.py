import scrapy
import json
from cafe_scrapy.items import Cafe_cafe

class ScrapyCafeSpiderSpider(scrapy.Spider):
    name = 'scrapy_cafe_spider'
    allowed_domains = ['webservice.recruit.co.jp']
    start_urls = ['http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=アクセスキー&count=50&large_area=Z011&keyword=カフェ%20渋谷&format=json']

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        for cafe in jsonresponse["results"]["shop"]:
            yield Cafe_cafe(
                store_name = cafe["name"],          # 店名
                address = cafe["address"],          # 住所
                business_hours = cafe["open"],      # 営業時間
                regular_holiday = cafe["close"],    # 定休日
                wifi = cafe["wifi"],                # WiFi有無
                access = cafe["access"],            # アクセス
                hp = cafe["urls"]["pc"],            # ホームページ
                img_url = cafe["photo"]["pc"]["l"], # 画像URL
                ido = cafe["lat"],                  # 緯度
                keido = cafe["lng"],                # 経度
            )
            
