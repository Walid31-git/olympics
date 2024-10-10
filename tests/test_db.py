from olympics import db


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 100

#Fonctions test qui echoue si on trouve moins de 50 medailles
def test_medals():
    rows = db.get_medals()
    assert len(rows) > 50
 
#Fonctions test qui echoue si on trouve moins de 10 des meilleurs collectifs   
def test_top_collective():
    rows = db.get_top_collective()
    assert len(rows) >= 10

#Fonctions test qui echoue si on trouve moins de 50 athletes
def test_athletes():
    rows = db.get_athletes()
    assert len(rows) > 50
    
