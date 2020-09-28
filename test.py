import unittest
import json
import xmltodict

from book import GoodreadsAPIClient

class TestGoodReadAPIClient(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    class_object = GoodreadsAPIClient() # instance of GoodReadsAPIClient class

    def test_valid_url(self):
        '''Test Case for valid good reads URL'''
        url         = "https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire"
        key_count   = 0
        result      = self.class_object.extract_bookid_from_url(url)
        json_data   = json.loads(result)
        # Get key count
        if 'title' in json_data and 'image_url' in json_data and 'publication_year' in json_data:
            key_count+=3
        if 'average_rating' in json_data and 'ratings_count' in json_data and 'num_pages' in json_data:
            key_count+=3
        if 'authors' in json_data:
            key_count+=1
        self.assertEqual(key_count, 7)
        print('Given URL is Valid')

    def test_invalid_url(self):
        '''Test Case for In-valid good reads URL'''
        url         = "https://www.goodreads.com/book/show/The_Godfather"
        result      = self.class_object.extract_bookid_from_url(url)
        self.assertEqual(result,"InvalidGoodreadsURL")
        print('Given URL is In-Valid')

    def test_xml_json_conversion(self):
        '''Test case for xml conversion'''
        my_xml = """
                <test>
                <id what="attribute">1234</id>
                <name>Sundar</name>
                </test>
            """
        json_string = json.dumps(xmltodict.parse(my_xml))
        result = json.loads(json_string)
        if type(result) is dict:
            flag = True
        self.assertEqual(True,flag)
        print("Given xml data is valid")

if __name__ == '__main__':
    unittest.main()
