try:
    from . import BASE, SESSION
except ImportError:
    raise AttributeError

from sqlalchemy import BigInteger, Column, Numeric, String, UnicodeText


class Joinpoke(BASE):
    __tablename__ = "pokeautocatch"
    chat_id = Column(String(14), primary_key=True)
    previous_poke = Column(BigInteger)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)

    def __init__(self, chat_id, previous_poke, reply, f_mesg_id):
        self.chat_id = str(chat_id)
        self.previous_poke = previous_poke
        self.reply = reply
        self.f_mesg_id = f_mesg_id


Joinpoke.__table__.create(checkfirst=True)

def get_poke(chat_id):
    try:
        return SESSION.query(Joinpoke).get(str(chat_id))
    finally:
        SESSION.close()
def getpoke(chat_id):
    try:
        return SESSION.query(Joinpoke).get(str(chat_id))
    finally:
        SESSION.close()

def get_current_poke_settings(chat_id):
    try:
        return (
            SESSION.query(Joinpoke).filter(Joinpoke.chat_id == str(chat_id)).one()
        )
    except BaseException:
        return None
    finally:
        SESSION.close()
def getcurrent_poke_settings(chat_id):
    try:
        return (
            SESSION.query(Joinpoke).filter(Joinpoke.chat_id == str(chat_id)).one()
        )
    except BaseException:
        return None
    finally:
        SESSION.close()
def add_poke_setting(chat_id, previous_poke, reply, f_mesg_id):
    to_check = getpoke(chat_id)
    if not to_check:
        adder = Joinpoke(chat_id, previous_poke, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(Joinpoke).get(str(chat_id))
    SESSION.delete(rem)
    SESSION.commit()
    adder = Joinpoke(chat_id, previous_poke, reply, f_mesg_id)
    SESSION.commit()
    return False

def addpoke_setting(chat_id, previous_poke, reply, f_mesg_id):
    to_check = getpoke(chat_id)
    if not to_check:
        adder = Joinpoke(chat_id, previous_poke, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(Joinpoke).get(str(chat_id))
    SESSION.delete(rem)
    SESSION.commit()
    adder = Joinpoke(chat_id, previous_poke, reply, f_mesg_id)
    SESSION.commit()
    return False

def rm_poke_setting(chat_id):
    try:
        rem = SESSION.query(Joinpoke).get(str(chat_id))
        if rem:
            SESSION.delete(rem)
            SESSION.commit()
            return True
    except BaseException:
        return False

def rmpoke_setting(chat_id):
    try:
        rem = SESSION.query(Joinpoke).get(str(chat_id))
        if rem:
            SESSION.delete(rem)
            SESSION.commit()
            return True
    except BaseException:
        return False

def update_previous_poke(chat_id, previous_poke):
    row = SESSION.query(Joinpoke).get(str(chat_id))
    row.previous_poke = previous_poke
    SESSION.commit()
def updateprevious_poke(chat_id, previous_poke):
    row = SESSION.query(Joinpoke).get(str(chat_id))
    row.previous_poke = previous_poke
    SESSION.commit()
