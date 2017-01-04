
import time
from weasyprint import HTML
import os


from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from wikispider.tools.split_pdf import split_single_pdf


class WspiderSpider(CrawlSpider):

    name = 'wspider'

    allowed_domains = ['wikipedia.org']
    start_urls = ["http://en.wikipedia.org/wiki/"]
    count = 0
    # in seconds
    total_time = 0.0

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="mw-body"]//a'), callback='parse_item'),
        Rule(LinkExtractor(allow=("http://en.wikipedia.org/wiki/")), callback='parse_item'),

    )

    # Output Folder where splitted pdf pages should be placed
    pdf_path_out = os.path.join('/Users', 'jan.nehmiz', 'Documents', 'Automated_UI_Testing', 'Template_Files', '')

    def parse_item(self, response):
        start_time = time.time()

        url = response.url
        body = response.body

        filename = url[8:].replace('/', '_')
        pdf_filename = filename + '.pdf'
        pdf_filename2 = filename + '2.pdf'
        html_filename = filename + '.html'


        temp_pdf_path = os.path.join('..', 'crawled_files', '')

        # with open(temp_pdf_path + html_filename, 'w+b') as f:
        #     f.write(result)

        HTML(url).write_pdf(self.pdf_path_out + pdf_filename2)

        cmd_string = 'wkhtmltopdf --no-background --disable-external-links --grayscale --no-images --lowquality ' \
                     + url + ' ' + self.pdf_path_out + pdf_filename
        print(cmd_string)
        os.system(cmd_string)

        pages_created = split_single_pdf(pdf_filename, self.pdf_path_out, self.pdf_path_out)

        self.count += pages_created + 1
        diff_time = time.time() - start_time
        self.total_time += diff_time

        print("Process Time: --- %s seconds ---" % diff_time)
        print("Total Time: --- %s seconds ---" % self.total_time)
        print("Total Files: --- %s  ---" % self.count)

