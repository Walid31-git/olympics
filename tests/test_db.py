from olympics import db


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 100

#Fonctions test qui echoue si on trouve moins de 50 medailles
def test_medals():
    rows = db.get_medals()
    assert len(rows) > 50
    rows = db.get_medals(1)
    assert len(rows) == 1
    
#j'ai changer de fonction car l'autre etait compliquer a implementer a 100%
   
def test_teams():
    rows = db.get_teams()
    assert len(rows) > 100
    rows = db.get_teams(1)
    assert len(rows) == 1

#Fonctions test qui echoue si on trouve moins de 50 athletes
def test_athletes():
    rows = db.get_athletes()
    assert len(rows) > 50
    rows = db.get_athletes(1)
    assert len(rows) == 1
    
