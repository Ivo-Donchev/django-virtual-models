from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    DecimalField,
    CASCADE
)



class Club(Model):
    name = CharField(max_length=256, unique=True)



class Party(Model):
    name = CharField(max_length=256, unique=True)
    club = ForeignKey(Club, related_name='parties', on_delete=CASCADE)


class Client(Model):
    full_name = CharField(max_length=256)
    age = IntegerField()


class ClientToParty(Model):
    client = ForeignKey(Client, related_name='client_to_parties', on_delete=CASCADE)
    party = ForeignKey(Party, related_name='client_to_parties', on_delete=CASCADE)

    bill = DecimalField(max_digits=10, decimal_places=2)
