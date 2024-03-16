insert into Actori(actorID,nume,prenume,nationalitate,dataNastere)
VALUES(1,'Christian','Bale','British','1974-01-30'
);

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
insert into Genuri(genID,numeGen) VALUES( 14, 'Istoric');
insert into Genuri(genID,numeGen) VALUES( 15, 'Politist');

select * from Genuri

insert into Scenariu(scenariuID,nume)
VALUES(1,'The Dark Knight');

select * from Scenariu

insert into Scriitori(scriitorID,scenariuID,nume,prenume,varsta)
VALUES (1,1,'Jonathan', 'Nolan',46);

insert into Scriitori(scriitorID,scenariuID,nume,prenume,varsta)
VALUES (2,1,'Christopher', 'Nolan',52);

insert into Scriitori(scriitorID,scenariuID,nume,prenume,varsta)
VALUES (3,1,'David S.',' Goyer',57);

insert into Director(directorID,nume,prenume,varsta)
VALUES(1,'Christopher', 'Nolan',52);


insert into Filme (filmID,directorID,genID,actorID,scenariuID,titlu,durata,
				   descriere,an_aparitie,categorie_varsta)
VALUES(1,1,1,1,1,'The Dark Knight','2h32min','Când amenințarea cunoscută sub numele de Joker face ravagii și haos asupra oamenilor din Gotham, Batman trebuie să accepte unul dintre cele mai mari teste psihologice și fizice ale capacității sale de a lupta împotriva nedreptății.',
	   2008,'PG-13'

);
select * from Filme

insert into FilmeGenuri(filmID,genID) VALUES(1,1);
insert into FilmeGenuri(filmID,genID) VALUES(1,2);
insert into FilmeGenuri(filmID,genID) VALUES(1,3);

select * from FilmeGenuri

insert into FilmeActori(filmID,actorID) VALUES (1,1);

select * from FilmeActori