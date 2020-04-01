import psycopg2
import csv

#0ID,1"Name",2"Sex",3"Age",4"Height",5"Weight",6"Team",7"NOC",8"Games",9"Year",10"Season",11"City",12"Sport",13"Event",14"Medal"

archivo = open("athlete_events.csv")
reader = csv.reader(archivo,delimiter=',')

conn = psycopg2.connect(user = "postgres",
                              password = "estudiantes123",
                              host = "10.20.251.157",
                              port = "5432",
                              database = "olimpicos")
  
cur = conn.cursor()

for linea in reader:
    #Insertar equipos
    if(linea[5]=="NA"):
        linea[5]="0"
    if(linea[4]=="NA"):
        linea[4]="0"
    if(linea[3]=="NA"):
        linea[3]="0"
    kIdCompetidor=0
    kIdEquipo=0
    kIdTemporada=0
    kIdDeporte=0
    kIdEvento=0
    auxId=0
    aux=0
    auxRow=None
    sqlquery = "SELECT * FROM equipo WHERE n_nomequipo=%s"
    sqlinsert = "INSERT INTO equipo(n_nomequipo) values(%s);"
    cur.execute(sqlquery, (linea[6],))
    auxRow = cur.fetchone()
    if(auxRow!=None):
        auxId=auxRow[0]
        kIdEquipo=auxRow[0]
    if(auxId==0):
        cur.execute(sqlinsert, (linea[6],))
        conn.commit()
        cur.execute(sqlquery, (linea[6],))
        auxRow = cur.fetchone()
        if(auxRow!=None):
            auxId=auxRow[0]
            kIdEquipo=auxRow[0]

    #Insertar competidores
    auxId=0;
    auxRow=None;
    sqlquery = "SELECT * FROM competidor WHERE n_nomcompetidor=%s"
    sqlinsert = "INSERT INTO competidor(n_nomcompetidor,o_sexo,v_edad,v_estatura,v_peso,k_idequipo) values(%s,%s,%s,%s,%s,%s);"
    cur.execute(sqlquery, (linea[1],))
    auxRow = cur.fetchone()
    if(auxRow!=None):
        auxId=auxRow[0]
        kIdCompetidor=auxRow[0]
    if(auxId==0):
        cur.execute(sqlinsert, (linea[1],linea[2],float(linea[3]),float(linea[4]),float(linea[5]),kIdEquipo))
        conn.commit()
        cur.execute(sqlquery, (linea[1],))
        auxRow = cur.fetchone()
        if(auxRow!=None):
            auxId=auxRow[0]
            kIdCompetidor=auxRow[0]

    #Insertar temporadas
    auxId=0;
    auxRow=None;
    sqlquery = "SELECT * FROM temporada WHERE n_nomtemporada=%s"
    sqlinsert = "INSERT INTO temporada(n_nomtemporada) values(%s);"
    cur.execute(sqlquery, (linea[10],))
    auxRow = cur.fetchone()
    if(auxRow!=None):
        auxId=auxRow[0]
        kIdTemporada=auxRow[0]
    if(auxId==0):
        cur.execute(sqlinsert, (linea[10],))
        conn.commit()
        cur.execute(sqlquery, (linea[10],))
        auxRow = cur.fetchone()
        if(auxRow!=None):
            auxId=auxRow[0]
            kIdTemporada=auxRow[0]

    #Insertar deportes
    auxId=0;
    auxRow=None;
    sqlquery = "SELECT * FROM deporte WHERE n_nomdeporte=%s"
    sqlinsert = "INSERT INTO deporte(n_nomdeporte) values(%s);"
    cur.execute(sqlquery, (linea[12],))
    auxRow = cur.fetchone()
    if(auxRow!=None):
        auxId=auxRow[0]
        kIdDeporte=auxRow[0]
    if(auxId==0):
        cur.execute(sqlinsert, (linea[12],))
        conn.commit()
        cur.execute(sqlquery, (linea[12],))
        auxRow = cur.fetchone()
        if(auxRow!=None):
            auxId=auxRow[0]
            kIdDeporte=auxRow[0]

    #Insertar eventos
    auxId=0;
    auxRow=None;
    sqlquery = "SELECT * FROM evento WHERE n_nomevento=%s"
    sqlinsert = "INSERT INTO evento(n_nomevento,k_iddeporte,k_idtemporada) values(%s,%s,%s);"
    cur.execute(sqlquery, (linea[13],))
    auxRow = cur.fetchone()
    if(auxRow!=None):
        auxId=auxRow[0]
        kIdEvento=auxRow[0]
    if(auxId==0):
        cur.execute(sqlinsert, (linea[13],kIdDeporte,kIdTemporada))
        conn.commit()
        cur.execute(sqlquery, (linea[13],))
        auxRow = cur.fetchone()
        if(auxRow!=None):
            auxId=auxRow[0]
            kIdEvento=auxRow[0]

    #Insertar rompimientos
    auxRow=None;
    sqlquery = "SELECT * FROM competidor_evento WHERE k_idcompetidor=%s and k_idevento=%s and v_anio=%s"
    cur.execute(sqlquery, (kIdCompetidor,kIdEvento,int(linea[9])))
    auxRow = cur.fetchone()
    
    if(auxRow==None):
        sqlinsert = "INSERT INTO competidor_evento values(%s,%s,%s,%s);"
        cur.execute(sqlinsert, (kIdCompetidor,kIdEvento,int(linea[9]),linea[14]))
        conn.commit()
    
cur.close()
conn.close()
