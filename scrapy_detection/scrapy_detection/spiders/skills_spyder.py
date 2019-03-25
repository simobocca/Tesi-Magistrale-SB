import scrapy
import os.path
import json


class QuotesSpider(scrapy.Spider):
    name = "skills"
    n_file = 0
    user_in_file = 3


    def start_requests(self):

        urls = []

        in_file = open('/home/simo/UnInfo/Tesi Magistrale/test/usernames_in_team/test_404.txt',"r")
        while True:
            in_line = in_file.readline()
            if in_line == "":
                break

            urls.append('https://dribbble.com/'+in_line)
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, errback=self.parse_error)

    
    def parse_error(self, failure):

        response = failure.value.response
        url = response.request.url

        entry = '{user: ' + url+'-Error404, skills: []}\n'

        if os.path.isfile("test_write_skills"+str(self.n_file)+".txt"):
            num_lines = sum(1 for line in open("test_write_skills"+str(self.n_file)+".txt"))
        else:
            num_lines = 0

        if num_lines == self.user_in_file:
            self.n_file = self.n_file+1

        with open("test_write_skills"+str(self.n_file)+".txt", mode='a') as f:
            f.write(entry)

    def parse(self, response):

        url = response.css('div.full-tabs ul li a::attr(href)').extract()

        entry = '{user: ' + str(url[0][url[0].rfind('/')+1:]) + ', skills: '+ str(response.css('ul.skills-list li a::attr(data-skill)').extract()) + '}\n'

        if os.path.isfile("test_write_skills"+str(self.n_file)+".txt"):
            num_lines = sum(1 for line in open("test_write_skills"+str(self.n_file)+".txt"))
        else:
            num_lines = 0

        if num_lines == self.user_in_file:
            self.n_file = self.n_file+1

        with open("test_write_skills"+str(self.n_file)+".txt", mode='a') as f:
            f.write(entry)

            
