from functools import partial

from ._compat import BytesIO
from .core import parse_html, pipeline, select, measure, rank, finalise

def extract(document, encoding='utf-8', count=None):
    if isinstance(document, bytes):
        document = BytesIO(document)
    
    crank = partial(rank, count=count) if count else rank
    
    return pipeline(
        parse_html(document, encoding=encoding),
        (select, measure, crank, finalise)
        )


class Extractor(object):

  def extract_lxml(self, elem, count=None):
    crank = partial(rank, count=count) if count else rank
    return pipeline(
        elem,
        (select, measure, crank, finalise))

  def extract_response(self, response, count=None):
    self.elem = elem = response.xpath('.')[0].root
    return self.extract_lxml(elem, count)

  def extract(self, document, encoding='utf-8', count=None):
      if isinstance(document, bytes):
          document = BytesIO(document)
      self.elem = elem = parse_html(document, encoding=encoding)

      return self.extract_lxml(elem, count)

