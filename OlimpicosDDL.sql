/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 13.5 		*/
/*  Created On : 01-mar-2020 09:52:39 p.m. 				*/
/*  DBMS       : PostgreSQL 						*/
/* ---------------------------------------------------- */

/* Drop Sequences for Autonumber Columns */

 

 

 

 

 

 

 

 

 

 

/* Drop Tables */

DROP TABLE IF EXISTS Competidor CASCADE
;

DROP TABLE IF EXISTS Competidor_evento CASCADE
;

DROP TABLE IF EXISTS Deporte CASCADE
;

DROP TABLE IF EXISTS Equipo CASCADE
;

DROP TABLE IF EXISTS Evento CASCADE
;

DROP TABLE IF EXISTS Temporada CASCADE
;

/* Create Tables */

CREATE TABLE Competidor
(
	k_idcompetidor serial NOT NULL,
	n_nomcompetidor varchar(60) NOT NULL,
	o_sexo char(1) NOT NULL,
	v_edad numeric(4) NOT NULL,
	v_estatura numeric(5,2) NULL,
	v_peso numeric(5,2) NULL,
	k_idequipo serial NOT NULL
)
;

CREATE TABLE Competidor_evento
(
	k_idcompetidor serial NOT NULL,
	k_idevento serial NOT NULL,
	v_anio numeric(4) NOT NULL,
	o_medalla varchar(10) NOT NULL
)
;

CREATE TABLE Deporte
(
	k_iddeporte serial NOT NULL,
	n_nomdeporte varchar(50) NOT NULL
)
;

CREATE TABLE Equipo
(
	k_idequipo serial NOT NULL,
	n_nomequipo varchar(50) NOT NULL
)
;

CREATE TABLE Evento
(
	k_idevento serial NOT NULL,
	n_nomevento varchar(80) NOT NULL,
	k_iddeporte serial NOT NULL,
	k_idtemporada serial NOT NULL
)
;

CREATE TABLE Temporada
(
	k_idtemporada serial NOT NULL,
	n_nomtemporada varchar(15) NOT NULL
)
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE Competidor ADD CONSTRAINT PK_Competidor
	PRIMARY KEY (k_idcompetidor)
;

ALTER TABLE Competidor_evento ADD CONSTRAINT PK_Competidor_evento
	PRIMARY KEY (k_idcompetidor,k_idevento,v_anio)
;

ALTER TABLE Deporte ADD CONSTRAINT PK_Deporte
	PRIMARY KEY (k_iddeporte)
;

ALTER TABLE Equipo ADD CONSTRAINT PK_Equipo
	PRIMARY KEY (k_idequipo)
;

ALTER TABLE Evento ADD CONSTRAINT PK_Evento
	PRIMARY KEY (k_idevento)
;

CREATE INDEX IXFK_Evento_Temporada ON Evento (k_idtemporada ASC)
;

ALTER TABLE Temporada ADD CONSTRAINT PK_Temporada
	PRIMARY KEY (k_idtemporada)
;

/* Create Foreign Key Constraints */

ALTER TABLE Competidor ADD CONSTRAINT FK_Competidor_Equipo
	FOREIGN KEY (k_idequipo) REFERENCES Equipo (k_idequipo) ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE Competidor_evento ADD CONSTRAINT FK_Competidor_evento_Competidor
	FOREIGN KEY (k_idcompetidor) REFERENCES Competidor (k_idcompetidor) ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE Competidor_evento ADD CONSTRAINT FK_Competidor_evento_Evento
	FOREIGN KEY (k_idevento) REFERENCES Evento (k_idevento) ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE Evento ADD CONSTRAINT FK_Evento_Deporte
	FOREIGN KEY (k_iddeporte) REFERENCES Deporte (k_iddeporte) ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE Evento ADD CONSTRAINT FK_Evento_Temporada
	FOREIGN KEY (k_idtemporada) REFERENCES Temporada (k_idtemporada) ON DELETE No Action ON UPDATE No Action
;

/* Create Table Comments, Sequences for Autonumber Columns */

 

 

 

 

 

 

 

 

 

 
