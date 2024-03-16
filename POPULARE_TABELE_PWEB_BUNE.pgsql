
--the dark knight

insert into Actori(actorID,nume,prenume,nationalitate,dataNastere)
VALUES(1,'Christian','Bale','British','1974-01-30'
);

insert into Actori(actorID,nume,prenume,nationalitate,dataNastere)
VALUES(2,'Heath','Ladger','Australian','1979-04-04'
);

insert into Actori(actorID,nume,prenume,nationalitate,dataNastere)
VALUES(3,'Aaron','Eckhart','American','1968-03-12'
);

--lord of the rings 

insert into Actori(actorID,nume,prenume,nationalitate,dataNastere)
VALUES(4,'Elijah','Wood','American','1981-01-28'
);

insert into Actori(actorID,nume,prenume,nationalitate,dataNastere)
VALUES(5,'Viggo','Mortensen','American','1958-10-20'
);

insert into Actori(actorID,nume,prenume,nationalitate,dataNastere)
VALUES(6,'Ian','McKellen','English','1939-05-25'
);

insert into Actori(actorID,nume,prenume,nationalitate,dataNastere)
VALUES(7,'Orlando','Bloom','English','1977-01-13'
);



select * from Actori;

insert into Genuri(genID,numeGen) VALUES( 1, 'Actiune');
insert into Genuri(genID,numeGen) VALUES( 2, 'Drama');
insert into Genuri(genID,numeGen) VALUES( 3, 'Crima');
insert into Genuri(genID,numeGen) VALUES( 4, 'Horror');
insert into Genuri(genID,numeGen) VALUES( 5, 'Romanta');
insert into Genuri(genID,numeGen) VALUES( 6, 'Thriller');
insert into Genuri(genID,numeGen) VALUES( 7, 'Mister');
insert into Genuri(genID,numeGen) VALUES( 8, 'Animatie');
insert into Genuri(genID,numeGen) VALUES( 9, 'Aventura');
insert into Genuri(genID,numeGen) VALUES( 10, 'Fantasy');
insert into Genuri(genID,numeGen) VALUES( 11, 'SF');
insert into Genuri(genID,numeGen) VALUES( 12, 'Biografic');
insert into Genuri(genID,numeGen) VALUES( 13, 'Istoric');
insert into Genuri(genID,numeGen) VALUES( 14, 'Politist');

select * from Genuri;

insert into Scenariu(scenariuid,nume)
VALUES(1,'The Dark Knight');

insert into Scenariu(scenariuid,nume)
VALUES(2,'The Lord of the Rings: The Fellowship of the Ring');

insert into Scenariu(scenariuid,nume)
VALUES(3,'The Lord of the Rings: The Two Towers');

insert into Scenariu(scenariuID,nume)
VALUES(77,'test');

select * from Scenariu;


insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (1,'Jonathan', 'Nolan',46);

insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (2,'Christopher', 'Nolan',52);

insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (3,'David S.',' Goyer',57);

--lord of the rings 
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (4,'J.R.R.','Tolkien',81);
/*
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (4,'J.R.R.','Tolkien',81);
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (4,'J.R.R.','Tolkien',81);
*/
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (5,'Fran','Walsh',64);
/*
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (5,'Fran','Walsh',64);
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (5,'Fran','Walsh',64);
*/
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (6,'Philippa','Boyens',61);
/*
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (6,'Philippa','Boyens',61);
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (6,'Philippa','Boyens',61);
*/
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (7,'Peter','Jackson',61);
/*
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (7,'Peter','Jackson',61);
insert into Scriitori(scriitorID,nume,prenume,varsta)
VALUES (7,'Peter','Jackson',61);
*/

select * from Scriitori;


insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (1,1);

insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (2,1);

insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (3,1);

/*lord of the rings */

insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (4,2);
insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (4,3);
insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (4,4);

insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (5,2);
insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (5,3);
insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (5,4);

insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (6,2);
insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (6,3);
insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (6,4);

insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (7,2);
insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (7,3);
insert into scriitoriscenariu(scriitorid,scenariuid)
VALUES (7,4);

select * from scriitoriscenariu ;

insert into Director(directorID,nume,prenume,varsta)
VALUES(1,'Christopher', 'Nolan',52);

insert into Director(directorID,nume,prenume,varsta)
VALUES(2,'Peter', 'Jackson',61);

select * from Director;

insert into Filme (filmID,directorid1,genID,actorID,scenariuid1,titlu,durata,
				   descriere,anaparitie,categorievarsta)
VALUES(1,1,1,1,1,'The Dark Knight','2h32min','Când amenințarea cunoscută sub numele de Joker face ravagii și haos asupra oamenilor din Gotham, Batman trebuie să accepte unul dintre cele mai mari teste psihologice și fizice ale capacității sale de a lupta împotriva nedreptății.',
	   2008,'PG-13'

);

--lord of the rings
insert into Filme (filmID,directorid1,genID,actorID,scenariuid1,titlu,durata,
				   descriere,anaparitie,categorievarsta)
VALUES(2,2,1,4,2,'The Lord of the Rings: The Fellowship of the Ring','2h58min','Un hobbit blând din Shire și opt însoțitori au pornit într-o călătorie pentru a distruge puternicul Inel Unic și a salva Pământul de Mijloc de Lordul Întunecat Sauron.',
	   2001,'PG-13'

);

insert into Filme (filmID,directorid1,genID,actorID,scenariuid1,titlu,durata,
				   descriere,anaparitie,categorievarsta)
VALUES(3,2,1,4,3,'The Lord of the Rings: The Two Towers','2h59min','În timp ce Frodo și Sam se apropie tot mai mult de Mordor cu ajutorul vicleanului Gollum, părtășia divizată ia poziție împotriva noului aliat al lui Sauron, Saruman, și a hoardelor sale din Isengard.',
	   2002,'PG-13'

);

insert into Filme (filmID,directorid1,genID,actorID,scenariuid1,titlu,durata,
				   descriere,anaparitie,categorievarsta)
VALUES(4,2,1,4,4,'The Lord of the Rings: The Return of the King','3h21min','Gandalf și Aragorn conduc Lumea Oamenilor împotriva armatei lui Sauron pentru a-și atrage privirea de la Frodo și Sam în timp ce se apropie de Muntele Doom cu Inelul Unic.',
	   2003,'PG-13'

);

select * from Filme;

insert into FilmeGenuri(filmID,genID) VALUES(1,1);
insert into FilmeGenuri(filmID,genID) VALUES(1,2);
insert into FilmeGenuri(filmID,genID) VALUES(1,3);

--the lord of the rings 
insert into FilmeGenuri(filmID,genID) VALUES(2,1);
insert into FilmeGenuri(filmID,genID) VALUES(2,2);
insert into FilmeGenuri(filmID,genID) VALUES(2,9);

insert into FilmeGenuri(filmID,genID) VALUES(3,1);
insert into FilmeGenuri(filmID,genID) VALUES(3,2);
insert into FilmeGenuri(filmID,genID) VALUES(3,9);

insert into FilmeGenuri(filmID,genID) VALUES(4,1);
insert into FilmeGenuri(filmID,genID) VALUES(4,2);
insert into FilmeGenuri(filmID,genID) VALUES(4,9);

select * from FilmeGenuri;
--the dark knight
insert into FilmeActori(filmID,actorID) VALUES (1,1);
insert into FilmeActori(filmID,actorID) VALUES (1,2);
insert into FilmeActori(filmID,actorID) VALUES (1,3);
--the lord of the rings  
insert into FilmeActori(filmID,actorID) VALUES (2,4);
insert into FilmeActori(filmID,actorID) VALUES (2,5);
insert into FilmeActori(filmID,actorID) VALUES (2,6);
insert into FilmeActori(filmID,actorID) VALUES (2,7);

