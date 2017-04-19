import unittest2 as unittest
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import shorturl.parts
import shorturl.filestore
import shorturl.dirstore

dir_path = os.path.dirname(os.path.realpath(__file__))


class UrlPartTest(unittest.TestCase):
    def test(self):
        part = shorturl.parts.generate_url_part()
        self.assertEqual(len(part), 6)


class UrlSaveTest(unittest.TestCase):
    def test(self):
        part = shorturl.parts.generate_url_part()
        url = 'http://google.com'
        path = '{0}/urls.csv'.format(dir_path)
        shorturl.filestore.save_url(path, part, url)
        
        num_lines = sum(1 for line in open(path))
        self.assertEqual(num_lines, 1)
        
        os.remove(path)


class UrlLoadTest(unittest.TestCase):
    def test(self):
        part = shorturl.parts.generate_url_part()
        url = 'http://google.com'
        path = '{0}/urls.csv'.format(dir_path)
        shorturl.filestore.save_url(path, part, url)
        
        num_lines = sum(1 for line in open(path))
        self.assertEqual(num_lines, 1)
        
        url = shorturl.filestore.load_url(path, part)
        self.assertEqual(url, 'http://google.com')
        
        os.remove(path)


class DirUrlSaveTest(unittest.TestCase):
    def test(self):
        part = shorturl.parts.generate_url_part()
        url = 'http://google.com'
        path = dir_path
        shorturl.dirstore.save_url(path, part, url)
        
        exists = os.path.exists(os.path.join(path, part))
        
        os.remove(os.path.join(path, part))
        
        self.assertEqual(True, exists)


class DirUrlLoadTest(unittest.TestCase):
    def test(self):
        part = shorturl.parts.generate_url_part()
        url = 'http://google.com'
        path = dir_path
        shorturl.dirstore.save_url(path, part, url)
        
        os.path.exists(os.path.join(path, part))
        
        url = shorturl.dirstore.load_url(path, part)
        
        os.remove(os.path.join(path, part))
        
        self.assertEqual(url, 'http://google.com', part)