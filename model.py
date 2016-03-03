from google.appengine.ext import ndb

class Guest(ndb.Model):
  TIPODEPERSONAJE = ndb.StringProperty()
  nombredepersonaje = ndb.StringProperty()
  nombredejugador= ndb.StringProperty()
  Altura= ndb.StringProperty()
  peso= ndb.StringProperty()
  Sexo= ndb.StringProperty()
  Edad= ndb.StringProperty()
  descripcionfisica= ndb.StringProperty()
def AllGuests():
  return Guest.query()

def UpdateGuest(id, TIPODEPERSONAJE, nombredepersonaje, nombredejugador, Altura, peso, Sexo, Edad, descripcionfisica ):
  guest = Guest(id=id, TIPODEPERSONAJE=TIPODEPERSONAJE, nombredepersonaje=nombredepersonaje, nombredejugador=nombredejugador, Altura=Altura, peso=peso, Sexo=Sexo, Edad=Edad, descripcionfisica=descripcionfisica)
  guest.put()
  return guest


def InsertGuest(TIPODEPERSONAJE, nombredepersonaje, nombredejugador, Altura, peso, Sexo, Edad, descripcionfisica ):
  guest = Guest(TIPODEPERSONAJE=TIPODEPERSONAJE, nombredepersonaje=nombredepersonaje, nombredejugador=nombredejugador, Altura=Altura, peso=peso, Sexo=Sexo, Edad=Edad, descripcionfisica=descripcionfisica)
  guest.put()
  return guest


def DeleteGuest(id):
  key = ndb.Key(Guest, id)
  key.delete()