insert into FilmeActori(filmID,actorID) VALUES (3,4);
insert into FilmeActori(filmID,actorID) VALUES (3,5);
insert into FilmeActori(filmID,actorID) VALUES (3,6);
insert into FilmeActori(filmID,actorID) VALUES (3,7);

insert into FilmeActori(filmID,actorID) VALUES (4,4);
insert into FilmeActori(filmID,actorID) VALUES (4,5);
insert into FilmeActori(filmID,actorID) VALUES (4,6);
insert into FilmeActori(filmID,actorID) VALUES (4,7);

select * from FilmeActori;

insert into Seriale(serialid,titlu,numar_episoade,descriere,actori,
					ani_desfasurare,statusul,scriitori,director,genuri,categorie_varsta)
VALUES(1,'Dirk Gently`s Holistic Detective Agency','18 episoade - 2 sezoane', 'Se concentrează pe detectivul holistic titular care investighează cazurile care implică supranaturalul. Bazat pe seria de romane „Agenția de detectivi holistici a lui Dirk Gently”, scrisă de Douglas Adams și publicată de Simon și Schuster în 1987.',
'Elijah Wood, Samuel Barnett, Hannah Marks', 2016,'Încheiat','Douglas Adams, Max Landis, Sinead Daly', 'Michael Patrick Jann','Actiune, Aventura, Comedie', 'R');

insert into Seriale(serialid,titlu,numar_episoade,descriere,actori,
					ani_desfasurare,statusul,scriitori,director,genuri,categorie_varsta)
VALUES(  2,
		'Angels in America',
		'6 episoade - 1 sezon',
		'Mai multe persoane disparate, dar conectate, trec prin criza SIDA la mijlocul anilor 1980.',
		'Al Pacino, Meryl Streep, Emma Thompson', 
		2003,
		'Încheiat',
		'Tony Kushner',
		'Mike Nichols',
		'Drama, Fantasy, Romanta', 
		'PG');

insert into Seriale(serialid,titlu,numar_episoade,descriere,actori,
					ani_desfasurare,statusul,scriitori,director,genuri,categorie_varsta)
VALUES(  3,
		'Bosom Buddies',
		'37 episoade - 2 sezoane ',
		'Doi tineri singuri trebuie să se deghizeze în femei pentru a locui în singurul apartament pe care și-l permit.',
		'Tom Hanks, Peter Scolari, Donna Dixon', 
		1980,
		'Încheiat',
		'Chris Thompson, Robert L. Boyett, Thomas L. Miller',
		'Joel Zwick',
		'Comedie', 
		'PG');

insert into Seriale(serialid,titlu,numar_episoade,descriere,actori,
					ani_desfasurare,statusul,scriitori,director,genuri,categorie_varsta)
VALUES(  4,
		'Young Rock',
		'37 episoade - 3 sezoane',
		'O privire asupra anilor formativi ai superstarului Dwayne „The Rock” Johnson, pe măsură ce trece prin viață.',
		'Dwayne Johnson, Joseph Lee Anderson, Stacey Leilua', 
		2021,
		'În desfășurare',
		'Jeff Chiang, Nahnatchka Khan',
		'Jeffrey Walker',
		'Comedie', 
		'PG');

insert into Seriale(serialid,titlu,numar_episoade,descriere,actori,
					ani_desfasurare,statusul,scriitori,director,genuri,categorie_varsta)
VALUES(  5,
		'Ballers',
		'47 episoade- 5 sezoane',
		'O serie centrată în jurul unui grup de jucători de fotbal și a familiilor, prietenilor și managerilor acestora.',
		'Dwayne Johnson, John David Washington, Donovan W. Carter', 
		2015,
		'Încheiat',
		'Stephen Levinson, Rashard Mendenhall',
		'Julian Farino',
		'Comedie, Drama', 
		'PG');

