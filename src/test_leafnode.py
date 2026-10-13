import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Link to Google", {"href":"https://google.com", "target":"_blank"})
        self.assertEqual(node.to_html(), "<a href=\"https://google.com\" target=\"_blank\">Link to Google</a>")

    def test_leaf_to_html_h(self):
        node = LeafNode("h1", "Main Title")
        self.assertEqual(node.to_html(), "<h1>Main Title</h1>")

    def test_leaf_to_html_code(self):
        node = LeafNode("code", """def test_func(n):
            return (n * n)""")
        self.assertEqual(node.to_html(), """<code>def test_func(n):
            return (n * n)</code>""")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "unformatted test text")
        self.assertEqual(node.to_html(), "unformatted test text")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
