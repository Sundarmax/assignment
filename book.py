# Import python lib
import requests
import json
import xmltodict
import jsonpath
import pprint

class GoodreadsAPIClient:

    def __init__(self):
        pass

    def convert_xml_to_json(self,xml_data):
        json_string = json.dumps(xmltodict.parse(xml_data))
        return json.loads(json_string)

    def get_required_data(self,json_data):
        # print(type(json_data))
        _temp  = {}
        _temp['title']          = jsonpath.jsonpath(json_data,'GoodreadsResponse.book.title')
        _temp['average_rating'] = jsonpath.jsonpath(json_data,'GoodreadsResponse.book.work.average_rating')
        _temp['ratings_count']  = jsonpath.jsonpath(json_data,'GoodreadsResponse.book.work.ratings_count')
        _temp['num_pages']      = jsonpath.jsonpath(json_data,'GoodreadsResponse.book.work.num_pages')
        _temp['image_url']      = jsonpath.jsonpath(json_data,'GoodreadsResponse.book.image_url')
        _temp['publication_year'] = jsonpath.jsonpath(json_data,'GoodreadsResponse.book.publication_year')
        _temp['authors']          = jsonpath.jsonpath(json_data,'GoodreadsResponse.book.authors.author.name')
        return _temp

    def get_book_details(self,book_url):
        try:
            response = requests.get(book_url)
            # print(response.text)
            # convert xml object to json 
            json_data   = self.convert_xml_to_json(response.text)
            result_data = self.get_required_data(json_data)
            return json.dumps(result_data,indent=4)
        except requests.exceptions.HTTPError as errh:
            return "An Http Error occurred:" + repr(errh)
        except requests.exceptions.ConnectionError as errc:
            return "An Error Connecting to the API occurred:" + repr(errc)
        except requests.exceptions.Timeout as errt:
            return "A Timeout Error occurred:" + repr(errt)
        except requests.exceptions.RequestException as err:
            return "An Unknown Error occurred" + repr(err)
        except Exception as e:
            return str(e)

    def test(self):
        print('works')

if __name__ == "__main__":
    _url  = "https://www.goodreads.com/book/show/12177850.xml?key=f2RoSa6nNsAnsiFbb93EUg"
    obj = GoodreadsAPIClient()
    output = obj.get_book_details(_url)
    print(output)