insert into Seriale(serialid,titlu,numar_episoade,descriere,actori,
					ani_desfasurare,statusul,scriitori,director,genuri,categorie_varsta)
VALUES(  6,
		'The Defenders',
		'8 episoade - 1 sezon',
		'Amplasat la câteva luni după evenimentele celui de-al doilea sezon din Daredevil și la o lună după evenimentele din Iron Fist, vigilenții Daredevil, Jessica Jones, Luke Cage și Iron Fist fac echipă în New York City pentru a lupta cu un inamic comun: The Hand.',
		'Sigourney Weaver, Charlie Cox, Krysten Ritter', 
		2017,
		'Încheiat',
		'Brian Michael Bendis, Douglas Petrie, Lauren Schmidt Hissrich',
		'S.J. Clarkson',
		'Actiune, Aventura, Crima', 
		'PG');

insert into Seriale(serialid,titlu,numar_episoade,descriere,actori,
					ani_desfasurare,statusul,scriitori,director,genuri,categorie_varsta)
VALUES(  7,
		'See',
		'24 episoade - 3 sezoane',
		'Departe într-un viitor distopic, rasa umană și-a pierdut simțul vederii, iar societatea a trebuit să găsească noi modalități de a interacționa, de a construi, de a vâna și de a supraviețui. Toate acestea sunt contestate atunci când un set de gemeni se nasc cu vedere.',
		'Dave Bautista, Jason Momoa, Sylvia Hoeks', 
		2019,
		'Încheiat',
		'Steven Knight, Hadi Nicholas Deeb, Kirsa Rein',
		'Anders Engström',
		'Actiune, Drama, SF', 
		'PG');
insert into Seriale(serialid,titlu,numar_episoade,descriere,actori,
					ani_desfasurare,statusul,scriitori,director,genuri,categorie_varsta)
VALUES(  8,
		'Chillers',
		'12 episoade - 1 sezon',
		'Pe baza povestirilor scurte ale lui Patricia Highsmith: afișând o atmosferă sinistră, explorând cele mai întunecate adâncimi ale naturii umane.',
		'Anthony Perkins, Doug Rollins, Assumpta Serna', 
		1990,
		'Încheiat',
		'Patricia Highsmith, Andrew Hislop, Marc Princi',
		'Mai Zetterling',
		'Actiune, Drama, Horror', 
		'PG');

insert into Seriale(serialid,titlu,numar_episoade,descriere,actori,
					ani_desfasurare,statusul,scriitori,director,genuri,categorie_varsta)
VALUES(  9,
		'Daybreak',
		'10 episoade - 1 sezon',
		'Josh, proscris din liceu, își caută iubita dispărută în Glendale post-apocaliptic. Lui i se alătură un grup de neadaptați Angelica și fostul său bătăuș Wesley. Pe drum se vor confrunta cu multe lucruri ciudate.',
		'Matthew Broderick, Colin Ford, Alyvia Alyn Lind', 
		2019,
		'Încheiat',
		'Aron Eli Coleite, Ira Madison III, Brad Peyton',
		'Michael Patrick Jann',
		'Actiune, Aventura, Comedie', 
		'PG');

insert into Seriale(serialid,titlu,numar_episoade,descriere,actori,
					ani_desfasurare,statusul,scriitori,director,genuri,categorie_varsta)
VALUES(  10,
		'The Get Down',
		'11 episoade - 1 sezon',
		'Un grup de adolescenți dezorganizați hoinăresc în voie pe străzile din Bronx, la sfârșitul anilor `70.',
		'Shameik Moore, Justice Smith, Herizen F. Guardiola', 
		2016,
		'Încheiat',
		'Stephen Adly Guirgis, Baz Luhrmann, Jacqui Rivera',
		'Ed Bianchi',
		'Drama', 
		'PG');

select * from seriale 

