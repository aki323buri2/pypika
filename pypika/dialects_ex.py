from .dialects import (
  MSSQLQuery, 
  MSSQLQueryBuilder, 
)

class MSSQLv2kQuery(MSSQLQuery):
  @classmethod
  def _builder(cls, **kwargs):
    return MSSQLv2kQueryBuilder(**kwargs)

class MSSQLv2kQueryBuilder(MSSQLQueryBuilder):
  QUOTE_CHAR = '[' 

  def _top_sql(self):
    if self._top:
      return 'TOP {} '.format(self._top)
    else: 
      return ''
