from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime

class utcnow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True

@compiles(utcnow, 'mysql')
def mysql_utcnow(element, compiler, **kw):
    return "(UTC_TIMESTAMP)"