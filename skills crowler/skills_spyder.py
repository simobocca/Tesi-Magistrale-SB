import scrapy


class QuotesSpider(scrapy.Spider):
    name = "skills"

    def start_requests(self):

        urls = []

        in_file = open('/home/simo/UnInfo/Tesi Magistrale/test/usernames_in_team/usernames_in_team_1.txt',"r")
        while True:
            in_line = in_file.readline()
            if in_line == "":
                break

            urls.append('https://dribbble.com/'+in_line)
            

        #urls = ['https://dribbble.com/shourav_chy01']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    



    def parse(self, response):

        url = response.css('div.full-tabs ul li a::attr(href)').extract()

        yield{
            'user' : url[0][url[0].rfind('/')+1:],
            'skills': response.css('ul.skills-list li a::attr(data-skill)').extract(),
        } 
            
