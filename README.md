# information_retrieval

### run application
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