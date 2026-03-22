import scrapy
from urllib.parse import urlencode
from bilibili_weekly.items import BilibiliWeeklyItem


class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["api.bilibili.com"]

    custom_headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,fr;q=0.7,fr-FR;q=0.6',
    'origin': 'https://www.bilibili.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Microsoft Edge";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
    # 'cookie': "enable_web_push=DISABLE; buvid4=3730451F-E54C-D1A2-B162-DD119A902EFC41295-024042401-UcSodAbmRba6Z5uFaugiRo4pCQmMqYeRQDiMb1iM42L540DDdqvWLHrumsCEmfXg; buvid_fp_plain=undefined; enable_feed_channel=ENABLE; buvid3=CD64C0D1-12EA-7198-517C-8005526DDE6892463infoc; b_nut=1745493892; _uuid=1F789DB8-6839-10B93-A2AD-98D851092106EF94141infoc; hit-dyn-v2=1; rpdid=|(k|kYYllJk)0J'u~R)Y)YluY; LIVE_BUVID=AUTO3217493000508296; fingerprint=31a32a47b4a733ceb66bed3655fca978; buvid_fp=351a9c8ef81044e192c4ff50a121c009; header_theme_version=OPEN; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; SESSDATA=d1dc8bc4%2C1776350829%2C27e92%2Aa1CjB-DV1j1BgRE6pHYjOjED3bk7ylNkVrCrDCjRjnwuxYLJHA69qTplPJnhtXc4TUER0SVnVUODl3MU9UVm9kaXFTVWU0aUpfalZVQ1FudmdMdGJtcGdDNUs4Uzh2ZzJwbXNTRVMwX2tTN3VNUERDbFhBdkY4Y21tLWJlQ1Q4ZlUwQW5rcEJzTnlBIIEC; bili_jct=6abd06817776902aa81d271bdb67a4ec; DedeUserID=238156820; DedeUserID__ckMd5=f646c99bee696b41; sid=78ocqv16; home_feed_column=5; PVID=1; browser_resolution=1528-698; CURRENT_QUALITY=80; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzM4NTQ0OTksImlhdCI6MTc3MzU5NTIzOSwicGx0IjotMX0.5Fj_QFW_D0wNvB7nzRDnDmuhbnLHI03CTYMDGQkI2DE; bili_ticket_expires=1773854439; bsource=search_google; bp_t_offset_238156820=1180861838825357312; b_lsid=98E73933_19CFD7D1076",
}

    custom_cookies = {
    'enable_web_push': 'DISABLE',
    'buvid4': '3730451F-E54C-D1A2-B162-DD119A902EFC41295-024042401-UcSodAbmRba6Z5uFaugiRo4pCQmMqYeRQDiMb1iM42L540DDdqvWLHrumsCEmfXg',
    'buvid_fp_plain': 'undefined',
    'enable_feed_channel': 'ENABLE',
    'buvid3': 'CD64C0D1-12EA-7198-517C-8005526DDE6892463infoc',
    'b_nut': '1745493892',
    '_uuid': '1F789DB8-6839-10B93-A2AD-98D851092106EF94141infoc',
    'hit-dyn-v2': '1',
    'rpdid': "|(k|kYYllJk)0J'u~R)Y)YluY",
    'LIVE_BUVID': 'AUTO3217493000508296',
    'fingerprint': '31a32a47b4a733ceb66bed3655fca978',
    'buvid_fp': '351a9c8ef81044e192c4ff50a121c009',
    'header_theme_version': 'OPEN',
    'theme-tip-show': 'SHOWED',
    'theme-avatar-tip-show': 'SHOWED',
    'SESSDATA': 'd1dc8bc4%2C1776350829%2C27e92%2Aa1CjB-DV1j1BgRE6pHYjOjED3bk7ylNkVrCrDCjRjnwuxYLJHA69qTplPJnhtXc4TUER0SVnVUODl3MU9UVm9kaXFTVWU0aUpfalZVQ1FudmdMdGJtcGdDNUs4Uzh2ZzJwbXNTRVMwX2tTN3VNUERDbFhBdkY4Y21tLWJlQ1Q4ZlUwQW5rcEJzTnlBIIEC',
    'bili_jct': '6abd06817776902aa81d271bdb67a4ec',
    'DedeUserID': '238156820',
    'DedeUserID__ckMd5': 'f646c99bee696b41',
    'sid': '78ocqv16',
    'home_feed_column': '5',
    'PVID': '1',
    'browser_resolution': '1528-698',
    'CURRENT_QUALITY': '80',
    'CURRENT_FNVAL': '4048',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzM4NTQ0OTksImlhdCI6MTc3MzU5NTIzOSwicGx0IjotMX0.5Fj_QFW_D0wNvB7nzRDnDmuhbnLHI03CTYMDGQkI2DE',
    'bili_ticket_expires': '1773854439',
    'bsource': 'search_google',
    'bp_t_offset_238156820': '1180861838825357312',
    'b_lsid': '98E73933_19CFD7D1076',
}

    def start_requests(self):
        latest_number = 364
        total_count = 100
        end_number = latest_number - total_count + 1

        for number in range(latest_number, end_number - 1, -1):
            params = {
                "number": str(number),
                "web_location": "333.934",
                "w_rid": "dd89ca7d1d839b3a6104b5d9afb00b96",
                "wts": "1773779358",
            }

            url = (
                "https://api.bilibili.com/x/web-interface/popular/series/one?"
                + urlencode(params)
            )

            headers = {
                **self.custom_headers,
                "referer": f"https://www.bilibili.com/v/popular/weekly?num={number}",
            }

            yield scrapy.Request(
                url=url,
                headers=headers,
                cookies=self.custom_cookies,
                callback=self.parse_one,
                cb_kwargs={"number": number},
                dont_filter=True,
            )

    def parse_one(self, response, number):
        data = response.json()

        if data.get("code") != 0:
            self.logger.error(f"第 {number} 期请求失败: {data}")
            return

        for video in data.get("data", {}).get("list", []):
            owner = video.get("owner") or {}
            stat = video.get("stat") or {}

            yield {
                "number": number,
                "up_name": owner.get("name"),
                "title": video.get("title"),
                "tname": video.get("tname"),
                "view": stat.get("view"),
                "like": stat.get("like"),
                "coin": stat.get("coin"),
                "favorite": stat.get("favorite"),
                "share": stat.get("share"),
                "reply": stat.get("reply"),
                "danmaku": stat.get("danmaku"),
            }