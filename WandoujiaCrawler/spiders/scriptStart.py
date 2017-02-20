# coding=utf-8
#
# from twisted.internet import reactor
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
#
# from WandoujiaCrawler.spiders.crawler import socialAppCrawler
# from WandoujiaCrawler.spiders.crawler import QuotesSpider
#
#  CrawlerProcess适合与运行单线程单个爬虫程序
#  加get_projcet_settings()才可以读取配置文件,中间件才起作用
#  process = CrawlerProcess(get_project_settings())
#
#  process.crawl(socialAppCrawler)
#  process.start()
#
#  CrawlerRunner适合多线程多爬虫程序运行
# configure_logging()
# runner = CrawlerRunner(get_project_settings())
# runner.crawl(socialAppCrawler)
# d = runner.join()
# d.addBoth(lambda _: reactor.stop())
#
# reactor.run() # the script will block here until all crawling jobs are finished