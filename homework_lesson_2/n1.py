from collections import namedtuple

Point = namedtuple("Point",["id", "username", "email", "is_active"])

all = [
    Point(1,"alibek","aliyev242@gmail.com",True),
    Point(2,"bilol12","billayev12i@gmail.com",False),
    Point(3,"tom&jerry_uz","jorayevjerri12@gmail.com",True)
]

for x in all:
    print(f"username: {x.username}, email: {x.email}")