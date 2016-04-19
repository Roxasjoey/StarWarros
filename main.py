import json
import webapp2
import time

import model


def AsDict(guest):
  return {'id': guest.key.id(), 'dato1': guest.dato1, 'dato2': guest.dato2,
  'dato3': guest.dato3, 'dato4': guest.dato4, 'dato5': guest.dato5,
  'dato6': guest.dato6, 'dato7': guest.dato7, 'dato8': guest.dato8,
  'dato9': guest.dato9, 'dato10': guest.dato10, 'dato11': guest.dato11,
  'dato12': guest.dato12, 'dato13': guest.dato13, 'dato14': guest.dato14,
  'dato15': guest.dato15, 'dato16': guest.dato16, 'hab1': guest.hab1,
  'hab2': guest.hab2, 'hab3': guest.hab3, 'hab4': guest.hab4,
  'hab5': guest.hab5, 'hab6': guest.hab6, 'hab7': guest.hab7,
  'hab8': guest.hab8, 'hab9': guest.hab9, 'hab10': guest.hab10,
  'hab11': guest.hab11, 'hab12': guest.hab12, 'hab13': guest.hab13,
  'hab14': guest.hab14, 'hab15': guest.hab15, 'hab16': guest.hab16,
  'hab17': guest.hab17, 'hab18': guest.hab18, 'hab19': guest.hab19,
  'hab20': guest.hab20, 'hab21': guest.hab21, 'hab22': guest.hab22,
  'hab23': guest.hab23, 'hab24': guest.hab24, 'hab25': guest.hab25,
  'hab26': guest.hab26, 'hab27': guest.hab27, 'hab28': guest.hab28,
  'hab29': guest.hab29, 'hab30': guest.hab30, 'hab31': guest.hab31,
  'hab32': guest.hab32, 'hab33': guest.hab33, 'hab34': guest.hab34,
  'hab35': guest.hab35, 'hab36': guest.hab36, 'hab37': guest.hab37,
  'hab38': guest.hab38, 'hab39': guest.hab39, 'hab40': guest.hab40,
  'hab41': guest.hab41, 'hab42': guest.hab42, 'hab43': guest.hab43,
  'hab44': guest.hab44, 'hab45': guest.hab45, 'hab46': guest.hab46,
  'hab47': guest.hab47, 'hab48': guest.hab48, 'hab49': guest.hab49,
  'hab50': guest.hab50, 'hab51': guest.hab51, 'var1': guest.var1,
  'var2': guest.var2, 'var3': guest.var3, 'var4': guest.var4,
  'var5': guest.var5, 'var6': guest.var6, 'var7': guest.var7,
  'var8': guest.var8, 'var9': guest.var9, 'var10': guest.var10,
  'var11': guest.var11, 'var12': guest.var12, 'var13': guest.var13,
  'var14': guest.var14, 'var15': guest.var15, 'var16': guest.var16,
  'var17': guest.var17, 'var18': guest.var18, 'var19': guest.var19,
  'var20': guest.var20, 'var21': guest.var21, 'var22': guest.var22,
  'var23': guest.var23, 'var24': guest.var24, 'var25': guest.var25,
  'var26': guest.var26, 'var27': guest.var27, 'var28': guest.var28,
  'var29': guest.var29, 'var30': guest.var30, 'var31': guest.var31,
  'var32': guest.var32, 'var33': guest.var33, 'var34': guest.var34,
  'info1': guest.info1, 'info2': guest.info2, 'info3': guest.info3,
  'info4': guest.info4,}


class RestHandler(webapp2.RequestHandler):

  def dispatch(self):
    #time.sleep(1)
    super(RestHandler, self).dispatch()


  def SendJson(self, r):
    self.response.headers['content-type'] = 'text/plain'
    self.response.write(json.dumps(r))
    

class QueryHandler(RestHandler):

  def get(self):
    guests = model.AllGuests()
    r = [ AsDict(guest) for guest in guests ]
    self.SendJson(r)


class UpdateHandler(RestHandler):

  def post(self):
    r = json.loads(self.request.body)
    guest = model.UpdateGuest(r['id'],r['dato1'],r['dato2'],r['dato3'],r['dato4'],r['dato5'],r['dato6'],r['dato7'],r['dato8'],r['dato9'], r['dato10'],r['dato11'],r['dato12'],r['dato13'],r['dato14'],r['dato15'],r['dato16']r['hab1'],r['hab2'],r['hab3'],r['hab4'],r['hab5'],r['hab6'],r['hab7'],r['hab8'],r['hab9'],r['hab10'],r['hab11'],r['hab12'],r['hab13'],r['hab14'],r['hab15'],r['hab16'],r['hab17'],r['hab18'],r['hab19'],r['hab20'],r['hab21'],r['hab22'],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''],r[''] )
    r = AsDict(guest)
    self.SendJson(r)


class InsertHandler(RestHandler):

  def post(self):
    r = json.loads(self.request.body)
    guest = model.InsertGuest(r['TIPODEPERSONAJE'], r['nombredepersonaje'],r['nombredejugador'], r['Altura'],r['peso'], r['Sexo'],r['Edad'], r['descripcionfisica'])
    r = AsDict(guest)
    self.SendJson(r)


class DeleteHandler(RestHandler):

  def post(self):
    r = json.loads(self.request.body)
    model.DeleteGuest(r['id'])


APP = webapp2.WSGIApplication([
    ('/rest/query', QueryHandler),
    ('/rest/insert', InsertHandler),
    ('/rest/delete', DeleteHandler),
    ('/rest/update', UpdateHandler),
], debug=True)


