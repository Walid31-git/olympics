from io import StringIO

from olympics import cli


def test_top_countries():
    string = StringIO()
    cli.top_countries(file=string)
    text = string.getvalue()
    assert 'Top' in text

def test_top_athletes():
    string = StringIO()
    cli.top_athletes(file=string)
    text = string.getvalue()
    assert 'Top' in text

def test_top_disciplines():
    string = StringIO()
    cli.top_disciplines(file=string)
    text = string.getvalue()
    assert 'Top' in text

def test_top_teams():
    string = StringIO()
    cli.top_teams(file=string)
    text = string.getvalue()
    assert 'Top' in text
