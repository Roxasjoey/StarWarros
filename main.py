import json
import webapp2
import time

import model


def AsDict(guest):
  return {'id': guest.key.id(), 'TIPODEPERSONAJE': guest.TIPODEPERSONAJE, 'nombredepersonaje': guest.nombredepersonaje,
  'nombredejugador': guest.nombredejugador, 'Altura': guest.Altura, 'peso': guest.peso, 'Sexo': guest.Sexo,
   'Edad': guest.Edad, 'descripcionfisica': guest.descripcionfisica}


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
    guest = model.UpdateGuest(r['id'],r['TIPODEPERSONAJE'], r['nombredepersonaje'],r['nombredejugador'], r['Altura'],r['peso'], r['Sexo'],r['Edad'], r['descripcionfisica'])
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


