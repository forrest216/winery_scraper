from requests_html import HTML, HTMLSession
import json


data = []

session = HTMLSession()
pk = 1
napa_count = range(1,14)
for n in napa_count:
   a = session.get(f'https://www.napavalley.com/businesses/?category=Wineries&page={n}')
   wineries = a.html.find('.article-secondary')
   for winery in wineries:
      price_find = winery.find('.bizdetail__price>span')
      price = None
      base = 'https://www.napavalley.com'
      detail = winery.find('.article-body-meta a')[0].attrs['href']
      grapes = ''
      if 'www' not in detail:
         detail_page = session.get(base + detail)
         redlist = detail_page.html.find('.bizdetail__glance dl:nth-of-type(1) dd')
         for red in redlist: grapes += f'{red.text},'
         whitelist = detail_page.html.find('.bizdetail__glance dl:nth-of-type(2) dd')
         for white in whitelist: grapes += f'{white.text},'
      if len(price_find):
         price = f'From {price_find[0].text}'
      else:
         price = 'No price data available'
      item = {}
      item['pk'] = pk
      item['model'] = 'main_app.Winery'
      item['fields'] = {
         'name': winery.find('.article-body-meta h4')[0].text,
         'address': winery.find('.article-body-meta>h6')[0].text,
         'desc': winery.find('.article-body-entry>p')[0].text,
         'rating': 0,
         'grapes': grapes,
         'price': price,
         'region': 'Napa'
      }
      data.append(item)
      pk += 1

sonoma_count = range(1,12)
for n in sonoma_count:
   a = session.get(f'https://www.sonoma.com/businesses/?category=Wineries&page={n}')
   wineries = a.html.find('.article-secondary')
   for winery in wineries:
      price_find = winery.find('.bizdetail__price>span')
      price = None
      base = 'https://www.sonoma.com'
      detail = winery.find('.article-body-meta a')[0].attrs['href']
      grapes = ''
      if 'www' not in detail:
         detail_page = session.get(base + detail)
         redlist = detail_page.html.find('.bizdetail__glance dl:nth-of-type(1) dd')
         for red in redlist: grapes += f'{red.text},'
         whitelist = detail_page.html.find('.bizdetail__glance dl:nth-of-type(2) dd')
         for white in whitelist: grapes += f'{white.text},'
      if len(price_find):
         price = f'From {price_find[0].text}'
      else:
         price = 'No price data available'
      item = {}
      item['pk'] = pk
      item['model'] = 'main_app.Winery'
      item['fields'] = {
         'name': winery.find('.article-body-meta h4')[0].text,
         'address': winery.find('.article-body-meta>h6')[0].text,
         'desc': winery.find('.article-body-entry>p')[0].text,
         'rating': 0,
         'grapes': grapes,
         'price': price,
         'region': 'Sonoma'
      }
      data.append(item)
      pk += 1

with open('winery_scrape_final.json', 'w') as writeJSON:
   json.dump(data, writeJSON, ensure_ascii=False)