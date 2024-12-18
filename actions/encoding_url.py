import urllib.parse
u = '{"order":["i.name,asc"],"perPage":10,"page":1,"where":{"schoolId":60,"schoolYearId":24,"instrumentId":"27379","schoolGradeId":231,"brandId":1}}'
x = urllib.parse.quote(u)
print(x)
x = urllib.parse.quote(u, safe=',"')
print(x)