from apps.dojo_ninjas_app.models import Dojo, Ninja

future = Dojo.objects.create(name="Future", city="Berkeley", state="CA")

padma = Ninja.objects.create(first_name="Padma", last_name="Patil", dojo=future)

bagend = Dojo.objects.create(name="Bag End", city="the Shire", state="ME")
lonely_mtn = Dojo.objects.create(name="Lonely Mountain", city="There", state="ME")
mt_doom = Dojo.objects.create(name="Mount Doom", city="Mordor", state="ME")



>>> bagend = Dojo.objects.create(name="Bag End", city="the Shire", state="ME")
>>> lonely_mtn = Dojo.objects.create(name="Lonely Mountain", city="There", state="ME")
>>> mt_doom = Dojo.objects.create(name="Mount Doom", city="Mordor", state="ME")
>>> all_dojos = Dojo.objects.all()
>>> all_dojos
<QuerySet [<Dojo object: Future, city: Berkeley, state = CA, id = 1>, <Dojo object: Bag End, city: the Shire, state = ME, id = 2>, <Dojo object: Lonely Mountain, city: There, state = ME, id = 3>, <Dojo object: Mount Doom, city: Mordor, state = ME, id = 4>]>
>>> bagend.delete()
(1, {'dojo_ninjas_app.Ninja': 0, 'dojo_ninjas_app.Dojo': 1})
>>> all_dojos = Dojo.objects.all()
>>> all_dojos
<QuerySet [<Dojo object: Future, city: Berkeley, state = CA, id = 1>, <Dojo object: Lonely Mountain, city: There, state = ME, id = 3>, <Dojo object: Mount Doom, city: Mordor, state = ME, id = 4>]>
>>> lonely_mtn.delete()
(1, {'dojo_ninjas_app.Ninja': 0, 'dojo_ninjas_app.Dojo': 1})
>>> mt_doom.delete()
(1, {'dojo_ninjas_app.Ninja': 0, 'dojo_ninjas_app.Dojo': 1})
>>> all_dojos = Dojo.objects.all()
>>> all_dojos 
<QuerySet [<Dojo object: Future, city: Berkeley, state = CA, id = 1>]>



past = Dojo.objects.create(name="Past", city="Emeryville", state="CA")
present = Dojo.objects.create(name="Present", city="Oakland", state="CA")


herm = Ninja.objects.create(first_name="Hermione", last_name="Granger", dojo=future)
bob = Ninja.objects.create(first_name="bob", last_name="Granger", dojo=future)

>>> future_ninjas = Ninja.objects.filter(dojo=future)
>>> future_ninjas
<QuerySet [<User object: Padma Patil(Future)>, <User object: Hermione Granger(Future)>, <User object: bob Granger(Future)>]>



harry = Ninja.objects.create(first_name="Harry", last_name="Potter", dojo=past)
ron = Ninja.objects.create(first_name="Ron", last_name="Weasely", dojo=past)
theo = Ninja.objects.create(first_name="Theodore", last_name="Roosevelt", dojo=past)

>>> theo = Ninja.objects.create(first_name="Theodore", last_name="Roosevelt", dojo=past)
>>> past_ninjas = Ninja.objects.filter(dojo=past)
>>> past_ninjas 
<QuerySet [<User object: Harry Potter(Past)>, <User object: Ron Weasely(Past)>, <User object: Theodore Roosevelt(Past)>]>
>>> 


suzanne = Ninja.objects.create(first_name="Suzanne", last_name="To My left", dojo=present)
keon = Ninja.objects.create(first_name="Keon", last_name="To My right", dojo=present)
me = Ninja.objects.create(first_name="Kat", last_name="Here and Now", dojo=present)

>>> present_ninjas = Ninja.objects.filter(dojo=present)
>>> present_ninjas
<QuerySet [<User object: Suzanne To My left(Present)>, <User object: Keon To My right(Present)>, <User object: Kat Here and Now(Present)>]>

>>> first_dojo = Dojo.objects.first()
>>> first_dojo
<Dojo object: Future, city: Berkeley, state = CA, id = 1>
>>> ninjas_of_the_first_dojo = Ninja.objects.filter(dojo=first_dojo)
>>> ninjas_of_the_first_dojo
<QuerySet [<User object: Padma Patil(Future)>, <User object: Padma Patil(Future)>, <User object: Hermione Granger(Future)>, <User object: bob Granger(Future)>]>
>>> 

>>> ninjas_last_dojo = Ninja.objects.filter(dojo=Dojo.objects.last())
>>> ninjas_last_dojo
<QuerySet [<User object: Suzanne To My left(Present)>, <User object: Keon To My right(Present)>, <User object: Kat Here and Now(Present)>]>
>>> 


>>> dojo_of_last_ninja = Ninja.objects.last().dojo
>>> dojo_of_last_ninja
<Dojo object: Present, city: Oakland, state = CA, id = 6>
>>> 


post_modern = Dojo.objects.create(name="Truth", city="The Mind", state="Of being", desc="distant future" )