# information_retrieval


## run stuff from project root folder
### run application (front-end? maybe...)
```bash
cd web-app/front-end/scrappy
npm run serve
```

### run application (back-end? who knows...)
```bash
source scrapy_env/bin/activate
flask run
```

### run scrapy
```bash
source scrapy_env/bin/activate
cd space/
scrapy crawl spaceflight_now -o spaceflight_now.jsonl
```