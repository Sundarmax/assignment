# Import python lib
import requests
import json
import xmltodict
import jsonpath
import pprint

class GoodreadsAPIClient:

    def __init__(self):
        '''Constructor'''
        self._url = ""

    def convert_xml_to_json(self,xml_data):
        '''It converts the xml object to json object'''
        json_string = json.dumps(xmltodict.parse(xml_data))
        return json.loads(json_string)

    def get_required_data(self,json_data):
        '''A function which collects required data from the good reads API response'''
        book_dict = jsonpath.jsonpath(json_data,'GoodreadsResponse.book')[0]
        author_dict = jsonpath.jsonpath(json_data,'GoodreadsResponse.book.authors.author')[0]
        _temp  = {}
        _temp['title']          = book_dict.get('title',None)
        _temp['image_url']          = book_dict.get('image_url',None)
        _temp['publication_year']   = book_dict.get('publication_year',None)
        if book_dict.get('average_rating',None) is not None:
            _temp['average_rating'] = float(book_dict.get('average_rating'))
        else:
            _temp['average_rating'] = book_dict.get('average_rating',None)
        if book_dict.get('ratings_count',None) is not None:
            _temp['ratings_count']  = int(book_dict.get('ratings_count'))
        else:
            _temp['ratings_count']  = book_dict.get('ratings_count',None)
        if book_dict.get('num_pages',None) is not None:
            _temp['num_pages']      = int(book_dict.get('num_pages'))
        else:
            _temp['num_pages']      = book_dict.get('num_pages',None)
        if type(author_dict) is list:
            authors = ""
            for author in author_dict:
                authors+=author.get('name',None)
                authors+=' '
            _temp['authors']            = authors
        else:
            _temp['authors']            = author_dict.get('name',None)
        return _temp

    def get_book_details(self):
        '''A function which uses requests to get the data from Goodreads website'''
        try:
            response = requests.get(self._url)
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
            print(e)
            return "InvalidGoodreadsURL"

    def extract_bookid_from_url(self,url):
        '''A function which extracts book id from the given URL'''
        _bookId = ""
        for i,char in enumerate(url):
            if char >= '0' and char <= '9':
                _bookId+=char
                # check if next element is int or char
                try:
                    next_char = url[i+1]
                    if not next_char >= '0' and next_char <= '9':
                        # print(next_char,i)
                        break
                except IndexError:
                    pass
        if _bookId != "":
            self._url = "https://www.goodreads.com/book/show/" + _bookId +".xml?key=f2RoSa6nNsAnsiFbb93EUg"
            # print(self._url)
            return self.get_book_details()
        else:
            return "InvalidGoodreadsURL"

if __name__ == "__main__":
    #_url  = "https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire"
    obj = GoodreadsAPIClient()
    url_input = input('Please enter the goodreads URL : ')
    result = obj.extract_bookid_from_url(url_input)
    print(result)