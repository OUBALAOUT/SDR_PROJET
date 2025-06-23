import TemperatureApp.*;
import org.omg.CosNaming.*;
import org.omg.CORBA.*;
import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;

public class SensorClient {
    public static void main(String args[]) {
        try {
            ORB orb = ORB.init(args, null);
            org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");
            NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);

            TemperatureService tempService = TemperatureServiceHelper.narrow(ncRef.resolve_str("TemperatureService"));

            // Capteur simulé
            BufferedReader br = new BufferedReader(new FileReader("data.csv"));
            String line;
            boolean skipHeader = true;

            while ((line = br.readLine()) != null) {
                if (skipHeader) {
                    skipHeader = false;
                    continue;
                }

                String[] parts = line.split(",");
                if (parts.length != 3) continue;

                String id = parts[0].trim();
                String capteur_id = parts[1].trim();
                float temp = Float.parseFloat(parts[2].trim());

            
                tempService.sendTemperature(id, capteur_id, temp);
                System.out.println("Température envoyée : " + temp);
                Thread.sleep(1000); // Simule un envoi toutes les secondes
        } 
         br.close();

        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}
