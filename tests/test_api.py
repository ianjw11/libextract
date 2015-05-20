from .fixtures import foo_file
from libextract.api import extract, ARTICLE_TABLES


def test_extract(foo_file):
    r = extract(foo_file)
    u = [(node.tag, score) for node, score in r]
    assert u == [
        ('article', 36),
        ('body', 14),
    ]


def test_extract_tabular(foo_file):
    r = extract(foo_file, strategy=ARTICLE_TABLES)
    u = [node.tag for node in r]
    assert u == [
        'article',
        'html',
        'body',
    ]
    for node in r[0]:
        assert node.tag == 'div'