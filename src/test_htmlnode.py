import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_exist(self):
        node = HTMLNode(tag = "a",value = "link to google", props = {"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://google.com\"")

    def test_props_multi(self):
        node = HTMLNode(tag="a", value="link to googe", props={
          "href":"https://google.com", 
          "target":"_blank"
        })
        self.assertEqual(node.props_to_html(), " href=\"https://google.com\" target=\"_blank\"")

    def test_props_none(self):
        node = HTMLNode(tag="p", value="this is a test paragraph")
        self.assertEqual(node.props_to_html(), "")

    def test_props_empty(self):
        node = HTMLNode(tag="p", value="this is a test paragraph", props={})
        self.assertEqual(node.props_to_html(), "")
