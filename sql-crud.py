from sqlalchemy import (
    create_engine, Column, Integer, String, MetaData
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer)


class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer)
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    

class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)
    

class Favorite_Places(base):
    __tablename__ = "Places"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    interesting_for = Column(String)
    distance = Column(String)
    time_to_dest = Column(String)
    

Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)


ada_lovelace = Programmer(
    first_name ="Ada",
    last_name ="Lovelace",
    gender ="F",
    nationality ="British",
    famous_for ="First Programmer"
)

alan_turing = Programmer(
    first_name ="Alan",
    last_name ="Turing",
    gender ="M",
    nationality ="British",
    famous_for ="Modern Computing"
)

grace_hopper = Programmer(
    first_name ="Grace",
    last_name ="Hopper",
    gender ="F",
    nationality ="American",
    famous_for ="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name ="Margaret",
    last_name ="Hamilton",
    gender ="F",
    nationality ="American",
    famous_for ="Apollo 11"
)

bill_gates = Programmer(
    first_name ="Bill",
    last_name ="Gates",
    gender ="M",
    nationality ="American",
    famous_for ="Microsoft"
)

tim_berners_lee = Programmer(
    first_name ="Tim",
    last_name ="Berners-Lee",
    gender ="M",
    nationality ="British",
    famous_for ="Internet"
)

gena_grig = Programmer(
    first_name ="Gena",
    last_name ="Grig",
    gender ="M",
    nationality ="Russian",
    famous_for ="Full Stack Developer"
)

# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(gena_grig)

# session.commit()

sweden_umea = Favorite_Places(
    country="Sweden",
    city="Umea",
    interesting_for="My hometown",
    distance="0",
    time_to_dest="0"
)

latvia_riga = Favorite_Places(
    country="Latvia",
    city="Riga",
    interesting_for="My first hometown",
    distance="2700",
    time_to_dest="2 hours"
)

czech_praga = Favorite_Places(
    country="Czech Republic",
    city="Prague",
    interesting_for="Honeymoon",
    distance="4700",
    time_to_dest="4 hours"
)

# session.add(sweden_umea)
# session.add(latvia_riga)
# session.add(czech_praga)

# session.commit()

# programmer = session.query(Programmer).filter_by(id=9).first()
# programmer.famous_for = "Senior Full Stack Developer in 1 year"

# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#         session.commit()    

# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")


# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )
    
places = session.query(Favorite_Places)
for place in places:
    print(
        place.id,
        place.country,
        place.city,
        place.interesting_for,
        place.distance,
        place.time_to_dest,
        sep=" | "
    )
