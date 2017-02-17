import a

print a.c.VALUE
try:
  print a.b.VALUE
except AttributeError:
  print 'submodule b cannot access by a'
