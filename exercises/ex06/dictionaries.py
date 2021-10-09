"""Practice with dictionaries."""

__author__ = "730470448"




def invert(d) -> dict[str,str]:
    inverted: dict[str,str]
    inverted = dict()
    for i in d:
        if(d[i] in inverted):
            raise KeyError("Duplicate Keys")
        inverted[d[i]] = i
    return inverted

print(invert({'a' : 'A', 'b' : 'a'}))


def favorite_color(color_dict) -> str:
    count: int = 0
    color_set: dict[str, int]
    color_set = dict()
    color_set["Blank"] = 0
    greatest: str = "Blank"
    for i in color_dict:
        for j in color_dict:
            if(color_dict[j] == color_dict[i]):
                count += 1
        color_set[color_dict[i]] = count
        count = 0
    for y in color_set:
        if(color_set[greatest] < color_set[y]):
            greatest = y
    return greatest


def count(l) -> dict[str,int]:
    d: dict[str, int]
    d = dict()
    for i in l:
        if(i in d):
            d[i] += 1
        else:
            d[i] =0
    return d
    
print(favorite_color({"Marc": "yellow","Jane" : "yellow","Bob":"yellow", "John" : "green", "Tom": "green", "Bill":"green", "Ezri": "blue", "Kris": "blue","Gary":"blue"}))
print(favorite_color({"Marc":"blue"}))
print(count([1,2,3,4,4,4,2,1,4]))
# Define your functions below