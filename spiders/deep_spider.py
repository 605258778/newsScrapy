# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Article(scrapy.Item):
    folder_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    count_view = scrapy.Field()
    count_comment = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    is_comment = scrapy.Field()
    is_recommend = scrapy.Field()
    sort = scrapy.Field()
    jump_url = scrapy.Field()
    image_url = scrapy.Field()
    image_net_url = scrapy.Field()
    file_url = scrapy.Field()
    file_name = scrapy.Field()
    approve_status = scrapy.Field()
    publish_time = scrapy.Field()
    publish_user = scrapy.Field()
    start_time = scrapy.Field()
    end_time = scrapy.Field()
    update_time = scrapy.Field()
    create_time = scrapy.Field()
    create_id = scrapy.Field()
    url = scrapy.Field()

class DeepSpider(CrawlSpider):
    name = "Deep"

    def __init__(self,rule):
        self.rule = rule
        self.name = rule.name
        self.allowed_domains = rule.allow_domains.split(",")
        self.start_urls = rule.start_urls.split(",")
        rule_list = []
        #添加`下一页`的规则
        if rule.next_page:
            rule_list.append(Rule(LinkExtractor(restrict_xpaths = rule.next_page)))

        #添加抽取文章链接的规则
        rule_list.append(Rule(LinkExtractor(
            allow=[rule.allow_url]),
            callback='parse_item',follow=True))
        self.rules = tuple(rule_list)

        super(DeepSpider, self).__init__()


    def parse_item(self, response):
        self.log('Hi, this is an article page! %s' % response.url)

        article = Article()

        article["url"] = response.url
        if self.rule.allow_domains == "gzfip.cn":
            title = response.xpath(self.rule.title_xpath).extract()
            article["title"] = title[0] if title else ""

            body = response.xpath(self.rule.body_xpath).extract()
            articleContent =  '\n'.join(body) if body else ""
            if(articleContent!=""):
                articleContent = articleContent.replace('<img src="/','<img src="http://'+self.rule.allow_domains+'/')
            article["content"] =  articleContent

            publish_time = response.xpath(self.rule.publish_time_xpath).extract()
            article["publish_time"] = (publish_time[0].decode('utf8')[5:15].encode('utf8') if (publish_time[0].find("更新时间")!=-1) else publish_time[0]) if publish_time else ""

            source_site = response.xpath(self.rule.source_site_xpath).extract()

            article["publish_user"] = source_site[0][source_site[0].find("作者:")+3:source_site[0].find("来源")-2]
            article["folder_id"] = 2
        elif self.rule.allow_domains == "forestry.gov.cn":
            title = response.xpath(self.rule.title_xpath).extract()
            article["title"] = title[0] if title else ""

            body = response.xpath(self.rule.body_xpath).extract()
            articleContent =  '\n'.join(body) if body else ""
            if(articleContent!=""):
                articleContent = articleContent.replace('alt src="/','alt src="http://'+self.rule.allow_domains+'/')
            article["content"] =  articleContent

            publish_time = response.xpath(self.rule.publish_time_xpath).extract()
            article["publish_time"] = publish_time[0] if publish_time else ""

            source_site = response.xpath(self.rule.source_site_xpath).extract()

            article["publish_user"] = ""
            article["folder_id"] = 2
        return article
