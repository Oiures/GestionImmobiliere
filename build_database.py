import sqlite3

conn = sqlite3.connect('ImmobCatalogue.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved

# Create table - Users
c.execute('''CREATE TABLE Users
             ([user_id] INTEGER PRIMARY KEY,
             [user_lname] text, 
             [user_fname] text)''')

# Create table - Goods
c.execute('''CREATE TABLE Goods
             ([good_id] INTEGER PRIMARY KEY,
             [good_name] text, 
             [good_description] text,
              [good_city] text, 
              [good_type] text, 
              [good_rooms] integer, 
              [good_caracteristique] text,
              [user_id] integer,
              CONSTRAINT fk_users FOREIGN KEY (user_id) REFERENCES Users(user_id))''')

# Insert into table - Users
c.execute('''INSERT INTO Users (user_id, user_lname, user_fname) VALUES
    (0, 'Parra', 'Morgan'),
    (1, 'Rougerie', 'Aurelien'),
    (2, 'James', 'Brock'),
    (3, 'Lopez', 'Camille')''')

# Insert into table - Users
c.execute('''INSERT INTO Goods (good_id, good_name, good_description, good_city, good_type, good_rooms, 
                                                                                good_caracteristique, user_id) VALUES
    (0, 'Bel appart', 'Un bel appartement dans le 6 ème', 'Lyon', 'Appartement', 5, '5 pieces en carton', 0),
    (1, 'Petite maison', 'Une belle petite maison dans le 2nd', 'Lyon', 'Maison', 2, '2 pieces en allumium', 0),
    (2, 'Tente confortable', 'Tente à louer dans le champs de René', 'Issoire', 'Tente', 1, '1 pièce, c est une tente', 1),
    (3, 'Grande maison', 'Une belle grande maison', 'Paris', 'Maison', 4, '4 pièce lumineuse,', 2),
    (4, 'Le chateau de l ancetre', 'Un grand chateau ayant appartenu à l ancetre', 'Paris', 'Chateau', 50, '50 pièces car c est un chateau', 2)''')


conn.commit()

# Note that the syntax to create new tables should only be used once in the code (unless you dropped the table/s at the end of the code).
# The [generated_id] column is used to set an auto-increment ID for each record
# When creating a new table, you can add both the field names as well as the field formats (e.g., Text)