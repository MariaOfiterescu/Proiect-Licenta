create table Users(
    userid SERIAL PRIMARY KEY,
    email varchar(50) NOT NULL,
    firstName varchar(50) NOT NULL,
    password1 varchar(50) NOT NULL,
    unique(email)
)


select * from Users;
drop table Users;

create table Form(
    formID int ,
    email varchar(50) NOT NULL,
    titluri varchar(50) NOT NULL,
    gen varchar(20) NOT NULL,
    actori varchar(50) NOT NULL,
    an_aparitie varchar(50) NOT NULL,

    primary key(formID),

    CONSTRAINT fk_email
	   FOREIGN KEY(email)
	     REFERENCES Users(email)
);

select * from Form;
drop table form;

select * from actori;