create table Actori(
	actorID int,
	nume varchar(500),
	prenume varchar(500),
	nationalitate varchar(500),
	dataNastere date,
	primary key(actorID)
);

select * from Actori

create table Genuri(
	genID int,
	numeGen varchar(500),
	primary key(genID)
);

select * from Genuri

create table Scenariu(
	scenariuID int,
	nume varchar(500),
	
	primary key (scenariuID)
);

select * from Scenariu

create table Scriitori(
   
	scriitorID int,
	scenariuID int,
	nume varchar(500),
	prenume varchar(500),
	varsta int,
	primary key(scriitorID),
	CONSTRAINT fk_scenariu
	   FOREIGN KEY(scenariuID)
	     REFERENCES Scenariu(scenariuID)
);

select * from Scriitori

create table Director(
    directorID int,
	nume varchar(500),
	prenume varchar(500),
	varsta int,
	primary key(directorID)
);

select * from Director
drop table Director

create table Filme(
    filmID SERIAL PRIMARY KEY,
    directorID int,
	genID int,
	actorID int,
	scenariuID int,
	titlu text,
	durata varchar,
	descriere text,
	an_aparitie int,
    categorie_varsta varchar,
	
	CONSTRAINT fk_director
	   FOREIGN KEY(directorID)
	     REFERENCES Director(directorID),
	
	CONSTRAINT fk_gen
	   FOREIGN KEY(genID)
	     REFERENCES Genuri(genID),
	
	CONSTRAINT fk_scenariu
	   FOREIGN KEY(scenariuID)
	     REFERENCES Scenariu(scenariuID)
);

select * from Filme


create table FilmeGenuri(
     filmID int references Filme (filmID) on update cascade on delete cascade,
	 genID int references Genuri (genID) on update cascade,
    CONSTRAINT filme_genuri_pk
	   PRIMARY KEY (filmID,genID)
);

select * from FilmeGenuri

create table FilmeActori(
     filmID int references Filme (filmID) on update cascade on delete cascade,
	actorID int references Actori (actorID) on update cascade,
	CONSTRAINT filme_actori_pk
	  PRIMARY KEY (filmID,actorID)
);

select * from FilmeActori


select * from "AspNetUsers"


create table Seriale (
	serialID SERIAL primary key,
	titlu text,
	numar_episoade varchar,
	descriere text,
	actori text,
	ani_desfasurare int,
	statusul varchar,
	scriitori text,
	director varchar,
	genuri text,
	categorie_varsta varchar
)

select * from seriale 

drop table seriale
drop table filme