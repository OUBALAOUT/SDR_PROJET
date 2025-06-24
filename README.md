Ce projet a pour but de concevoir une solution de surveillance de la température dans 
un environnement distribué, en combinant les technologies de l’IoT et les capacités de communication de CORBA.

#########  FICHIER SDR_SERVER_CLIENT  ########

Generer fichies idl:

> idlj -fall TemperatureService.idl

Compiler les fichiers java:

> javac TemperatureApp/*.java TemperatureImpl.java SensorClient.java ServerMain.java

Lancer nameservice :
> tnameserv -ORBInitialPort 
1050

Lancer le server:

> java -cp ".;mysql-connector-j-8.3.0/mysql-connector-j-8.3.0.jar" ServerMain -ORBInitialPort 1050

Envoyer les donnees par le client:

> java SensorClient -ORBInitialPort 1050 -ORBInitialHost localhost

####INTERFACE_WEB#####

lancer app flask:

> python app.py

NB:

Telecharger SGBD MYSQL et cree les tables.

Changer les information de base de donnees(Server implimentation et interface web).



