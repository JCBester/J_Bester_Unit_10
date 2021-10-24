import pytest
import requests
resp_data = requests.get(
        "https://api.duckduckgo.com/?q=presidents+of+the+united+states" +
        "&format=json"
).json()
def is_in_resp_data(name):
    for i in resp_data["RelatedTopics"]:
        if name in i["Result"]:
            return True
    return False
@pytest.mark.parametrize("president", [
    "Washington",  # George
    "Adams",  # John
    "Jefferson",  # Thos.
    "Madison",  # James
    "Monroe",  # James
    # Adams, John Quincy
    "Jackson",  # Andrew
    "Van Buren",  # Martin
    "Harrison",  # Wm. Henry
    "Tyler",  # John
    "Polk",  # James K.
    "Taylor",  # Zachary
    "Fillmore",  # Millard
    "Pierce",  # Franklin
    "Buchanan",  # James
    "Lincoln",  # Abraham
    "Johnson",  # Andrew
    "Grant",  # Ulysses S.
    "Hayes",  # Rutherford B.
    "Arthur",  # Chester A.
    "Cleveland",  # Grover
    "Harrison",  # Benjamin
    # Cleveland, Grover (2nd term)
    "McKinley",  # Wm.
    "Roosevelt",  # Theodore
    "Taft",  # Wm. Howard
    "Wilson",  # Woodrow
    "Harding",  # Warren G.
    "Coolidge",  # Calvin
    "Hoover",  # Herbert
    # Roosevelt, Franklin D.
    "Truman",  # Harry S.
    "Eisenhower",  # Dwight D.
    "Kennedy",  # John F.
    # Johnson, Lyndon B.
    "Nixon",  # Richard M.
    "Ford",  # Gerald R.
    "Carter",  # James
    "Reagan",  # Ronald
    "Bush",  # George H. W.
    "Clinton",  # Wm. J.
    # Bush, George W.
    "Obama",  # Barack
    "Trump",  # Donald
    "Biden",  # Jos. R., Jr.
])
def test_presidents(president):
    assert(is_in_resp_data(president))
