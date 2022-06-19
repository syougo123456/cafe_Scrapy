import sqlite3

class CafeScrapyPipeline:
    _db = None

    @classmethod
    def get_database(cls):
        cls._db = sqlite3.connect('C:\project4\cafeproject\db.sqlite3')

        return cls._db
    
    def process_item(self, item, spider):
            """
            Pipeline にデータが渡される時に実行される
            item に spider から渡された item がセットされる
            """
            self.save_post(item)
            return item

    def save_post(self, item):
        """
        item を DB に保存する
        """
        if self.find_post(item['store_name']):
            # 既に同じ店名のデータが存在する場合はスキップ
            return

        db = self.get_database()
        db.execute(
            'INSERT INTO cafe_cafe (store_name, address, business_hours, regular_holiday, wifi, access, hp, img_url, ido, keido) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                item['store_name'],
                item['address'],
                item['business_hours'],
                item['regular_holiday'],
                item['wifi'],
                item['access'],
                item['hp'],
                item['img_url'],
                item['ido'],
                item['keido']
            )
        )
        db.commit()

    def find_post(self, store_name):
        db = self.get_database()
        cursor = db.execute(
            'SELECT * FROM cafe_cafe WHERE store_name=?',
            (store_name,)
        )
        return cursor.fetchone()